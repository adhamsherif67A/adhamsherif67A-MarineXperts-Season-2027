"""Launch file wrapping Mini-Project A + Mini-Project B into one system.

Starts:
  - depth_sensor_node  (publisher + /calibrate_depth service + /dive_to_depth action)
  - depth_monitor_node (subscriber that logs threshold-crossing warnings)

Launch arguments:
  params_file   Path to a YAML parameter file (defaults to config/params.yaml
                shipped with this package).
  depth_topic   Topic name both nodes should use for depth readings.
                Demonstrates a remapping applied consistently across nodes.
                Default: "depth".

Example:
  ros2 launch fake_depth2 fake_depth2.launch.py
  ros2 launch fake_depth2 fake_depth2.launch.py depth_topic:=depth_raw
  ros2 launch fake_depth2 fake_depth2.launch.py params_file:=/path/to/my_params.yaml
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    default_params_file = os.path.join(
        get_package_share_directory('fake_depth2'), 'config', 'params.yaml'
    )

    params_file_arg = DeclareLaunchArgument(
        'params_file',
        default_value=default_params_file,
        description='Full path to the parameter YAML file for both nodes.',
    )

    depth_topic_arg = DeclareLaunchArgument(
        'depth_topic',
        default_value='depth',
        description='Topic name used for DepthReading messages on both nodes.',
    )

    params_file = LaunchConfiguration('params_file')
    depth_topic = LaunchConfiguration('depth_topic')

    depth_sensor_node = Node(
        package='fake_depth2',
        executable='depth_sensor_node',
        name='depth_sensor_node',
        output='screen',
        parameters=[params_file],
        remappings=[('depth', depth_topic)],
    )

    depth_monitor_node = Node(
        package='fake_depth2',
        executable='depth_monitor_node',
        name='depth_monitor_node',
        output='screen',
        parameters=[params_file],
        remappings=[('depth', depth_topic)],
    )

    return LaunchDescription([
        params_file_arg,
        depth_topic_arg,
        depth_sensor_node,
        depth_monitor_node,
    ])
