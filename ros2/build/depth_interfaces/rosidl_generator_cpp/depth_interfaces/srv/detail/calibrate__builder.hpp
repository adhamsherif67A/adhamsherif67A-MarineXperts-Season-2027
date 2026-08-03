// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from depth_interfaces:srv/Calibrate.idl
// generated code does not contain a copyright notice

#ifndef DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__BUILDER_HPP_
#define DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "depth_interfaces/srv/detail/calibrate__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace depth_interfaces
{

namespace srv
{

namespace builder
{

class Init_Calibrate_Request_zero_offset
{
public:
  Init_Calibrate_Request_zero_offset()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::depth_interfaces::srv::Calibrate_Request zero_offset(::depth_interfaces::srv::Calibrate_Request::_zero_offset_type arg)
  {
    msg_.zero_offset = std::move(arg);
    return std::move(msg_);
  }

private:
  ::depth_interfaces::srv::Calibrate_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::depth_interfaces::srv::Calibrate_Request>()
{
  return depth_interfaces::srv::builder::Init_Calibrate_Request_zero_offset();
}

}  // namespace depth_interfaces


namespace depth_interfaces
{

namespace srv
{

namespace builder
{

class Init_Calibrate_Response_message
{
public:
  explicit Init_Calibrate_Response_message(::depth_interfaces::srv::Calibrate_Response & msg)
  : msg_(msg)
  {}
  ::depth_interfaces::srv::Calibrate_Response message(::depth_interfaces::srv::Calibrate_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::depth_interfaces::srv::Calibrate_Response msg_;
};

class Init_Calibrate_Response_success
{
public:
  Init_Calibrate_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Calibrate_Response_message success(::depth_interfaces::srv::Calibrate_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_Calibrate_Response_message(msg_);
  }

private:
  ::depth_interfaces::srv::Calibrate_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::depth_interfaces::srv::Calibrate_Response>()
{
  return depth_interfaces::srv::builder::Init_Calibrate_Response_success();
}

}  // namespace depth_interfaces

#endif  // DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__BUILDER_HPP_
