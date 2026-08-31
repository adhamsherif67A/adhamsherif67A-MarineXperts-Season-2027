#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from mavros_msgs.msg import State

class FlightStateMonitor(Node):
    def __init__(self):
        super().__init__('flight_state_monitor')
        self.prev_connected = None
        self.prev_armed = None
        self.prev_mode = None
        self.subscription = self.create_subscription(State, '/mavros/state', self.state_callback, 10)
        self.get_logger().info('Flight State Monitor active. Listening to /mavros/state...')

    def state_callback(self, msg: State):
        if (msg.connected != self.prev_connected or msg.armed != self.prev_armed or msg.mode != self.prev_mode):
            self.prev_connected = msg.connected
            self.prev_armed = msg.armed
            self.prev_mode = msg.mode
            conn_status = 'CONNECTED' if msg.connected else 'DISCONNECTED'
            arm_status = 'ARMED' if msg.armed else 'DISARMED'
            mode_status = msg.mode if msg.mode else 'UNKNOWN'
            self.get_logger().info(f'\n[FLIGHT STATE UPDATE]\n  ├─ Link Status : {conn_status}\n  ├─ Armed State : {arm_status}\n  └─ Flight Mode : {mode_status}\n')

def main(args=None):
  rclpy.init(args=args)
  node = FlightStateMonitor()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  finally:
    if rclpy.ok():
      rclpy.shutdown()
    node.destroy_node()

if __name__ == '__main__':
    main()