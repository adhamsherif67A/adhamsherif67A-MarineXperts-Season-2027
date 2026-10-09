import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
import math
from transforms3d.euler import euler2quat

class ROVCircleNode(Node):
    def __init__(self):
        super().__init__('rov_circle_node')

        self.center_x = 0.0
        self.center_y = 0.0
        self.radius = 1.0        # ✅ متر واحد
        self.angular_speed = 0.2

        self.current_mode = ""
        self.start_time = None
        self.locked_depth = None  # ✅ هيتحفظ عمق اللحظة دي

        self.current_z = 0.0  # بيتحدث من الـ local position

        self.setpoint_pub = self.create_publisher(
            PoseStamped, '/mavros/setpoint_position/local', 10)

        self.state_sub = self.create_subscription(
            State, '/mavros/state', self.state_cb, 10)

        # ✅ Subscribe على العمق الحالي
        self.pose_sub = self.create_subscription(
            PoseStamped, '/mavros/local_position/pose', self.pose_cb, 10)

        self.timer = self.create_timer(0.05, self.control_loop)
        self.get_logger().info("ROV Circle Node Started.")

    def state_cb(self, msg):
        self.current_mode = msg.mode

    def pose_cb(self, msg):
        self.current_z = msg.pose.position.z  # ✅ بنحدّث العمق الحالي دايماً

    def control_loop(self):
        if self.current_mode != "GUIDED":
            self.get_logger().warn("Not in GUIDED mode!", throttle_duration_sec=2.0)
            self.start_time = None
            self.locked_depth = None  # ريست لو خرج من GUIDED
            return

        if self.start_time is None:
            self.start_time = self.get_clock().now().nanoseconds / 1e9
            self.locked_depth = self.current_z  # ✅ احفظ العمق اللي انت فيه دلوقتي
            self.get_logger().info(f"Circle started at depth: {self.locked_depth:.2f} m")

        t = self.get_clock().now().nanoseconds / 1e9 - self.start_time

        target_x = self.center_x + self.radius * math.cos(self.angular_speed * t)
        target_y = self.center_y + self.radius * math.sin(self.angular_speed * t)
        yaw = math.atan2(self.center_y - target_y, self.center_x - target_x)
        quat = euler2quat(0.0, 0.0, yaw, axes='sxyz')

        msg = PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "map"
        msg.pose.position.x = target_x
        msg.pose.position.y = target_y
        msg.pose.position.z = self.locked_depth  # ✅ العمق المحفوظ
        msg.pose.orientation.w = quat[0]
        msg.pose.orientation.x = quat[1]
        msg.pose.orientation.y = quat[2]
        msg.pose.orientation.z = quat[3]

        self.setpoint_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ROVCircleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()