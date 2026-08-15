// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fake_depth2_interfaces:srv/CalibrateDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__BUILDER_HPP_
#define FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fake_depth2_interfaces/srv/detail/calibrate_depth__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fake_depth2_interfaces
{

namespace srv
{

namespace builder
{

class Init_CalibrateDepth_Request_requested_offset
{
public:
  explicit Init_CalibrateDepth_Request_requested_offset(::fake_depth2_interfaces::srv::CalibrateDepth_Request & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::srv::CalibrateDepth_Request requested_offset(::fake_depth2_interfaces::srv::CalibrateDepth_Request::_requested_offset_type arg)
  {
    msg_.requested_offset = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::srv::CalibrateDepth_Request msg_;
};

class Init_CalibrateDepth_Request_reset_to_zero
{
public:
  Init_CalibrateDepth_Request_reset_to_zero()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CalibrateDepth_Request_requested_offset reset_to_zero(::fake_depth2_interfaces::srv::CalibrateDepth_Request::_reset_to_zero_type arg)
  {
    msg_.reset_to_zero = std::move(arg);
    return Init_CalibrateDepth_Request_requested_offset(msg_);
  }

private:
  ::fake_depth2_interfaces::srv::CalibrateDepth_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::srv::CalibrateDepth_Request>()
{
  return fake_depth2_interfaces::srv::builder::Init_CalibrateDepth_Request_reset_to_zero();
}

}  // namespace fake_depth2_interfaces


namespace fake_depth2_interfaces
{

namespace srv
{

namespace builder
{

class Init_CalibrateDepth_Response_applied_offset
{
public:
  explicit Init_CalibrateDepth_Response_applied_offset(::fake_depth2_interfaces::srv::CalibrateDepth_Response & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::srv::CalibrateDepth_Response applied_offset(::fake_depth2_interfaces::srv::CalibrateDepth_Response::_applied_offset_type arg)
  {
    msg_.applied_offset = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::srv::CalibrateDepth_Response msg_;
};

class Init_CalibrateDepth_Response_message
{
public:
  explicit Init_CalibrateDepth_Response_message(::fake_depth2_interfaces::srv::CalibrateDepth_Response & msg)
  : msg_(msg)
  {}
  Init_CalibrateDepth_Response_applied_offset message(::fake_depth2_interfaces::srv::CalibrateDepth_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return Init_CalibrateDepth_Response_applied_offset(msg_);
  }

private:
  ::fake_depth2_interfaces::srv::CalibrateDepth_Response msg_;
};

class Init_CalibrateDepth_Response_success
{
public:
  Init_CalibrateDepth_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CalibrateDepth_Response_message success(::fake_depth2_interfaces::srv::CalibrateDepth_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_CalibrateDepth_Response_message(msg_);
  }

private:
  ::fake_depth2_interfaces::srv::CalibrateDepth_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::srv::CalibrateDepth_Response>()
{
  return fake_depth2_interfaces::srv::builder::Init_CalibrateDepth_Response_success();
}

}  // namespace fake_depth2_interfaces

#endif  // FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__BUILDER_HPP_
