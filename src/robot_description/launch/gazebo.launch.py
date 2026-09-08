import os
import xacro
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'robot_description'
    package_share = Path(get_package_share_directory(package_name))

    # Path to the parent share directory so Gazebo finds 'model://robot_description'
    pkg_share_parent = str(package_share.parent)

    urdf_path = package_share / 'urdf' / 'robot_description.urdf'
    
    # ==========================================================
    # COMPILE XACRO: This dynamically injects your separate 
    # ardupilot.xacro file into the URDF before launching.
    # ==========================================================
    doc = xacro.process_file(str(urdf_path))
    robot_description = doc.toxml()

    world_path = package_share / 'worlds' / 'pool.sdf'
    ros_gz_sim_share = Path(get_package_share_directory('ros_gz_sim'))

    # Environment variable for Gazebo Harmonic resources
    gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=[
            pkg_share_parent,
            ':' + os.environ.get('GZ_SIM_RESOURCE_PATH', '')
        ]
    )

    return LaunchDescription([
        gz_resource_path,

        # Start Gazebo Harmonic
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(str(ros_gz_sim_share / 'launch' / 'gz_sim.launch.py')),
            launch_arguments={'gz_args': f'-r {world_path}'}.items(),
        ),

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': True
            }],
        ),

        # Spawn Mako underwater
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=[
                '-name', 'mako',
                '-topic', 'robot_description',
                '-x', '0.0',
                '-y', '0.0',
                '-z', '-1.0',  # Spawns exactly 1 meter underwater
            ],
            output='screen',
        ),

        # ==========================================================
        # ROS-Gazebo Bridge
        # ==========================================================
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                # Bridge Mako's dynamic TF from the Odometry Publisher
                '/model/mako/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
                
                # Bridge Mako's joint states using your exact SDF world name
                '/world/CompetitionWorld2025/model/mako/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model',
                
                # Thrusters (Updated to match URDF's 't1_joint' naming)
                '/model/mako/joint/t1_joint/cmd_thrust@std_msgs/msg/Float64]gz.msgs.Double',
                '/model/mako/joint/t2_joint/cmd_thrust@std_msgs/msg/Float64]gz.msgs.Double',
                '/model/mako/joint/t3_joint/cmd_thrust@std_msgs/msg/Float64]gz.msgs.Double',
                '/model/mako/joint/t4_joint/cmd_thrust@std_msgs/msg/Float64]gz.msgs.Double',
                '/model/mako/joint/t5_joint/cmd_thrust@std_msgs/msg/Float64]gz.msgs.Double',
                '/model/mako/joint/t6_joint/cmd_thrust@std_msgs/msg/Float64]gz.msgs.Double',

                # ==================================
                # ZED 2i RGBD CAMERA BRIDGES
                # ==================================
                '/robot_description/zed2i/image@sensor_msgs/msg/Image[gz.msgs.Image',
                '/robot_description/zed2i/depth_image@sensor_msgs/msg/Image[gz.msgs.Image',
                '/robot_description/zed2i/points@sensor_msgs/msg/PointCloud2[gz.msgs.PointCloudPacked',
                '/robot_description/zed2i/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo',
            ],
            remappings=[
                # Remap to standard ROS 2 topics for RViz
                ('/model/mako/tf', '/tf'),
                ('/world/CompetitionWorld2025/model/mako/joint_state', '/joint_states'),
                
                # Simplify camera topics for easier access in RViz
                ('/robot_description/zed2i/image', '/zed2i/image_raw'),
                ('/robot_description/zed2i/depth_image', '/zed2i/depth/image_raw'),
                ('/robot_description/zed2i/points', '/zed2i/points'),
                ('/robot_description/zed2i/camera_info', '/zed2i/camera_info'),
            ],
            output='screen'
        ),

        # ==========================================================
        # Static Transforms
        # ==========================================================
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_world_map',
            arguments=['--frame-id', 'world', '--child-frame-id', 'map'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_map_odom',
            arguments=['--frame-id', 'map', '--child-frame-id', 'odom'],
        ),
        
        # CAMERA OPTICAL FRAME: Rotates the point cloud so it points forward in RViz
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_zed_optical',
            arguments=['0', '0', '0', '-1.5708', '0', '-1.5708', 'zed_link', 'zed_link_optical'],
        ),
    ])