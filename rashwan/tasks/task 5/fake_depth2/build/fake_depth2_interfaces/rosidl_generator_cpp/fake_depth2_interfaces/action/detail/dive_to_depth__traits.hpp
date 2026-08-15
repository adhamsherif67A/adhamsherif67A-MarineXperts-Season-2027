// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fake_depth2_interfaces:action/DiveToDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__TRAITS_HPP_
#define FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fake_depth2_interfaces/action/detail/dive_to_depth__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace fake_depth2_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const DiveToDepth_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: target_depth
  {
    out << "target_depth: ";
    rosidl_generator_traits::value_to_yaml(msg.target_depth, out);
    out << ", ";
  }

  // member: dive_rate
  {
    out << "dive_rate: ";
    rosidl_generator_traits::value_to_yaml(msg.dive_rate, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DiveToDepth_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: target_depth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_depth: ";
    rosidl_generator_traits::value_to_yaml(msg.target_depth, out);
    out << "\n";
  }

  // member: dive_rate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dive_rate: ";
    rosidl_generator_traits::value_to_yaml(msg.dive_rate, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DiveToDepth_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::action::DiveToDepth_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::action::DiveToDepth_Goal & msg)
{
  return fake_depth2_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_Goal>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_Goal";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_Goal>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_Goal";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<fake_depth2_interfaces::action::DiveToDepth_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace fake_depth2_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const DiveToDepth_Result & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: final_depth
  {
    out << "final_depth: ";
    rosidl_generator_traits::value_to_yaml(msg.final_depth, out);
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
  const DiveToDepth_Result & msg,
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

  // member: final_depth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "final_depth: ";
    rosidl_generator_traits::value_to_yaml(msg.final_depth, out);
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

inline std::string to_yaml(const DiveToDepth_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::action::DiveToDepth_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::action::DiveToDepth_Result & msg)
{
  return fake_depth2_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_Result>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_Result";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_Result>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_Result";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_Result>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_Result>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fake_depth2_interfaces::action::DiveToDepth_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace fake_depth2_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const DiveToDepth_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: current_depth
  {
    out << "current_depth: ";
    rosidl_generator_traits::value_to_yaml(msg.current_depth, out);
    out << ", ";
  }

  // member: remaining_distance
  {
    out << "remaining_distance: ";
    rosidl_generator_traits::value_to_yaml(msg.remaining_distance, out);
    out << ", ";
  }

  // member: percent_complete
  {
    out << "percent_complete: ";
    rosidl_generator_traits::value_to_yaml(msg.percent_complete, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DiveToDepth_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: current_depth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_depth: ";
    rosidl_generator_traits::value_to_yaml(msg.current_depth, out);
    out << "\n";
  }

  // member: remaining_distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "remaining_distance: ";
    rosidl_generator_traits::value_to_yaml(msg.remaining_distance, out);
    out << "\n";
  }

  // member: percent_complete
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "percent_complete: ";
    rosidl_generator_traits::value_to_yaml(msg.percent_complete, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DiveToDepth_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::action::DiveToDepth_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::action::DiveToDepth_Feedback & msg)
{
  return fake_depth2_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_Feedback>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_Feedback";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_Feedback>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_Feedback";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<fake_depth2_interfaces::action::DiveToDepth_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "fake_depth2_interfaces/action/detail/dive_to_depth__traits.hpp"

namespace fake_depth2_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const DiveToDepth_SendGoal_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DiveToDepth_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DiveToDepth_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request & msg)
{
  return fake_depth2_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_SendGoal_Request";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace fake_depth2_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const DiveToDepth_SendGoal_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: accepted
  {
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << ", ";
  }

  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DiveToDepth_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accepted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << "\n";
  }

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DiveToDepth_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response & msg)
{
  return fake_depth2_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_SendGoal_Response";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_SendGoal>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_SendGoal";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_SendGoal>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_SendGoal";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>::value &&
    has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>::value &&
    has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<fake_depth2_interfaces::action::DiveToDepth_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace fake_depth2_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const DiveToDepth_GetResult_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DiveToDepth_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DiveToDepth_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::action::DiveToDepth_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::action::DiveToDepth_GetResult_Request & msg)
{
  return fake_depth2_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_GetResult_Request";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_GetResult_Request";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "fake_depth2_interfaces/action/detail/dive_to_depth__traits.hpp"

namespace fake_depth2_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const DiveToDepth_GetResult_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: result
  {
    out << "result: ";
    to_flow_style_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DiveToDepth_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result:\n";
    to_block_style_yaml(msg.result, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DiveToDepth_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::action::DiveToDepth_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::action::DiveToDepth_GetResult_Response & msg)
{
  return fake_depth2_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_GetResult_Response";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_GetResult_Response";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_Result>::value> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_Result>::value> {};

template<>
struct is_message<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_GetResult>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_GetResult";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_GetResult>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_GetResult";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>::value &&
    has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>::value &&
    has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>::value
  >
{
};

template<>
struct is_service<fake_depth2_interfaces::action::DiveToDepth_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "fake_depth2_interfaces/action/detail/dive_to_depth__traits.hpp"

namespace fake_depth2_interfaces
{

namespace action
{

inline void to_flow_style_yaml(
  const DiveToDepth_FeedbackMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: feedback
  {
    out << "feedback: ";
    to_flow_style_yaml(msg.feedback, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DiveToDepth_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback:\n";
    to_block_style_yaml(msg.feedback, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DiveToDepth_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use fake_depth2_interfaces::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  fake_depth2_interfaces::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fake_depth2_interfaces::action::to_yaml() instead")]]
inline std::string to_yaml(const fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage & msg)
{
  return fake_depth2_interfaces::action::to_yaml(msg);
}

template<>
inline const char * data_type<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage>()
{
  return "fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage";
}

template<>
inline const char * name<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage>()
{
  return "fake_depth2_interfaces/action/DiveToDepth_FeedbackMessage";
}

template<>
struct has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<fake_depth2_interfaces::action::DiveToDepth_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<fake_depth2_interfaces::action::DiveToDepth_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<fake_depth2_interfaces::action::DiveToDepth>
  : std::true_type
{
};

template<>
struct is_action_goal<fake_depth2_interfaces::action::DiveToDepth_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<fake_depth2_interfaces::action::DiveToDepth_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<fake_depth2_interfaces::action::DiveToDepth_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__TRAITS_HPP_
