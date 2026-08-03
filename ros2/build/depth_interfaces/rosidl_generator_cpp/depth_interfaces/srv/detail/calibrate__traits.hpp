// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from depth_interfaces:srv/Calibrate.idl
// generated code does not contain a copyright notice

#ifndef DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__TRAITS_HPP_
#define DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "depth_interfaces/srv/detail/calibrate__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace depth_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Calibrate_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: zero_offset
  {
    out << "zero_offset: ";
    rosidl_generator_traits::value_to_yaml(msg.zero_offset, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Calibrate_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: zero_offset
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "zero_offset: ";
    rosidl_generator_traits::value_to_yaml(msg.zero_offset, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Calibrate_Request & msg, bool use_flow_style = false)
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

}  // namespace depth_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use depth_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const depth_interfaces::srv::Calibrate_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  depth_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use depth_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const depth_interfaces::srv::Calibrate_Request & msg)
{
  return depth_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<depth_interfaces::srv::Calibrate_Request>()
{
  return "depth_interfaces::srv::Calibrate_Request";
}

template<>
inline const char * name<depth_interfaces::srv::Calibrate_Request>()
{
  return "depth_interfaces/srv/Calibrate_Request";
}

template<>
struct has_fixed_size<depth_interfaces::srv::Calibrate_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<depth_interfaces::srv::Calibrate_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<depth_interfaces::srv::Calibrate_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace depth_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Calibrate_Response & msg,
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
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Calibrate_Response & msg,
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Calibrate_Response & msg, bool use_flow_style = false)
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

}  // namespace depth_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use depth_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const depth_interfaces::srv::Calibrate_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  depth_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use depth_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const depth_interfaces::srv::Calibrate_Response & msg)
{
  return depth_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<depth_interfaces::srv::Calibrate_Response>()
{
  return "depth_interfaces::srv::Calibrate_Response";
}

template<>
inline const char * name<depth_interfaces::srv::Calibrate_Response>()
{
  return "depth_interfaces/srv/Calibrate_Response";
}

template<>
struct has_fixed_size<depth_interfaces::srv::Calibrate_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<depth_interfaces::srv::Calibrate_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<depth_interfaces::srv::Calibrate_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<depth_interfaces::srv::Calibrate>()
{
  return "depth_interfaces::srv::Calibrate";
}

template<>
inline const char * name<depth_interfaces::srv::Calibrate>()
{
  return "depth_interfaces/srv/Calibrate";
}

template<>
struct has_fixed_size<depth_interfaces::srv::Calibrate>
  : std::integral_constant<
    bool,
    has_fixed_size<depth_interfaces::srv::Calibrate_Request>::value &&
    has_fixed_size<depth_interfaces::srv::Calibrate_Response>::value
  >
{
};

template<>
struct has_bounded_size<depth_interfaces::srv::Calibrate>
  : std::integral_constant<
    bool,
    has_bounded_size<depth_interfaces::srv::Calibrate_Request>::value &&
    has_bounded_size<depth_interfaces::srv::Calibrate_Response>::value
  >
{
};

template<>
struct is_service<depth_interfaces::srv::Calibrate>
  : std::true_type
{
};

template<>
struct is_service_request<depth_interfaces::srv::Calibrate_Request>
  : std::true_type
{
};

template<>
struct is_service_response<depth_interfaces::srv::Calibrate_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__TRAITS_HPP_
