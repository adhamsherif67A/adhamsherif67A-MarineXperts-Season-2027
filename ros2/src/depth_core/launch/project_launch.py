import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='depth_core',
            executable='fake_sensor_node',
            name='fake_depth_sensor',
            output='screen',
            parameters=[
                {'dive_step': 1.5} # Injects the parameter at runtime
            ]
        )
    ])