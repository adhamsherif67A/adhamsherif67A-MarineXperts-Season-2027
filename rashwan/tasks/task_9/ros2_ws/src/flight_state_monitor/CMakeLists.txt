cmake_minimum_required(VERSION 3.8)

project(flight_state_monitor)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(mavros_msgs REQUIRED)

include_directories(
  include
)

add_executable(state_monitor
  src/state_monitor.cpp
)

ament_target_dependencies(state_monitor
  rclcpp
  mavros_msgs
)

install(
  PROGRAMS
    scripts/mock_mavros_state.py
  DESTINATION lib/${PROJECT_NAME}
)

install(
  TARGETS state_monitor
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY include/
  DESTINATION include
)

ament_package()
