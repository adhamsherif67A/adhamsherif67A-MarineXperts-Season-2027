#!/usr/bin/env python3
"""
MAVROS Autotune Node for Position and Velocity Tuning
"""
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from mavros_msgs.msg import State, PositionTarget
from mavros_msgs.srv import SetMode, CommandBool, ParamGet, ParamSet
from geometry_msgs.msg import PoseStamped, TwistStamped
from std_srvs.srv import Trigger, SetBool
import numpy as np
import threading
import time
import math
from enum import Enum, auto

class AutotuneType(Enum):
    POSITION = auto()
    VELOCITY = auto()

class AutotuneAxis(Enum):
    SURGE = auto()  # North/X
    SWAY = auto()   # East/Y
    HEAVE = auto()  # Down/Z

class AutotuneState(Enum):
    IDLE = auto()
    PREPARING = auto()
    RUNNING = auto()
    FINISHED = auto()
    ERROR = auto()

class MAVROSAutotuneNode(Node):
    def __init__(self):
        super().__init__('mavros_autotune')
        
        # Parameters
        self.declare_parameter('axis', 'surge')
        self.declare_parameter('type', 'velocity')
        self.declare_parameter('step_magnitude', 0.5)  # m/s for velocity, m for position
        self.declare_parameter('timeout', 30.0)  # seconds
        self.declare_parameter('safety_radius', 2.0)  # meters
        
        # State
        self.current_state = State()
        self.current_pose = PoseStamped()
        self.current_velocity = TwistStamped()
        self.autotune_state = AutotuneState.IDLE
        self.autotune_thread = None
        self.stop_autotune = False
        
        # QoS profiles
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1
        )
        
        # Subscribers
        self.state_sub = self.create_subscription(
            State, '/mavros/state', self.state_callback, qos_profile)
        self.pose_sub = self.create_subscription(
            PoseStamped, '/mavros/local_position/pose', self.pose_callback, qos_profile)
        self.vel_sub = self.create_subscription(
            TwistStamped, '/mavros/local_position/velocity', self.velocity_callback, qos_profile)
        
        # Publishers
        self.setpoint_pub = self.create_publisher(
            PositionTarget, '/mavros/setpoint_raw/local', 10)
        
        # Service clients
        self.set_mode_client = self.create_client(SetMode, '/mavros/set_mode')
        self.arming_client = self.create_client(CommandBool, '/mavros/cmd/arming')
        self.param_get_client = self.create_client(ParamGet, '/mavros/param_get')
        self.param_set_client = self.create_client(ParamSet, '/mavros/param_set')
        
        # Services for external control
        self.start_autotune_service = self.create_service(
            Trigger, '~/start_autotune', self.start_autotune_callback)
        self.stop_autotune_service = self.create_service(
            Trigger, '~/stop_autotune', self.stop_autotune_callback)
        
        # Timer for publishing setpoints (at 20 Hz)
        self.timer = self.create_timer(0.05, self.setpoint_timer_callback)
        
        # Lock for thread safety
        self.lock = threading.Lock()
        
        self.get_logger().info('MAVROS Autotune Node initialized')
    
    def state_callback(self, msg):
        self.current_state = msg
    
    def pose_callback(self, msg):
        self.current_pose = msg
    
    def velocity_callback(self, msg):
        self.current_velocity = msg
    
    def start_autotune_callback(self, request, response):
        self.get_logger().info('Received start autotune request')
        if self.autotune_state != AutotuneState.IDLE:
            response.success = False
            response.message = 'Autotune already running'
            return response
        
        # Get parameters
        axis_str = self.get_parameter('axis').get_parameter_value().string_value
        type_str = self.get_parameter('type').get_parameter_value().string_value
        
        try:
            axis = AutotuneAxis[axis_str.upper()]
            atype = AutotuneType[type_str.upper()]
        except KeyError:
            response.success = False
            response.message = f'Invalid axis or type: axis={axis_str}, type={type_str}'
            return response
        
        self.autotune_state = AutotuneState.PREPARING
        self.stop_autotune = False
        self.autotune_thread = threading.Thread(
            target=self.autotune_thread_func,
            args=(axis, atype),
            daemon=True)
        self.autotune_thread.start()
        
        response.success = True
        response.message = 'Autotune started'
        return response
    
    def stop_autotune_callback(self, request, response):
        self.get_logger().info('Received stop autotune request')
        self.stop_autotune = True
        if self.autotune_thread and self.autotune_thread.is_alive():
            self.autotune_thread.join(timeout=5.0)
        self.autotune_state = AutotuneState.IDLE
        response.success = True
        response.message = 'Autotune stopped'
        return response
    
    def autotune_thread_func(self, axis, atype):
        try:
            self.get_logger().info(f'Starting autotune for axis={axis.name}, type={atype.name}')
            self.autotune_state = AutotuneState.RUNNING
            
            # Ensure we are connected
            if not self.wait_for_connection(timeout=10.0):
                self.get_logger().error('FCU connection timeout')
                self.autotune_state = AutotuneState.ERROR
                return
            
            # Set mode to GUIDED
            if not self.set_mode('GUIDED'):
                self.get_logger().error('Failed to set GUIDED mode')
                self.autotune_state = AutotuneState.ERROR
                return
            
            # Arm the vehicle
            if not self.arm_vehicle():
                self.get_logger().error('Failed to arm vehicle')
                self.autotune_state = AutotuneState.ERROR
                return
            
            # Hold position in other axes
            self.hold_position()
            
            # Run the actual tune procedure based on type
            if atype == AutotuneType.VELOCITY:
                self.tune_velocity(axis)
            else:  # POSITION
                self.tune_position(axis)
            
            self.get_logger().info('Autotune procedure finished')
        except Exception as e:
            self.get_logger().error(f'Autotune thread exception: {e}')
            self.autotune_state = AutotuneState.ERROR
        finally:
            self.autotune_state = AutotuneState.IDLE
            # Disarm? We'll leave it armed for safety; user can disarm manually.
            # self.disarm_vehicle()
    
    def wait_for_connection(self, timeout=10.0):
        start = self.get_clock().now()
        while (self.get_clock().now() - start).nanoseconds / 1e9 < timeout:
            if self.current_state.connected:
                return True
            time.sleep(0.1)
        return False
    
    def set_mode(self, mode):
        if not self.set_mode_client.wait_for_service(timeout=5.0):
            self.get_logger().error('SetMode service not available')
            return False
        req = SetMode.Request()
        req.custom_mode = mode
        future = self.set_mode_client.call_async(req)
        rclpy.spin_until_future_complete(self, future, timeout=5.0)
        if future.result() is not None:
            return future.result().mode_sent
        else:
            self.get_logger().error('SetMode service call failed')
            return False
    
    def arm_vehicle(self):
        if not self.arming_client.wait_for_service(timeout=5.0):
            self.get_logger().error('Arming service not available')
            return False
        req = CommandBool.Request()
        req.value = True
        future = self.arming_client.call_async(req)
        rclpy.spin_until_future_complete(self, future, timeout=5.0)
        if future.result() is not None:
            return future.result().success
        else:
            self.get_logger().error('Arming service call failed')
            return False
    
    def disarm_vehicle(self):
        if not self.arming_client.wait_for_service(timeout=5.0):
            self.get_logger().error('Arming service not available')
            return False
        req = CommandBool.Request()
        req.value = False
        future = self.arming_client.call_async(req)
        rclpy.spin_until_future_complete(self, future, timeout=5.0)
        if future.result() is not None:
            return future.result().success
        else:
            self.get_logger().error('Disarming service call failed')
            return False
    
    def hold_position(self):
        # Publish current position as setpoint to hold position
        # We'll do this in the timer callback continuously
        pass
    
    def tune_velocity(self, axis):
        self.get_logger().info(f'Tuning velocity for axis {axis.name}')
        # Placeholder for velocity tuning algorithm
        # We'll implement a simple step response method
        # For now, just log and wait
        duration = self.get_parameter('timeout').get_parameter_value().double_value
        start_time = self.get_clock().now()
        while (self.get_clock().now() - start_time).nanoseconds / 1e9 < duration and not self.stop_autotune:
            # Publish zero velocity setpoint (hold)
            self.publish_velocity_setpoint(0.0, 0.0, 0.0)
            time.sleep(0.1)
        self.get_logger().info('Velocity tune placeholder completed')
    
    def tune_position(self, axis):
        self.get_logger().info(f'Tuning position for axis {axis.name}')
        # Placeholder
        duration = self.get_parameter('timeout').get_parameter_value().double_value
        start_time = self.get_clock().now()
        while (self.get_clock().now() - start_time).nanoseconds / 1e9 < duration and not self.stop_autotune:
            # Publish zero velocity setpoint (hold)
            self.publish_velocity_setpoint(0.0, 0.0, 0.0)
            time.sleep(0.1)
        self.get_logger().info('Position tune placeholder completed')
    
    def publish_velocity_setpoint(self, vx, vy, vz):
        msg = PositionTarget()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.coordinate_frame = PositionTarget.FRAME_LOCAL_NED
        # Ignore position, acceleration, yaw
        msg.type_mask = (
            PositionTarget.IGNORE_PX | PositionTarget.IGNORE_PY | PositionTarget.IGNORE_PZ |
            PositionTarget.IGNORE_AFX | PositionTarget.IGNORE_AFY | PositionTarget.IGNORE_AFZ |
            PositionTarget.IGNORE_YAW | PositionTarget.IGNORE_YAW_RATE
        )
        msg.velocity.x = float(vx)
        msg.velocity.y = float(vy)
        msg.velocity.z = float(vz)
        self.setpoint_pub.publish(msg)
    
    def setpoint_timer_callback(self):
        # If we are in autotune running state, we publish setpoints based on the tune logic
        # For now, we just publish zero velocity to hold
        if self.autotune_state == AutotuneState.RUNNING:
            self.publish_velocity_setpoint(0.0, 0.0, 0.0)
        # Otherwise, we don't publish anything (let other controllers handle)

def main(args=None):
    rclpy.init(args=args)
    node = MAVROSAutotuneNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
