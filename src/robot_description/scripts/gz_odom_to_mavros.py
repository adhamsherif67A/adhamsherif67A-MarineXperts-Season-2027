#!/usr/bin/env python3
"""Relay Gazebo ground-truth odometry to MAVROS ExternalNav.

Gazebo publishes odometry in ROS ENU / FLU conventions (``odom`` ->
``base_link``).  MAVROS' odometry input accepts those ROS conventions and
performs its own ENU/FLU to MAVLink NED/FRD conversion before sending the
ODOMETRY message to ArduPilot.  Keeping that conversion in MAVROS prevents a
second, error-prone frame conversion in the simulation description.
"""

import math

import rclpy
from nav_msgs.msg import Odometry
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy


class GazeboOdomToMavros(Node):
    """Publishes valid Gazebo odometry to MAVROS' ExternalNav input."""

    def __init__(self):
        super().__init__('gz_odom_to_mavros')
        self.declare_parameter('source_topic', '/odometry/gz')
        self.declare_parameter('target_topic', '/mavros/odometry/in')

        source = self.get_parameter('source_topic').value
        target = self.get_parameter('target_topic').value
        qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.RELIABLE)

        self.publisher = self.create_publisher(Odometry, target, qos)
        self.subscription = self.create_subscription(
            Odometry, source, self._odometry_callback, qos)
        self.get_logger().info(f'Relaying {source} to {target} for EKF3 ExternalNav')

    @staticmethod
    def _is_finite(message: Odometry) -> bool:
        pose = message.pose.pose
        twist = message.twist.twist
        values = (
            pose.position.x, pose.position.y, pose.position.z,
            pose.orientation.x, pose.orientation.y,
            pose.orientation.z, pose.orientation.w,
            twist.linear.x, twist.linear.y, twist.linear.z,
            twist.angular.x, twist.angular.y, twist.angular.z,
        )
        return all(math.isfinite(value) for value in values)

    def _odometry_callback(self, message: Odometry):
        if not self._is_finite(message):
            self.get_logger().warn('Discarding non-finite Gazebo odometry')
            return

        # MAVROS requires a local-world frame and an FLU vehicle frame.
        # The Gazebo OdometryPublisher already provides exactly these frames.
        message.header.frame_id = 'odom'
        message.child_frame_id = 'base_link'
        self.publisher.publish(message)


def main():
    rclpy.init()
    node = GazeboOdomToMavros()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    except Exception:
        # SIGTERM can shut down the ROS context while the executor is waiting.
        # Propagate real runtime faults, but exit cleanly after that shutdown.
        if rclpy.ok():
            raise
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
