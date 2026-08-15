// dive_client.cpp
//
// Action client for /dive_to_depth. Sends a goal, prints live feedback,
// and prints the final result. Ctrl+C cancels the in-flight goal cleanly.
//
// Usage:
//   ros2 run fake_depth2 dive_client <target_depth> [dive_rate]
//
// Example:
//   ros2 run fake_depth2 dive_client 25.0 1.0

#include <chrono>
#include <cstdlib>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "fake_depth2_interfaces/action/dive_to_depth.hpp"

using namespace std::chrono_literals;
using namespace std::placeholders;

using DiveToDepth = fake_depth2_interfaces::action::DiveToDepth;
using GoalHandleDive = rclcpp_action::ClientGoalHandle<DiveToDepth>;

class DiveClientNode : public rclcpp::Node
{
public:
  explicit DiveClientNode(float target_depth, float dive_rate)
  : Node("dive_client"), target_depth_(target_depth), dive_rate_(dive_rate)
  {
    client_ = rclcpp_action::create_client<DiveToDepth>(this, "dive_to_depth");
  }

  void send_goal()
  {
    using namespace std::chrono_literals;

    if (!client_->wait_for_action_server(5s)) {
      RCLCPP_ERROR(this->get_logger(), "dive_to_depth action server not available");
      rclcpp::shutdown();
      return;
    }

    auto goal_msg = DiveToDepth::Goal();
    goal_msg.target_depth = target_depth_;
    goal_msg.dive_rate = dive_rate_;

    auto options = rclcpp_action::Client<DiveToDepth>::SendGoalOptions();
    options.goal_response_callback = std::bind(&DiveClientNode::goal_response_cb, this, _1);
    options.feedback_callback = std::bind(&DiveClientNode::feedback_cb, this, _1, _2);
    options.result_callback = std::bind(&DiveClientNode::result_cb, this, _1);

    RCLCPP_INFO(
      this->get_logger(), "Sending dive goal: target_depth=%.2fm dive_rate=%.2fm/s",
      target_depth_, dive_rate_);
    client_->async_send_goal(goal_msg, options);
  }

private:
  void goal_response_cb(const GoalHandleDive::SharedPtr & goal_handle)
  {
    if (!goal_handle) {
      RCLCPP_ERROR(this->get_logger(), "Dive goal was rejected by server");
    } else {
      RCLCPP_INFO(this->get_logger(), "Dive goal accepted, diving...");
    }
  }

  void feedback_cb(
    GoalHandleDive::SharedPtr, const std::shared_ptr<const DiveToDepth::Feedback> feedback)
  {
    RCLCPP_INFO(
      this->get_logger(), "feedback: current_depth=%.2fm remaining=%.2fm complete=%.1f%%",
      feedback->current_depth, feedback->remaining_distance, feedback->percent_complete);
  }

  void result_cb(const GoalHandleDive::WrappedResult & result)
  {
    switch (result.code) {
      case rclcpp_action::ResultCode::SUCCEEDED:
        RCLCPP_INFO(
          this->get_logger(), "Dive succeeded: final_depth=%.2fm message=\"%s\"",
          result.result->final_depth, result.result->message.c_str());
        break;
      case rclcpp_action::ResultCode::ABORTED:
        RCLCPP_ERROR(this->get_logger(), "Dive aborted");
        break;
      case rclcpp_action::ResultCode::CANCELED:
        RCLCPP_WARN(
          this->get_logger(), "Dive canceled: final_depth=%.2fm", result.result->final_depth);
        break;
      default:
        RCLCPP_ERROR(this->get_logger(), "Unknown result code");
        break;
    }
    rclcpp::shutdown();
  }

  rclcpp_action::Client<DiveToDepth>::SharedPtr client_;
  float target_depth_;
  float dive_rate_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  if (argc < 2) {
    RCLCPP_ERROR(
      rclcpp::get_logger("dive_client"),
      "Usage: dive_client <target_depth> [dive_rate]");
    rclcpp::shutdown();
    return 1;
  }

  const float target_depth = std::stof(argv[1]);
  const float dive_rate = (argc >= 3) ? std::stof(argv[2]) : 0.0f;

  auto node = std::make_shared<DiveClientNode>(target_depth, dive_rate);
  node->send_goal();
  rclcpp::spin(node);
  return 0;
}
