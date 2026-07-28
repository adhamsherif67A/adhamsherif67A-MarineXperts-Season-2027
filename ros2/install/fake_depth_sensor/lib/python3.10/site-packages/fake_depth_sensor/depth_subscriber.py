#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class DepthSubscriberNode(Node):
    def __init__(self):
        super().__init__('depth_subscriber')
        self.subscription_ = self.create_subscription(
            Float64,
            'depth',
            self.depth_callback,
            10
        )
        self.threshold_ = 80.0
        self.get_logger().info(f'Depth Subscriber started. Monitoring threshold: {self.threshold_}')

    def depth_callback(self, msg: Float64):
        if msg.data > self.threshold_:
            self.get_logger().warn(f'CRITICAL: Depth threshold exceeded! Reading: {msg.data:.2f}')
        else:
            self.get_logger().info(f'Depth OK: {msg.data:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = DepthSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()