#include "fake_depth_sensor/depth_subscriber.hpp"

#include <rclcpp/rclcpp.hpp>

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<DepthSubscriber>();

    rclcpp::spin(node);

    rclcpp::shutdown();

    return 0;
}
