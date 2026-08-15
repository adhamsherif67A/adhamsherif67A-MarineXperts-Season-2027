// calibrate_client.cpp
//
// Simple synchronous Service client for /calibrate_depth.
//
// Usage:
//   ros2 run fake_depth2 calibrate_client --reset
//   ros2 run fake_depth2 calibrate_client <offset_value>
//
// Example:
//   ros2 run fake_depth2 calibrate_client 2.5

#include <chrono>
#include <cstdlib>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "fake_depth2_interfaces/srv/calibrate_depth.hpp"

using namespace std::chrono_literals;
using CalibrateDepth = fake_depth2_interfaces::srv::CalibrateDepth;

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  if (argc < 2) {
    RCLCPP_ERROR(
      rclcpp::get_logger("calibrate_client"),
      "Usage: calibrate_client --reset | calibrate_client <offset_value>");
    rclcpp::shutdown();
    return 1;
  }

  auto node = rclcpp::Node::make_shared("calibrate_client");
  auto client = node->create_client<CalibrateDepth>("calibrate_depth");

  auto request = std::make_shared<CalibrateDepth::Request>();
  const std::string arg1 = argv[1];
  if (arg1 == "--reset") {
    request->reset_to_zero = true;
    request->requested_offset = 0.0f;
  } else {
    request->reset_to_zero = false;
    request->requested_offset = std::stof(arg1);
  }

  while (!client->wait_for_service(1s)) {
    if (!rclcpp::ok()) {
      RCLCPP_ERROR(node->get_logger(), "Interrupted while waiting for calibrate_depth service");
      rclcpp::shutdown();
      return 1;
    }
    RCLCPP_INFO(node->get_logger(), "Waiting for calibrate_depth service...");
  }

  auto future = client->async_send_request(request);
  if (rclcpp::spin_until_future_complete(node, future) == rclcpp::FutureReturnCode::SUCCESS) {
    auto response = future.get();
    RCLCPP_INFO(
      node->get_logger(), "success=%d applied_offset=%.3f message=\"%s\"",
      response->success, response->applied_offset, response->message.c_str());
  } else {
    RCLCPP_ERROR(node->get_logger(), "Failed to call calibrate_depth service");
  }

  rclcpp::shutdown();
  return 0;
}
