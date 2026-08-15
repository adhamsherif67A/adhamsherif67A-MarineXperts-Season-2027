// depth_sensor_node.cpp
//
// Simulates a fake depth sensor (Mini-Project A) and extends it with:
//   - a /calibrate_depth Service to reset/calibrate the zero offset (Mini-Project B)
//   - a /dive_to_depth Action to simulate diving to a target depth with
//     live feedback and cancellation support (Mini-Project B)
//
// All simulation state (raw_depth_, zero_offset_, diving_) is protected by
// state_mutex_ because the publish timer and the action execution thread
// can run concurrently.

#include <chrono>
#include <cmath>
#include <functional>
#include <memory>
#include <mutex>
#include <random>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"

#include "fake_depth2_interfaces/msg/depth_reading.hpp"
#include "fake_depth2_interfaces/srv/calibrate_depth.hpp"
#include "fake_depth2_interfaces/action/dive_to_depth.hpp"

using namespace std::chrono_literals;
using namespace std::placeholders;

using DepthReading = fake_depth2_interfaces::msg::DepthReading;
using CalibrateDepth = fake_depth2_interfaces::srv::CalibrateDepth;
using DiveToDepth = fake_depth2_interfaces::action::DiveToDepth;
using GoalHandleDive = rclcpp_action::ServerGoalHandle<DiveToDepth>;

class DepthSensorNode : public rclcpp::Node
{
public:
  DepthSensorNode()
  : Node("depth_sensor_node"), rng_(std::random_device{}())
  {
    declare_parameters();
    read_static_parameters();

    // React to runtime changes of the tunable parameters (incl. zero_offset,
    // which is also how the calibration service applies its result).
    param_cb_handle_ = this->add_on_set_parameters_callback(
      std::bind(&DepthSensorNode::on_set_parameters, this, _1));

    publisher_ = this->create_publisher<DepthReading>("depth", 10);

    auto period = std::chrono::duration<double>(1.0 / publish_rate_hz_);
    timer_ = this->create_wall_timer(
      std::chrono::duration_cast<std::chrono::milliseconds>(period),
      std::bind(&DepthSensorNode::on_timer, this));

    calibrate_service_ = this->create_service<CalibrateDepth>(
      "calibrate_depth",
      std::bind(&DepthSensorNode::handle_calibrate, this, _1, _2));

    action_server_ = rclcpp_action::create_server<DiveToDepth>(
      this,
      "dive_to_depth",
      std::bind(&DepthSensorNode::handle_goal, this, _1, _2),
      std::bind(&DepthSensorNode::handle_cancel, this, _1),
      std::bind(&DepthSensorNode::handle_accepted, this, _1));

    start_time_ = this->now();

    RCLCPP_INFO(
      this->get_logger(),
      "depth_sensor_node up: mode=%s rate=%.2fHz baseline=%.2fm amplitude=%.2fm "
      "warn_threshold=%.2fm zero_offset=%.2fm",
      mode_.c_str(), publish_rate_hz_, baseline_depth_, amplitude_, warn_threshold_,
      zero_offset_);
  }

private:
  // ---------------------------------------------------------------- params
  void declare_parameters()
  {
    rcl_interfaces::msg::ParameterDescriptor desc;

    desc.description = "Publish rate for /depth, in Hz. Read once at startup.";
    this->declare_parameter<double>("publish_rate_hz", 5.0, desc);

    desc.description = "Simulation mode: 'sine' or 'random'.";
    this->declare_parameter<std::string>("mode", "sine", desc);

    desc.description = "Baseline (resting) depth in meters.";
    this->declare_parameter<double>("baseline_depth", 10.0, desc);

    desc.description = "Amplitude of the simulated depth variation, in meters.";
    this->declare_parameter<double>("amplitude", 5.0, desc);

    desc.description = "Period of the sine wave, in seconds (sine mode only).";
    this->declare_parameter<double>("period_s", 20.0, desc);

    desc.description = "Standard deviation of additive Gaussian noise, in meters.";
    this->declare_parameter<double>("noise_stddev", 0.05, desc);

    desc.description = "Depth (meters) at which a threshold-crossing flag is raised.";
    this->declare_parameter<double>("warn_threshold", 12.0, desc);

    desc.description = "Calibration offset added to the raw simulated depth.";
    this->declare_parameter<double>("zero_offset", 0.0, desc);

    desc.description = "Frame id used in published message headers.";
    this->declare_parameter<std::string>("frame_id", "depth_sensor_link", desc);

    desc.description = "Default dive rate (m/s) used when a goal doesn't specify one.";
    this->declare_parameter<double>("default_dive_rate", 0.5, desc);

    desc.description = "Control loop rate (Hz) used while executing a dive action.";
    this->declare_parameter<double>("dive_control_hz", 10.0, desc);

    desc.description = "Distance (m) from target within which a dive is considered complete.";
    this->declare_parameter<double>("dive_goal_tolerance", 0.05, desc);
  }

