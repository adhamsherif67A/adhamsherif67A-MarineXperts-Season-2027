#include "flight_state_monitor/state_monitor.hpp"

StateMonitor::StateMonitor()
: Node("flight_state_monitor"),
  first_message_(true),
  previous_connected_(false),
  previous_armed_(false),
  previous_mode_("")
{
  state_subscription_ = this->create_subscription<mavros_msgs::msg::State>(
    "/mavros/state",
    10,
    std::bind(&StateMonitor::stateCallback, this, std::placeholders::_1)
  );

  RCLCPP_INFO(
    this->get_logger(),
    "Flight State Monitor started."
  );

  RCLCPP_INFO(
    this->get_logger(),
    "Waiting for /mavros/state ..."
  );
}

void StateMonitor::stateCallback(
  const mavros_msgs::msg::State::SharedPtr msg)
{
  bool state_changed =
    first_message_ ||
    msg->connected != previous_connected_ ||
    msg->armed != previous_armed_ ||
    msg->mode != previous_mode_;

  if (!state_changed) {
    return;
  }

  RCLCPP_INFO(this->get_logger(), "================================");
  RCLCPP_INFO(this->get_logger(), "[STATE CHANGE]");

  RCLCPP_INFO(
    this->get_logger(),
    "Connection: %s",
    msg->connected ? "Connected" : "Disconnected"
  );

  RCLCPP_INFO(
    this->get_logger(),
    "Armed: %s",
    msg->armed ? "Armed" : "Disarmed"
  );

  RCLCPP_INFO(
    this->get_logger(),
    "Mode: %s",
    msg->mode.c_str()
  );

  RCLCPP_INFO(this->get_logger(), "================================");

  previous_connected_ = msg->connected;
  previous_armed_ = msg->armed;
  previous_mode_ = msg->mode;

  first_message_ = false;
}

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);

  auto node = std::make_shared<StateMonitor>();

  rclcpp::spin(node);

  rclcpp::shutdown();

  return 0;
}
