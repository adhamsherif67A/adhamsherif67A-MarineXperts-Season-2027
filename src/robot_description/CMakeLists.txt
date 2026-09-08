cmake_minimum_required(VERSION 3.8)

project(robot_description)

find_package(ament_cmake REQUIRED)

# Install directories into the share path
install(
    DIRECTORY config launch meshes textures urdf worlds 
    DESTINATION share/${PROJECT_NAME}
)

install(
    FILES package.xml
    DESTINATION share/${PROJECT_NAME}
)

ament_package()