  void read_static_parameters()
  {
    publish_rate_hz_ = this->get_parameter("publish_rate_hz").as_double();
    mode_ = this->get_parameter("mode").as_string();
    baseline_depth_ = this->get_parameter("baseline_depth").as_double();
    amplitude_ = this->get_parameter("amplitude").as_double();
    period_s_ = this->get_parameter("period_s").as_double();
    noise_stddev_ = this->get_parameter("noise_stddev").as_double();
    warn_threshold_ = this->get_parameter("warn_threshold").as_double();
    zero_offset_ = this->get_parameter("zero_offset").as_double();
    frame_id_ = this->get_parameter("frame_id").as_string();
    default_dive_rate_ = this->get_parameter("default_dive_rate").as_double();
    dive_control_hz_ = this->get_parameter("dive_control_hz").as_double();
    dive_goal_tolerance_ = this->get_parameter("dive_goal_tolerance").as_double();
  }

  rcl_interfaces::msg::SetParametersResult on_set_parameters(
    const std::vector<rclcpp::Parameter> & params)
  {
    std::lock_guard<std::mutex> lock(state_mutex_);
    rcl_interfaces::msg::SetParametersResult result;
    result.successful = true;

    for (const auto & p : params) {
      if (p.get_name() == "zero_offset") {
        zero_offset_ = p.as_double();
      } else if (p.get_name() == "warn_threshold") {
        warn_threshold_ = p.as_double();
      } else if (p.get_name() == "amplitude") {
        amplitude_ = p.as_double();
      } else if (p.get_name() == "baseline_depth") {
        baseline_depth_ = p.as_double();
      } else if (p.get_name() == "period_s") {
        if (p.as_double() <= 0.0) {
          result.successful = false;
          result.reason = "period_s must be > 0";
          continue;
        }
        period_s_ = p.as_double();
      } else if (p.get_name() == "noise_stddev") {
        noise_stddev_ = p.as_double();
      } else if (p.get_name() == "mode") {
        const auto & m = p.as_string();
        if (m != "sine" && m != "random") {
          result.successful = false;
          result.reason = "mode must be 'sine' or 'random'";
          continue;
        }
        mode_ = m;
      } else if (p.get_name() == "default_dive_rate") {
        default_dive_rate_ = p.as_double();
      } else if (p.get_name() == "dive_control_hz") {
        dive_control_hz_ = p.as_double();
      } else if (p.get_name() == "dive_goal_tolerance") {
        dive_goal_tolerance_ = p.as_double();
      }
    }
    return result;
  }

  // -------------------------------------------------------------- timer
  void on_timer()
  {
    DepthReading msg;
    double published_depth;
    bool crossed;

    {
      std::lock_guard<std::mutex> lock(state_mutex_);

      if (!diving_) {
        double t = (this->now() - start_time_).seconds();
        std::normal_distribution<double> noise(0.0, noise_stddev_);

        if (mode_ == "random") {
          std::uniform_real_distribution<double> uni(-1.0, 1.0);
          raw_depth_ = baseline_depth_ + amplitude_ * uni(rng_) + noise(rng_);
        } else {
          raw_depth_ = baseline_depth_ +
            amplitude_ * std::sin(2.0 * M_PI * t / period_s_) + noise(rng_);
        }
      }

      published_depth = raw_depth_ + zero_offset_;
      crossed = has_last_depth_ &&
        ((last_published_depth_ < warn_threshold_ && published_depth >= warn_threshold_) ||
         (last_published_depth_ >= warn_threshold_ && published_depth < warn_threshold_));
      last_published_depth_ = published_depth;
      has_last_depth_ = true;

      msg.zero_offset = static_cast<float>(zero_offset_);
    }

    msg.header.stamp = this->now();
    msg.header.frame_id = frame_id_;
    msg.depth = static_cast<float>(published_depth);
    msg.threshold_crossed = crossed;

    publisher_->publish(msg);
  }

  // ------------------------------------------------------------- service
  void handle_calibrate(
    const std::shared_ptr<CalibrateDepth::Request> request,
    std::shared_ptr<CalibrateDepth::Response> response)
  {
    double applied = request->reset_to_zero ? 0.0 : static_cast<double>(request->requested_offset);

    // Route through set_parameter so on_set_parameters keeps zero_offset_
    // and the "zero_offset" ROS parameter in sync.
    auto set_result = this->set_parameter(rclcpp::Parameter("zero_offset", applied));

    response->success = set_result.successful;
    response->applied_offset = static_cast<float>(applied);
    response->message = set_result.successful
      ? (request->reset_to_zero
           ? "Sensor calibrated: zero_offset reset to 0.0"
           : "Sensor calibrated: zero_offset set to requested value")
      : ("Calibration rejected: " + set_result.reason);

    RCLCPP_INFO(
      this->get_logger(), "Calibrate request (reset_to_zero=%d, requested=%.3f) -> %s",
      request->reset_to_zero, request->requested_offset, response->message.c_str());
  }

