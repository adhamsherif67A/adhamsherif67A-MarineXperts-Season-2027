// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fake_depth2_interfaces:msg/DepthReading.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__STRUCT_H_
#define FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/DepthReading in the package fake_depth2_interfaces.
/**
  * A single simulated depth sensor reading.
 */
typedef struct fake_depth2_interfaces__msg__DepthReading
{
  std_msgs__msg__Header header;
  /// Depth in meters, positive = deeper.
  float depth;
  /// The zero-offset (calibration) currently applied to this reading.
  float zero_offset;
  /// True if this reading crossed the configured warning threshold
  /// relative to the previous reading (edge-triggered).
  bool threshold_crossed;
} fake_depth2_interfaces__msg__DepthReading;

// Struct for a sequence of fake_depth2_interfaces__msg__DepthReading.
typedef struct fake_depth2_interfaces__msg__DepthReading__Sequence
{
  fake_depth2_interfaces__msg__DepthReading * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fake_depth2_interfaces__msg__DepthReading__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__STRUCT_H_
