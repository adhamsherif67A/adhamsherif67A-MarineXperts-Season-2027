from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('tf2_demo_pkg')
    rviz_config = os.path.join(pkg_share, 'rviz', 'tf_demo.rviz')

    return LaunchDescription([
        Node(
            package='tf2_demo_pkg',
            executable='static_sensor_broadcaster',
            name='static_sensor_broadcaster',
            output='screen',
        ),
        Node(
            package='tf2_demo_pkg',
            executable='dynamic_mock_broadcaster',
            name='dynamic_mock_broadcaster',
            output='screen',
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config],
        ),
    ])
