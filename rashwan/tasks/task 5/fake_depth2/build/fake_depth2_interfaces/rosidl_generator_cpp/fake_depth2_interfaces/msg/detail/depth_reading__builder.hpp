// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fake_depth2_interfaces:msg/DepthReading.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__BUILDER_HPP_
#define FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fake_depth2_interfaces/msg/detail/depth_reading__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fake_depth2_interfaces
{

namespace msg
{

namespace builder
{

class Init_DepthReading_threshold_crossed
{
public:
  explicit Init_DepthReading_threshold_crossed(::fake_depth2_interfaces::msg::DepthReading & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::msg::DepthReading threshold_crossed(::fake_depth2_interfaces::msg::DepthReading::_threshold_crossed_type arg)
  {
    msg_.threshold_crossed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::msg::DepthReading msg_;
};

class Init_DepthReading_zero_offset
{
public:
  explicit Init_DepthReading_zero_offset(::fake_depth2_interfaces::msg::DepthReading & msg)
  : msg_(msg)
  {}
  Init_DepthReading_threshold_crossed zero_offset(::fake_depth2_interfaces::msg::DepthReading::_zero_offset_type arg)
  {
    msg_.zero_offset = std::move(arg);
    return Init_DepthReading_threshold_crossed(msg_);
  }

private:
  ::fake_depth2_interfaces::msg::DepthReading msg_;
};

class Init_DepthReading_depth
{
public:
  explicit Init_DepthReading_depth(::fake_depth2_interfaces::msg::DepthReading & msg)
  : msg_(msg)
  {}
  Init_DepthReading_zero_offset depth(::fake_depth2_interfaces::msg::DepthReading::_depth_type arg)
  {
    msg_.depth = std::move(arg);
    return Init_DepthReading_zero_offset(msg_);
  }

private:
  ::fake_depth2_interfaces::msg::DepthReading msg_;
};

class Init_DepthReading_header
{
public:
  Init_DepthReading_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DepthReading_depth header(::fake_depth2_interfaces::msg::DepthReading::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_DepthReading_depth(msg_);
  }

private:
  ::fake_depth2_interfaces::msg::DepthReading msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::msg::DepthReading>()
{
  return fake_depth2_interfaces::msg::builder::Init_DepthReading_header();
}

}  // namespace fake_depth2_interfaces

#endif  // FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__BUILDER_HPP_
