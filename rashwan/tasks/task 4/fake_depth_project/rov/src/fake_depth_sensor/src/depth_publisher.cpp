#include "fake_depth_sensor/depth_publisher.hpp"

#include <cmath>

DepthPublisher::DepthPublisher()
    : Node("depth_publisher"),
      time_(0.0)
{
    publisher_ = this->create_publisher<std_msgs::msg::Float64>(
        "/depth",
        10
    );

    timer_ = this->create_wall_timer(
        std::chrono::milliseconds(500),
        std::bind(&DepthPublisher::publish_depth, this)
    );

    RCLCPP_INFO(this->get_logger(), "Depth Publisher started.");
}

void DepthPublisher::publish_depth()
{
    std_msgs::msg::Float64 message;

    message.data = 5.0 + 4.0 * std::sin(time_);

    publisher_->publish(message);

    RCLCPP_INFO(
        this->get_logger(),
        "Published depth: %.2f m",
        message.data
    );

    time_ += 0.3;
}
