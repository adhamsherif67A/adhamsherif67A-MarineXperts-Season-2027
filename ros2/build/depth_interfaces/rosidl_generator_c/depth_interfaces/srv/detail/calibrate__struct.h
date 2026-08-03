// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from depth_interfaces:srv/Calibrate.idl
// generated code does not contain a copyright notice

#ifndef DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__STRUCT_H_
#define DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Calibrate in the package depth_interfaces.
typedef struct depth_interfaces__srv__Calibrate_Request
{
  float zero_offset;
} depth_interfaces__srv__Calibrate_Request;

// Struct for a sequence of depth_interfaces__srv__Calibrate_Request.
typedef struct depth_interfaces__srv__Calibrate_Request__Sequence
{
  depth_interfaces__srv__Calibrate_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__srv__Calibrate_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Calibrate in the package depth_interfaces.
typedef struct depth_interfaces__srv__Calibrate_Response
{
  bool success;
  rosidl_runtime_c__String message;
} depth_interfaces__srv__Calibrate_Response;

// Struct for a sequence of depth_interfaces__srv__Calibrate_Response.
typedef struct depth_interfaces__srv__Calibrate_Response__Sequence
{
  depth_interfaces__srv__Calibrate_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} depth_interfaces__srv__Calibrate_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__STRUCT_H_
