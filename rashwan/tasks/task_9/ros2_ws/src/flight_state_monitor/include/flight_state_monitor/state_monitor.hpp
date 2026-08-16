#ifndef FLIGHT_STATE_MONITOR__STATE_MONITOR_HPP_
#define FLIGHT_STATE_MONITOR__STATE_MONITOR_HPP_

#include <string>

#include "rclcpp/rclcpp.hpp"
#include "mavros_msgs/msg/state.hpp"

class StateMonitor : public rclcpp::Node
{
public:
  StateMonitor();

private:
  void stateCallback(const mavros_msgs::msg::State::SharedPtr msg);

  rclcpp::Subscription<mavros_msgs::msg::State>::SharedPtr state_subscription_;

  bool first_message_;

  bool previous_connected_;
  bool previous_armed_;
  std::string previous_mode_;
};

#endif
