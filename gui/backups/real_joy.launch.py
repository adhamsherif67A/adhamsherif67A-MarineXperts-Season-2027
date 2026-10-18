import os

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Get the package share directory
    pkg_share = os.path.dirname(__file__)
    
    # NOTE: Custom CycloneDDS configuration disabled due to invalid/deprecated options
    # If needed, create a valid cyclonedds.xml with current schema
    
    # Extend the current environment with our custom variables
    # This preserves all existing environment variables (LD_LIBRARY_PATH, PYTHONPATH, etc.)
    env = os.environ.copy()
    # Use default RMW implementation (Fast-RTPS by default in ROS2 Humble)
    # Uncomment the following lines to use CycloneDDS
    # env['CYCLONEDDS_URI'] = f'file://{cyclonedds_config}'
    # env['RMW_IMPLEMENTATION'] = 'rmw_cyclonedds_cpp'
    
    return LaunchDescription([
        # Joy controller node (from joy package)
        Node(
            package='joy',
            executable='game_controller_node',
            name='game_controller_node',
            output='screen',
            env=env
        ),
        
        # RealJoy C++ node
        Node(
            package='real_joy',
            executable='realjoy_node',
            name='real_joy_node',
            output='screen',
            env=env
        ),
        
        # ZED to MAVROS pose node (Python)
        Node(
            package='real_joy',
            executable='zed_to_mavros_pose.py',
            name='zed_to_mavros_pose',
            output='screen',
            env=env,
            ros_arguments=['--ros-args', '--log-level', 'info']
        ),
        
        # ROV GUI Dashboard
       Node(
            package='real_joy',
            executable='rov_gui_gst.py',
            name='rov_gui',
            output='screen',
            env=env
        ),
    ])
