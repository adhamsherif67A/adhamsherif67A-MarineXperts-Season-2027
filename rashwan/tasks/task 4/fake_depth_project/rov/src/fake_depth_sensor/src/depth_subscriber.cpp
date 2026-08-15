#include "fake_depth_sensor/depth_subscriber.hpp"

DepthSubscriber::DepthSubscriber()
    : Node("depth_subscriber"),
      depth_threshold_(5.0)
{
    subscription_ = this->create_subscription<std_msgs::msg::Float64>(
        "/depth",
        10,
        std::bind(
            &DepthSubscriber::depth_callback,
            this,
            std::placeholders::_1
        )
    );

    RCLCPP_INFO(
        this->get_logger(),
        "Depth Subscriber started. Threshold: %.2f m",
        depth_threshold_
    );
}

void DepthSubscriber::depth_callback(
    const std_msgs::msg::Float64::SharedPtr message)
{
    double current_depth = message->data;

    RCLCPP_INFO(
        this->get_logger(),
        "Received depth: %.2f m",
        current_depth
    );

    if (current_depth > depth_threshold_)
    {
        RCLCPP_WARN(
            this->get_logger(),
            "WARNING: Depth threshold exceeded! Current depth: %.2f m",
            current_depth
        );
    }
}
