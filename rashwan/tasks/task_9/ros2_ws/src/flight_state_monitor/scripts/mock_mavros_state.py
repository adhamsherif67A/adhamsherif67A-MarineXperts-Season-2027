#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from mavros_msgs.msg import State


class MockMavrosState(Node):

    def __init__(self):
        super().__init__('mock_mavros_state')

        self.publisher = self.create_publisher(
            State,
            '/mavros/state',
            10
        )

        self.timer = self.create_timer(
            2.0,
            self.publish_state
        )

        self.counter = 0

        self.get_logger().info(
            'Mock MAVROS State Publisher started.'
        )

    def publish_state(self):

        msg = State()

        # Change the state every few messages
        if self.counter < 3:

            msg.connected = False
            msg.armed = False
            msg.mode = "MANUAL"

        elif self.counter < 6:

            msg.connected = True
            msg.armed = False
            msg.mode = "MANUAL"

        elif self.counter < 9:

            msg.connected = True
            msg.armed = True
            msg.mode = "MANUAL"

        else:

            msg.connected = True
            msg.armed = True
            msg.mode = "STABILIZE"

        self.publisher.publish(msg)

        self.get_logger().info(
            f"Published -> "
            f"connected={msg.connected}, "
            f"armed={msg.armed}, "
            f"mode={msg.mode}"
        )

        self.counter += 1


def main(args=None):

    rclpy.init(args=args)

    node = MockMavrosState()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
