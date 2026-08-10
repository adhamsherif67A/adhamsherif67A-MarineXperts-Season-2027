#include <chrono>
#include <cmath>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/transform_stamped.hpp"
#include "tf2_ros/static_transform_broadcaster.h"
#include "tf2_ros/transform_broadcaster.h"
#include "tf2/LinearMath/Quaternion.h"

using namespace std::chrono_literals;

class FrameDrillNode : public rclcpp::Node
{
public:
  FrameDrillNode()
  : Node("frame_drill_node"), angle_(0.0)
  {
    static_broadcaster_ = std::make_unique<tf2_ros::StaticTransformBroadcaster>(this);
    publishStaticTransform();

    dynamic_broadcaster_ = std::make_unique<tf2_ros::TransformBroadcaster>(this);
    
    timer_ = this->create_wall_timer(
      50ms, std::bind(&FrameDrillNode::publishDynamicTransform, this));
  }

private:
  void publishStaticTransform()
  {
    geometry_msgs::msg::TransformStamped t;
    t.header.stamp = this->get_clock()->now();
    t.header.frame_id = "base_link";
    t.child_frame_id = "mock_sensor_link";

    t.transform.translation.x = 0.2;
    t.transform.translation.y = 0.0;
    t.transform.translation.z = 0.1;

    tf2::Quaternion q;
    q.setRPY(0, 0, 0);
    t.transform.rotation.x = q.x();
    t.transform.rotation.y = q.y();
    t.transform.rotation.z = q.z();
    t.transform.rotation.w = q.w();

    static_broadcaster_->sendTransform(t);
  }

  void publishDynamicTransform()
  {
    geometry_msgs::msg::TransformStamped t;
    t.header.stamp = this->get_clock()->now();
    t.header.frame_id = "odom";
    t.child_frame_id = "base_link";

    double radius = 1.0;
    t.transform.translation.x = radius * cos(angle_);
    t.transform.translation.y = radius * sin(angle_);
    t.transform.translation.z = 0.0;

    tf2::Quaternion q;
    q.setRPY(0, 0, angle_ + (M_PI / 2.0));
    t.transform.rotation.x = q.x();
    t.transform.rotation.y = q.y();
    t.transform.rotation.z = q.z();
    t.transform.rotation.w = q.w();

    dynamic_broadcaster_->sendTransform(t);
    angle_ += 0.05; 
  }

  std::unique_ptr<tf2_ros::StaticTransformBroadcaster> static_broadcaster_;
  std::unique_ptr<tf2_ros::TransformBroadcaster> dynamic_broadcaster_;
  rclcpp::TimerBase::SharedPtr timer_;
  double angle_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<FrameDrillNode>());
  rclcpp::shutdown();
  return 0;
}