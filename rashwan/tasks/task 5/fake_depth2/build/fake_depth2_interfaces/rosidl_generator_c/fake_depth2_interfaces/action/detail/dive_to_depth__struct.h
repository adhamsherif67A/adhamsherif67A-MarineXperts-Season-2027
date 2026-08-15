// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fake_depth2_interfaces:action/DiveToDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__STRUCT_H_
#define FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/DiveToDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__action__DiveToDepth_Goal
{
  /// Target depth in meters (positive = deeper).
  float target_depth;
  /// Rate at which simulated depth approaches the target, in meters/second.
  /// If <= 0.0, the server falls back to its default dive rate parameter.
  float dive_rate;
} fake_depth2_interfaces__action__DiveToDepth_Goal;

// Struct for a sequence of fake_depth2_interfaces__action__DiveToDepth_Goal.
typedef struct fake_depth2_interfaces__action__DiveToDepth_Goal__Sequence
{
  fake_depth2_interfaces__action__DiveToDepth_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__action__DiveToDepth_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/DiveToDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__action__DiveToDepth_Result
{
  bool success;
  float final_depth;
  rosidl_runtime_c__String message;
} fake_depth2_interfaces__action__DiveToDepth_Result;

// Struct for a sequence of fake_depth2_interfaces__action__DiveToDepth_Result.
typedef struct fake_depth2_interfaces__action__DiveToDepth_Result__Sequence
{
  fake_depth2_interfaces__action__DiveToDepth_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__action__DiveToDepth_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/DiveToDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__action__DiveToDepth_Feedback
{
  float current_depth;
  float remaining_distance;
  float percent_complete;
} fake_depth2_interfaces__action__DiveToDepth_Feedback;

// Struct for a sequence of fake_depth2_interfaces__action__DiveToDepth_Feedback.
typedef struct fake_depth2_interfaces__action__DiveToDepth_Feedback__Sequence
{
  fake_depth2_interfaces__action__DiveToDepth_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__action__DiveToDepth_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "fake_depth2_interfaces/action/detail/dive_to_depth__struct.h"

/// Struct defined in action/DiveToDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  fake_depth2_interfaces__action__DiveToDepth_Goal goal;
} fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request;

// Struct for a sequence of fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request.
typedef struct fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__Sequence
{
  fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/DiveToDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response;

// Struct for a sequence of fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response.
typedef struct fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__Sequence
{
  fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/DiveToDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__action__DiveToDepth_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} fake_depth2_interfaces__action__DiveToDepth_GetResult_Request;

// Struct for a sequence of fake_depth2_interfaces__action__DiveToDepth_GetResult_Request.
typedef struct fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__Sequence
{
  fake_depth2_interfaces__action__DiveToDepth_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "fake_depth2_interfaces/action/detail/dive_to_depth__struct.h"

/// Struct defined in action/DiveToDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__action__DiveToDepth_GetResult_Response
{
  int8_t status;
  fake_depth2_interfaces__action__DiveToDepth_Result result;
} fake_depth2_interfaces__action__DiveToDepth_GetResult_Response;

// Struct for a sequence of fake_depth2_interfaces__action__DiveToDepth_GetResult_Response.
typedef struct fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__Sequence
{
  fake_depth2_interfaces__action__DiveToDepth_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "fake_depth2_interfaces/action/detail/dive_to_depth__struct.h"

/// Struct defined in action/DiveToDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  fake_depth2_interfaces__action__DiveToDepth_Feedback feedback;
} fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage;

// Struct for a sequence of fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage.
typedef struct fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__Sequence
{
  fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__STRUCT_H_
