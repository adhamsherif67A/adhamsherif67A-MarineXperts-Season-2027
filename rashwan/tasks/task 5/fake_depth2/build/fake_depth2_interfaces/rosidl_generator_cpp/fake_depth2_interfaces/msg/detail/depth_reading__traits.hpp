// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fake_depth2_interfaces:msg/DepthReading.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__TRAITS_HPP_
#define FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fake_depth2_interfaces/msg/detail/depth_reading__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace fake_depth2_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const DepthReading & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: depth
  {
    out << "depth: ";
    rosidl_generator_traits::value_to_yaml(msg.depth, out);
    out << ", ";
  }

  // member: zero_offset
  {
    out << "zero_offset: ";
    rosidl_generator_traits::value_to_yaml(msg.zero_offset, out);
    out << ", ";
  }

  // member: threshold_crossed
  {
    out << "threshold_crossed: ";
    rosidl_generator_traits::value_to_yaml(msg.threshold_crossed, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DepthReading & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: depth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "depth: ";
    rosidl_generator_traits::value_to_yaml(msg.depth, out);
    out << "\n";
  }

  // member: zero_offset
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "zero_offset: ";
    rosidl_generator_traits::value_to_yaml(msg.zero_offset, out);
    out << "\n";
  }

  // member: threshold_crossed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "threshold_crossed: ";
    rosidl_generator_traits::value_to_yaml(msg.threshold_crossed, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DepthReading & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::msg::DepthReading & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::msg::DepthReading & msg)
{
  return fake_depth2_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::msg::DepthReading>()
{
  return "fake_depth2_interfaces::msg::DepthReading";
}

template<>
inline const char * name<fake_depth2_interfaces::msg::DepthReading>()
{
  return "fake_depth2_interfaces/msg/DepthReading";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::msg::DepthReading>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::msg::DepthReading>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fake_depth2_interfaces::msg::DepthReading>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__TRAITS_HPP_
