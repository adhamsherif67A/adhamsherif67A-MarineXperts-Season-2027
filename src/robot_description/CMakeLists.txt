cmake_minimum_required(VERSION 3.8)

project(robot_description)

find_package(ament_cmake REQUIRED)

# Install directories into the share path
install(
    DIRECTORY config launch meshes urdf worlds
    DESTINATION share/${PROJECT_NAME}
)

install(
    FILES package.xml
    DESTINATION share/${PROJECT_NAME}
)

install(
    PROGRAMS
        scripts/gz_odom_to_mavros.py
        scripts/fix_ardusub_params.py
        scripts/local_waypoint_mission.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()
