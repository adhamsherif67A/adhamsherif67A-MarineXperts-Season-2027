#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math

class DepthPublisherNode(Node):
    def __init__(self):
        super().__init__('depth_publisher')
        self.publisher_ = self.create_publisher(Float64, 'depth', 10)
        self.timer_ = self.create_timer(0.5, self.publish_depth)
        self.time_x_ = 0.0
        self.get_logger().info('Depth Publisher Node has been started.')

    def publish_depth(self):
        msg = Float64()
        msg.data = 50.0 + 50.0 * math.sin(self.time_x_)
        self.time_x_ += 0.2
        
        self.get_logger().info(f'Publishing Depth: {msg.data:.2f}')
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DepthPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()