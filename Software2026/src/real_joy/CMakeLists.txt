cmake_minimum_required(VERSION 3.8)
project(real_joy)

# Compile options (nice warnings)
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rcl_interfaces REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(mavros_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(std_srvs REQUIRED)

# Single CPP (main)
add_executable(realjoy_node
  src/joystick.cpp
)

# Include headers
target_include_directories(realjoy_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)

# Link ROS 2 deps
target_compile_features(realjoy_node PRIVATE cxx_std_17)

ament_target_dependencies(realjoy_node
  rcl_interfaces
  rclcpp
  sensor_msgs
  mavros_msgs
  std_srvs
)

# Install executable
install(TARGETS realjoy_node
  DESTINATION lib/${PROJECT_NAME}
)

# Install headers
install(DIRECTORY include/
  DESTINATION include
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install config files (CycloneDDS configuration)
install(DIRECTORY config/
  DESTINATION share/${PROJECT_NAME}/config
)

# Install Python scripts
install(PROGRAMS
  src/zed_to_mavros_pose.py
  DESTINATION lib/${PROJECT_NAME}

)

install(PROGRAMS
  src/rov_gui_gst.py
  DESTINATION lib/${PROJECT_NAME}

)

# This is a workaround to ensure setup.py is used for Python entry points
# The setup.py must be in the package root and properly configured
# Mako desktop application and retained hardware GUI.
install(DIRECTORY src/mako_station DESTINATION lib/${PROJECT_NAME}
  PATTERN "__pycache__" EXCLUDE)
install(PROGRAMS src/rov_gui_gst_legacy.py DESTINATION lib/${PROJECT_NAME})

ament_package()
