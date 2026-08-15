cmake_minimum_required(VERSION 3.8)
project(fake_depth2)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(std_msgs REQUIRED)
find_package(fake_depth2_interfaces REQUIRED)

add_executable(depth_sensor_node src/depth_sensor_node.cpp)
ament_target_dependencies(depth_sensor_node rclcpp rclcpp_action std_msgs fake_depth2_interfaces)

add_executable(depth_monitor_node src/depth_monitor_node.cpp)
ament_target_dependencies(depth_monitor_node rclcpp fake_depth2_interfaces)

add_executable(calibrate_client src/calibrate_client.cpp)
ament_target_dependencies(calibrate_client rclcpp fake_depth2_interfaces)

add_executable(dive_client src/dive_client.cpp)
ament_target_dependencies(dive_client rclcpp rclcpp_action fake_depth2_interfaces)

install(TARGETS
  depth_sensor_node
  depth_monitor_node
  calibrate_client
  dive_client
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  config
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
