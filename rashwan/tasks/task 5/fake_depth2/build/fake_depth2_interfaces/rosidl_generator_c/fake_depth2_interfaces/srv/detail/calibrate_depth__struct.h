// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fake_depth2_interfaces:srv/CalibrateDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__STRUCT_H_
#define FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/CalibrateDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__srv__CalibrateDepth_Request
{
  bool reset_to_zero;
  float requested_offset;
} fake_depth2_interfaces__srv__CalibrateDepth_Request;

// Struct for a sequence of fake_depth2_interfaces__srv__CalibrateDepth_Request.
typedef struct fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence
{
  fake_depth2_interfaces__srv__CalibrateDepth_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/CalibrateDepth in the package fake_depth2_interfaces.
typedef struct fake_depth2_interfaces__srv__CalibrateDepth_Response
{
  bool success;
  rosidl_runtime_c__String message;
  float applied_offset;
} fake_depth2_interfaces__srv__CalibrateDepth_Response;

// Struct for a sequence of fake_depth2_interfaces__srv__CalibrateDepth_Response.
typedef struct fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence
{
  fake_depth2_interfaces__srv__CalibrateDepth_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__STRUCT_H_
