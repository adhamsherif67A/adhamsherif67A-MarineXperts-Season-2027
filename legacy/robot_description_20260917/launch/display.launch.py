from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    package_share = Path(get_package_share_directory('robot_description'))
    urdf_path = package_share / 'urdf' / 'robot_description.urdf'
    robot_description = urdf_path.read_text()

    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_world_map',
            arguments=['0', '0', '0', '0', '0', '0', 'world', 'map'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_map_odom',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_odom_footprint',
            arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_footprint'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_footprint_base',
            arguments=['0', '0', '0', '0', '0', '0', 'base_footprint', 'base_link'],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
        ),
    ])
