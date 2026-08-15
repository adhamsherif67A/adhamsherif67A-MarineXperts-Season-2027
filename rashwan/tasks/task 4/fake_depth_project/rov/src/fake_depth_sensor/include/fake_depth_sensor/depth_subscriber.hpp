#ifndef FAKE_DEPTH_SENSOR__DEPTH_SUBSCRIBER_HPP_
#define FAKE_DEPTH_SENSOR__DEPTH_SUBSCRIBER_HPP_

#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/float64.hpp>

#include <memory>

class DepthSubscriber : public rclcpp::Node
{
public:
    DepthSubscriber();

private:
    void depth_callback(
        const std_msgs::msg::Float64::SharedPtr message);

    rclcpp::Subscription<std_msgs::msg::Float64>::SharedPtr subscription_;

    double depth_threshold_;
};

#endif  // FAKE_DEPTH_SENSOR__DEPTH_SUBSCRIBER_HPP_
