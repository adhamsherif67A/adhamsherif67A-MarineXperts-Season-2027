// static_sensor_broadcaster.cpp
//
// ينشر transform ثابت (لا يتغيّر مع الوقت) بين base_link وفريم حساس وهمي.
// ده بيمثّل حساس مركّب فعليًا على جسم الروبوت في مكان معروف وثابت،
// زي كاميرا أو LiDAR مثبت في مكان معين وما بيتحركش بالنسبة للـ base_link.
//
// النشر هنا يحصل مرة واحدة بس عند تشغيل النود (latched topic /tf_static)،
// مش على loop زي الـ dynamic broadcaster.

#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/static_transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"
#include "tf2/LinearMath/Quaternion.h"

class StaticSensorBroadcaster : public rclcpp::Node
{
public:
  StaticSensorBroadcaster() : Node("static_sensor_broadcaster")
  {
    // tf2_ros::StaticTransformBroadcaster بينشر على /tf_static
    // وهو latched يعني أي subscriber جديد (زي RViz2) هيستلم آخر قيمة فورًا
    // حتى لو اشترك بعد ما النشر حصل.
    static_broadcaster_ = std::make_shared<tf2_ros::StaticTransformBroadcaster>(this);

    publish_static_transform();
  }

private:
  void publish_static_transform()
  {
    geometry_msgs::msg::TransformStamped t;

    t.header.stamp = this->get_clock()->now();
    t.header.frame_id = "base_link";      // الأب (parent frame)
    t.child_frame_id = "mock_sensor_link"; // الابن (child frame) - الحساس الوهمي

    // مكان الحساس بالنسبة لـ base_link (مثال: حساس مركّب لفوق وقدام شوية)
    t.transform.translation.x = 0.20;  // 20 سم لقدام
    t.transform.translation.y = 0.00;
    t.transform.translation.z = 0.15;  // 15 سم لفوق

    // orientation (بدون دوران هنا، quaternion محايد)
    tf2::Quaternion q;
    q.setRPY(0, 0, 0);
    t.transform.rotation.x = q.x();
    t.transform.rotation.y = q.y();
    t.transform.rotation.z = q.z();
    t.transform.rotation.w = q.w();

    static_broadcaster_->sendTransform(t);

    RCLCPP_INFO(this->get_logger(),
      "Publishing static transform: base_link -> mock_sensor_link (once)");
  }

  std::shared_ptr<tf2_ros::StaticTransformBroadcaster> static_broadcaster_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<StaticSensorBroadcaster>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
