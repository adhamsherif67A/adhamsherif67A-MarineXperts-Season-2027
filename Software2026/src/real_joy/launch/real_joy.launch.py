"""Mako app by default; opt into the retained hardware control stack explicitly."""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    hardware=LaunchConfiguration('hardware')
    return LaunchDescription([
        DeclareLaunchArgument('hardware',default_value='false',choices=['true','false']),
        Node(package='real_joy',executable='rov_gui_gst.py',name='mako_gui',
             condition=UnlessCondition(hardware),output='screen'),
        Node(package='joy',executable='game_controller_node',
             condition=IfCondition(hardware),output='screen'),
        Node(package='real_joy',executable='realjoy_node',
             condition=IfCondition(hardware),output='screen'),
        Node(package='real_joy',executable='zed_to_mavros_pose.py',
             condition=IfCondition(hardware),output='screen'),
        Node(package='real_joy',executable='rov_gui_gst_legacy.py',
             condition=IfCondition(hardware),output='screen'),
    ])
