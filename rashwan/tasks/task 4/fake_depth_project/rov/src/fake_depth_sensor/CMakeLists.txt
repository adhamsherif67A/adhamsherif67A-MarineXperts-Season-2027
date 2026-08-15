cmake_minimum_required(VERSION 3.8)

project(fake_depth_sensor)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(
  include
)

add_library(depth_publisher_lib
  src/depth_publisher.cpp
)

ament_target_dependencies(
  depth_publisher_lib
  rclcpp
  std_msgs
)

add_executable(depth_publisher
  src/publisher_main.cpp
)

target_link_libraries(
  depth_publisher
  depth_publisher_lib
)

ament_target_dependencies(
  depth_publisher
  rclcpp
  std_msgs
)

add_library(depth_subscriber_lib
  src/depth_subscriber.cpp
)

ament_target_dependencies(
  depth_subscriber_lib
  rclcpp
  std_msgs
)

add_executable(depth_subscriber
  src/subscriber_main.cpp
)

target_link_libraries(
  depth_subscriber
  depth_subscriber_lib
)

ament_target_dependencies(
  depth_subscriber
  rclcpp
  std_msgs
)

install(
  DIRECTORY include/
  DESTINATION include
)

install(
  TARGETS
    depth_publisher_lib
    depth_publisher
    depth_subscriber_lib
    depth_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
