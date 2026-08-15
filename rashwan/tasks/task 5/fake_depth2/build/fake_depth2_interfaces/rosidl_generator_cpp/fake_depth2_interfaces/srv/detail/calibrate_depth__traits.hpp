// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fake_depth2_interfaces:srv/CalibrateDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__TRAITS_HPP_
#define FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fake_depth2_interfaces/srv/detail/calibrate_depth__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace fake_depth2_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const CalibrateDepth_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: reset_to_zero
  {
    out << "reset_to_zero: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_to_zero, out);
    out << ", ";
  }

  // member: requested_offset
  {
    out << "requested_offset: ";
    rosidl_generator_traits::value_to_yaml(msg.requested_offset, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CalibrateDepth_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: reset_to_zero
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset_to_zero: ";
    rosidl_generator_traits::value_to_yaml(msg.reset_to_zero, out);
    out << "\n";
  }

  // member: requested_offset
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "requested_offset: ";
    rosidl_generator_traits::value_to_yaml(msg.requested_offset, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CalibrateDepth_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::srv::CalibrateDepth_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::srv::CalibrateDepth_Request & msg)
{
  return fake_depth2_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::srv::CalibrateDepth_Request>()
{
  return "fake_depth2_interfaces::srv::CalibrateDepth_Request";
}

template<>
inline const char * name<fake_depth2_interfaces::srv::CalibrateDepth_Request>()
{
  return "fake_depth2_interfaces/srv/CalibrateDepth_Request";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::srv::CalibrateDepth_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::srv::CalibrateDepth_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<fake_depth2_interfaces::srv::CalibrateDepth_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace fake_depth2_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const CalibrateDepth_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << ", ";
  }

  // member: applied_offset
  {
    out << "applied_offset: ";
    rosidl_generator_traits::value_to_yaml(msg.applied_offset, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CalibrateDepth_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }

  // member: applied_offset
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "applied_offset: ";
    rosidl_generator_traits::value_to_yaml(msg.applied_offset, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CalibrateDepth_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::srv::CalibrateDepth_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::srv::CalibrateDepth_Response & msg)
{
  return fake_depth2_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::srv::CalibrateDepth_Response>()
{
  return "fake_depth2_interfaces::srv::CalibrateDepth_Response";
}

template<>
inline const char * name<fake_depth2_interfaces::srv::CalibrateDepth_Response>()
{
  return "fake_depth2_interfaces/srv/CalibrateDepth_Response";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::srv::CalibrateDepth_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::srv::CalibrateDepth_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fake_depth2_interfaces::srv::CalibrateDepth_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fake_depth2_interfaces::srv::CalibrateDepth>()
{
  return "fake_depth2_interfaces::srv::CalibrateDepth";
}

template<>
inline const char * name<fake_depth2_interfaces::srv::CalibrateDepth>()
{
  return "fake_depth2_interfaces/srv/CalibrateDepth";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::srv::CalibrateDepth>
  : std::integral_constant<
    bool,
    has_fixed_size<fake_depth2_interfaces::srv::CalibrateDepth_Request>::value &&
    has_fixed_size<fake_depth2_interfaces::srv::CalibrateDepth_Response>::value
  >
{
};

template<>
struct has_bounded_size<fake_depth2_interfaces::srv::CalibrateDepth>
  : std::integral_constant<
    bool,
    has_bounded_size<fake_depth2_interfaces::srv::CalibrateDepth_Request>::value &&
    has_bounded_size<fake_depth2_interfaces::srv::CalibrateDepth_Response>::value
  >
{
};

template<>
struct is_service<fake_depth2_interfaces::srv::CalibrateDepth>
  : std::true_type
{
};

template<>
struct is_service_request<fake_depth2_interfaces::srv::CalibrateDepth_Request>
  : std::true_type
{
};

template<>
struct is_service_response<fake_depth2_interfaces::srv::CalibrateDepth_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__TRAITS_HPP_