  // -------------------------------------------------------------- action
  rclcpp_action::GoalResponse handle_goal(
    const rclcpp_action::GoalUUID &, std::shared_ptr<const DiveToDepth::Goal> goal)
  {
    if (goal->target_depth < 0.0) {
      RCLCPP_WARN(this->get_logger(), "Rejecting dive goal: target_depth must be >= 0");
      return rclcpp_action::GoalResponse::REJECT;
    }
    RCLCPP_INFO(this->get_logger(), "Accepted dive goal to %.2fm", goal->target_depth);
    return rclcpp_action::GoalResponse::ACCEPT_AND_EXECUTE;
  }

  rclcpp_action::CancelResponse handle_cancel(const std::shared_ptr<GoalHandleDive>)
  {
    RCLCPP_INFO(this->get_logger(), "Received request to cancel dive");
    return rclcpp_action::CancelResponse::ACCEPT;
  }

  void handle_accepted(const std::shared_ptr<GoalHandleDive> goal_handle)
  {
    std::thread{std::bind(&DepthSensorNode::execute_dive, this, _1), goal_handle}.detach();
  }

  void execute_dive(const std::shared_ptr<GoalHandleDive> goal_handle)
  {
    const auto goal = goal_handle->get_goal();
    const double target = goal->target_depth;

    double rate, control_hz, tolerance, start_depth, offset_snapshot;
    {
      std::lock_guard<std::mutex> lock(state_mutex_);
      rate = goal->dive_rate > 0.0 ? goal->dive_rate : default_dive_rate_;
      control_hz = dive_control_hz_ > 0.0 ? dive_control_hz_ : 10.0;
      tolerance = dive_goal_tolerance_;
      start_depth = raw_depth_;
      offset_snapshot = zero_offset_;
      diving_ = true;
    }

    const double total_distance = std::fabs(target - start_depth);
    auto feedback = std::make_shared<DiveToDepth::Feedback>();
    auto result = std::make_shared<DiveToDepth::Result>();
    rclcpp::Rate loop_rate(control_hz);

    while (rclcpp::ok()) {
      if (goal_handle->is_canceling()) {
        double final_depth;
        {
          std::lock_guard<std::mutex> lock(state_mutex_);
          diving_ = false;
          final_depth = raw_depth_ + zero_offset_;
        }
        result->success = false;
        result->final_depth = static_cast<float>(final_depth);
        result->message = "Dive canceled before reaching target";
        goal_handle->canceled(result);
        RCLCPP_INFO(this->get_logger(), "Dive canceled at %.2fm", final_depth);
        return;
      }

      double current_raw, remaining;
      {
        std::lock_guard<std::mutex> lock(state_mutex_);
        const double step = rate / control_hz;
        if (raw_depth_ < target) {
          raw_depth_ = std::min(target, raw_depth_ + step);
        } else {
          raw_depth_ = std::max(target, raw_depth_ - step);
        }
        current_raw = raw_depth_;
        offset_snapshot = zero_offset_;
      }
      remaining = std::fabs(target - current_raw);

      feedback->current_depth = static_cast<float>(current_raw + offset_snapshot);
      feedback->remaining_distance = static_cast<float>(remaining);
      feedback->percent_complete = static_cast<float>(
        total_distance > 1e-6 ? 100.0 * (1.0 - remaining / total_distance) : 100.0);
      goal_handle->publish_feedback(feedback);

      if (remaining <= tolerance) {
        break;
      }
      loop_rate.sleep();
    }

    double final_depth;
    {
      std::lock_guard<std::mutex> lock(state_mutex_);
      diving_ = false;
      final_depth = raw_depth_ + zero_offset_;
    }

    result->success = true;
    result->final_depth = static_cast<float>(final_depth);
    result->message = "Reached target depth";
    goal_handle->succeed(result);
    RCLCPP_INFO(this->get_logger(), "Dive complete at %.2fm", final_depth);
  }

  // ----------------------------------------------------------------- state
  rclcpp::Publisher<DepthReading>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Service<CalibrateDepth>::SharedPtr calibrate_service_;
  rclcpp_action::Server<DiveToDepth>::SharedPtr action_server_;
  OnSetParametersCallbackHandle::SharedPtr param_cb_handle_;

  std::mt19937 rng_;
  rclcpp::Time start_time_;

  std::mutex state_mutex_;
  double raw_depth_{0.0};
  double last_published_depth_{0.0};
  bool has_last_depth_{false};
  bool diving_{false};

  // parameters (guarded by state_mutex_ where mutated at runtime)
  double publish_rate_hz_{5.0};
  std::string mode_{"sine"};
  double baseline_depth_{10.0};
  double amplitude_{5.0};
  double period_s_{20.0};
  double noise_stddev_{0.05};
  double warn_threshold_{12.0};
  double zero_offset_{0.0};
  std::string frame_id_{"depth_sensor_link"};
  double default_dive_rate_{0.5};
  double dive_control_hz_{10.0};
  double dive_goal_tolerance_{0.05};
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<DepthSensorNode>();
  rclcpp::executors::MultiThreadedExecutor executor;
  executor.add_node(node);
  executor.spin();
  rclcpp::shutdown();
  return 0;
}
