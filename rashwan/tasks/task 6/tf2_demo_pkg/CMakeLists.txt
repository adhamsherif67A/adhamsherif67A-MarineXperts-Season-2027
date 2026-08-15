cmake_minimum_required(VERSION 3.8)
project(tf2_demo_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(geometry_msgs REQUIRED)

# ---- Static broadcaster node ----
add_executable(static_sensor_broadcaster src/static_sensor_broadcaster.cpp)
ament_target_dependencies(static_sensor_broadcaster
  rclcpp tf2 tf2_ros geometry_msgs)

# ---- Dynamic broadcaster node ----
add_executable(dynamic_mock_broadcaster src/dynamic_mock_broadcaster.cpp)
ament_target_dependencies(dynamic_mock_broadcaster
  rclcpp tf2 tf2_ros geometry_msgs)

install(TARGETS
  static_sensor_broadcaster
  dynamic_mock_broadcaster
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
