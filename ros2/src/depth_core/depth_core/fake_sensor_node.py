import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from std_msgs.msg import Float32

# Import the custom interfaces you just built
from depth_interfaces.srv import Calibrate
from depth_interfaces.action import Dive 

class FakeDepthSensor(Node):
    def __init__(self):
        super().__init__('fake_depth_sensor')
        self.current_depth = 0.0
        self.declare_parameter('dive_step', 0.5) # Default step size is 0.5m
        
        # Continuous Depth Publisher
        self.depth_pub = self.create_publisher(Float32, 'current_depth', 10)
        self.timer = self.create_timer(1.0, self.publish_depth)
        
        # Calibration Service Server
        self.cal_srv = self.create_service(Calibrate, 'calibrate_sensor', self.calibrate_callback)
        
        # Dive Action Server
        self._action_server = ActionServer(
            self,
            Dive,
            'dive_action',
            self.execute_dive_callback
        )
        self.get_logger().info("Fake Depth Sensor is online.")

    def publish_depth(self):
        msg = Float32()
        msg.data = self.current_depth
        self.depth_pub.publish(msg)

    def calibrate_callback(self, request, response):
        self.get_logger().info(f"Calibration requested. Setting depth to {request.zero_offset}m")
        self.current_depth = request.zero_offset
        response.success = True
        response.message = f"Sensor successfully calibrated to {self.current_depth}m."
        return response

    def execute_dive_callback(self, goal_handle):
        target = goal_handle.request.target_depth
        self.get_logger().info(f"Executing dive to target: {target}m")
        
        feedback_msg = Dive.Feedback()
        # Read the parameter dynamically at runtime
        step_size = self.get_parameter('dive_step').get_parameter_value().double_value
        step = step_size if target > self.current_depth else -step_size
        
        # Simulate the dive loop with feedback
        while abs(target - self.current_depth) > 0.1:
            self.current_depth += step
            feedback_msg.current_depth = self.current_depth
            self.get_logger().info(f"Dive feedback: {self.current_depth:.1f}m")
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.5) 
            
        # Snap to exact target upon completion
        self.current_depth = target
        goal_handle.succeed()
        
        # Return final result
        result = Dive.Result()
        result.success = True
        result.final_depth = self.current_depth
        self.get_logger().info("Dive action complete.")
        return result

def main(args=None):
    rclpy.init(args=args)
    node = FakeDepthSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()