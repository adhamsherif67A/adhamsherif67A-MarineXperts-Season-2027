// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from depth_interfaces:action/Dive.idl
// generated code does not contain a copyright notice

#ifndef DEPTH_INTERFACES__ACTION__DETAIL__DIVE__STRUCT_H_
#define DEPTH_INTERFACES__ACTION__DETAIL__DIVE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/Dive in the package depth_interfaces.
typedef struct depth_interfaces__action__Dive_Goal
{
  float target_depth;
} depth_interfaces__action__Dive_Goal;

// Struct for a sequence of depth_interfaces__action__Dive_Goal.
typedef struct depth_interfaces__action__Dive_Goal__Sequence
{
  depth_interfaces__action__Dive_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__action__Dive_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/Dive in the package depth_interfaces.
typedef struct depth_interfaces__action__Dive_Result
{
  bool success;
  float final_depth;
} depth_interfaces__action__Dive_Result;

// Struct for a sequence of depth_interfaces__action__Dive_Result.
typedef struct depth_interfaces__action__Dive_Result__Sequence
{
  depth_interfaces__action__Dive_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__action__Dive_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/Dive in the package depth_interfaces.
typedef struct depth_interfaces__action__Dive_Feedback
{
  float current_depth;
} depth_interfaces__action__Dive_Feedback;

// Struct for a sequence of depth_interfaces__action__Dive_Feedback.
typedef struct depth_interfaces__action__Dive_Feedback__Sequence
{
  depth_interfaces__action__Dive_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__action__Dive_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "depth_interfaces/action/detail/dive__struct.h"

/// Struct defined in action/Dive in the package depth_interfaces.
typedef struct depth_interfaces__action__Dive_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  depth_interfaces__action__Dive_Goal goal;
} depth_interfaces__action__Dive_SendGoal_Request;

// Struct for a sequence of depth_interfaces__action__Dive_SendGoal_Request.
typedef struct depth_interfaces__action__Dive_SendGoal_Request__Sequence
{
  depth_interfaces__action__Dive_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__action__Dive_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/Dive in the package depth_interfaces.
typedef struct depth_interfaces__action__Dive_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} depth_interfaces__action__Dive_SendGoal_Response;

// Struct for a sequence of depth_interfaces__action__Dive_SendGoal_Response.
typedef struct depth_interfaces__action__Dive_SendGoal_Response__Sequence
{
  depth_interfaces__action__Dive_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__action__Dive_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/Dive in the package depth_interfaces.
typedef struct depth_interfaces__action__Dive_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} depth_interfaces__action__Dive_GetResult_Request;

// Struct for a sequence of depth_interfaces__action__Dive_GetResult_Request.
typedef struct depth_interfaces__action__Dive_GetResult_Request__Sequence
{
  depth_interfaces__action__Dive_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__action__Dive_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "depth_interfaces/action/detail/dive__struct.h"

/// Struct defined in action/Dive in the package depth_interfaces.
typedef struct depth_interfaces__action__Dive_GetResult_Response
{
  int8_t status;
  depth_interfaces__action__Dive_Result result;
} depth_interfaces__action__Dive_GetResult_Response;

// Struct for a sequence of depth_interfaces__action__Dive_GetResult_Response.
typedef struct depth_interfaces__action__Dive_GetResult_Response__Sequence
{
  depth_interfaces__action__Dive_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__action__Dive_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "depth_interfaces/action/detail/dive__struct.h"

/// Struct defined in action/Dive in the package depth_interfaces.
typedef struct depth_interfaces__action__Dive_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  depth_interfaces__action__Dive_Feedback feedback;
} depth_interfaces__action__Dive_FeedbackMessage;

// Struct for a sequence of depth_interfaces__action__Dive_FeedbackMessage.
typedef struct depth_interfaces__action__Dive_FeedbackMessage__Sequence
{
  depth_interfaces__action__Dive_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__action__Dive_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DEPTH_INTERFACES__ACTION__DETAIL__DIVE__STRUCT_H_
