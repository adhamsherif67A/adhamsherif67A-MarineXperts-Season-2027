// dynamic_mock_broadcaster.cpp
//
// ينشر transform متغيّر مع الوقت بين base_link وفريم وهمي اسمه mock_frame.
// ده بيمثّل حاجة بتتحرك فعليًا بالنسبة للروبوت (مش مثبتة)، زي:
//   - نتيجة تتبّع جسم متحرك (object tracking)
//   - أو ذراع/رأس بيدور
//   - أو ببساطة تمرين علشان تتأكد إن dynamic broadcasting شغّال صح.
//
// هنا الفريم بيتحرك في دايرة حوالين base_link، وبينشر على /tf
// (مش /tf_static) كل فترة زمنية ثابتة (timer)، وكل مرة بـ timestamp جديد.

#include <chrono>
#include <cmath>
#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"
#include "tf2/LinearMath/Quaternion.h"

using namespace std::chrono_literals;

class DynamicMockBroadcaster : public rclcpp::Node
{
public:
  DynamicMockBroadcaster() : Node("dynamic_mock_broadcaster"), angle_(0.0)
  {
    broadcaster_ = std::make_shared<tf2_ros::TransformBroadcaster>(this);

    // Timer بينادي على publish_dynamic_transform كل 50 مللي ثانية (20Hz)
    timer_ = this->create_wall_timer(
      50ms, std::bind(&DynamicMockBroadcaster::publish_dynamic_transform, this));
  }

private:
  void publish_dynamic_transform()
  {
    geometry_msgs::msg::TransformStamped t;

    // لازم كل مرة نحدّث الـ timestamp، لأن tf2 محتاج يعرف إن ده sample جديد
    t.header.stamp = this->get_clock()->now();
    t.header.frame_id = "base_link";
    t.child_frame_id = "mock_frame";

    // فريم بيتحرك في دايرة نصف قطرها 0.5 متر حوالين base_link
    double radius = 0.5;
    t.transform.translation.x = radius * std::cos(angle_);
    t.transform.translation.y = radius * std::sin(angle_);
    t.transform.translation.z = 0.0;

    // ندوّر الفريم مع اتجاه حركته على الدايرة
    tf2::Quaternion q;
    q.setRPY(0, 0, angle_);
    t.transform.rotation.x = q.x();
    t.transform.rotation.y = q.y();
    t.transform.rotation.z = q.z();
    t.transform.rotation.w = q.w();

    broadcaster_->sendTransform(t);

    angle_ += 0.05;
    if (angle_ > 2 * M_PI) {
      angle_ -= 2 * M_PI;
    }
  }

  std::shared_ptr<tf2_ros::TransformBroadcaster> broadcaster_;
  rclcpp::TimerBase::SharedPtr timer_;
  double angle_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<DynamicMockBroadcaster>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
