#ifndef FAKE_DEPTH_SENSOR__DEPTH_PUBLISHER_HPP_
#define FAKE_DEPTH_SENSOR__DEPTH_PUBLISHER_HPP_

#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/float64.hpp>

#include <memory>

class DepthPublisher : public rclcpp::Node
{
public:
    DepthPublisher();

private:
    void publish_depth();

    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;

    double time_;
};

#endif  // FAKE_DEPTH_SENSOR__DEPTH_PUBLISHER_HPP_
