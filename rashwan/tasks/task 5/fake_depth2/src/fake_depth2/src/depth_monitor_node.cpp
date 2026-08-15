// depth_monitor_node.cpp
//
// Mini-Project A: subscribes to /depth and logs a warning whenever the
// reading crosses a configurable depth threshold (edge-triggered, so it
// warns once per crossing rather than on every message past the line).
//
// depth_threshold is a runtime-settable parameter (ros2 param set ...).

#include <functional>
#include <memory>
#include <mutex>

#include "rclcpp/rclcpp.hpp"
#include "fake_depth2_interfaces/msg/depth_reading.hpp"

using std::placeholders::_1;
using DepthReading = fake_depth2_interfaces::msg::DepthReading;

class DepthMonitorNode : public rclcpp::Node
{
public:
  DepthMonitorNode()
  : Node("depth_monitor_node")
  {
    rcl_interfaces::msg::ParameterDescriptor desc;
    desc.description = "Depth (meters) at which this monitor logs a crossing warning.";
    this->declare_parameter<double>("depth_threshold", 12.0, desc);
    threshold_ = this->get_parameter("depth_threshold").as_double();

    param_cb_handle_ = this->add_on_set_parameters_callback(
      std::bind(&DepthMonitorNode::on_set_parameters, this, _1));

    subscription_ = this->create_subscription<DepthReading>(
      "depth", 10, std::bind(&DepthMonitorNode::on_depth, this, _1));

    RCLCPP_INFO(this->get_logger(), "depth_monitor_node up: depth_threshold=%.2fm", threshold_);
  }

private:
  rcl_interfaces::msg::SetParametersResult on_set_parameters(
    const std::vector<rclcpp::Parameter> & params)
  {
    std::lock_guard<std::mutex> lock(mutex_);
    rcl_interfaces::msg::SetParametersResult result;
    result.successful = true;
    for (const auto & p : params) {
      if (p.get_name() == "depth_threshold") {
        threshold_ = p.as_double();
        RCLCPP_INFO(this->get_logger(), "depth_threshold updated to %.2fm", threshold_);
      }
    }
    return result;
  }

  void on_depth(const DepthReading::SharedPtr msg)
  {
    std::lock_guard<std::mutex> lock(mutex_);
    const double depth = msg->depth;

    const bool crossed = has_last_ &&
      ((last_depth_ < threshold_ && depth >= threshold_) ||
       (last_depth_ >= threshold_ && depth < threshold_));

    if (crossed) {
      const char * direction = (depth >= threshold_) ? "past" : "back above";
      RCLCPP_WARN(
        this->get_logger(),
        "Depth threshold crossed! current=%.2fm threshold=%.2fm (%s the line, zero_offset=%.2fm)",
        depth, threshold_, direction, msg->zero_offset);
    } else {
      RCLCPP_DEBUG(this->get_logger(), "depth=%.2fm (threshold=%.2fm)", depth, threshold_);
    }

    last_depth_ = depth;
    has_last_ = true;
  }

  rclcpp::Subscription<DepthReading>::SharedPtr subscription_;
  OnSetParametersCallbackHandle::SharedPtr param_cb_handle_;

  std::mutex mutex_;
  double threshold_{12.0};
  double last_depth_{0.0};
  bool has_last_{false};
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<DepthMonitorNode>());
  rclcpp::shutdown();
  return 0;
}
