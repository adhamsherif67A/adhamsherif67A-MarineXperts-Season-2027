// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from fake_depth2_interfaces:msg/DepthReading.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "fake_depth2_interfaces/msg/detail/depth_reading__rosidl_typesupport_introspection_c.h"
#include "fake_depth2_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "fake_depth2_interfaces/msg/detail/depth_reading__functions.h"
#include "fake_depth2_interfaces/msg/detail/depth_reading__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  fake_depth2_interfaces__msg__DepthReading__init(message_memory);
}

void fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_fini_function(void * message_memory)
{
  fake_depth2_interfaces__msg__DepthReading__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_member_array[4] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fake_depth2_interfaces__msg__DepthReading, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "depth",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fake_depth2_interfaces__msg__DepthReading, depth),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "zero_offset",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fake_depth2_interfaces__msg__DepthReading, zero_offset),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "threshold_crossed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(fake_depth2_interfaces__msg__DepthReading, threshold_crossed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_members = {
  "fake_depth2_interfaces__msg",  // message namespace
  "DepthReading",  // message name
  4,  // number of fields
  sizeof(fake_depth2_interfaces__msg__DepthReading),
  fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_member_array,  // message members
  fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_init_function,  // function to initialize message memory (memory has to be allocated)
  fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_type_support_handle = {
  0,
  &fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_fake_depth2_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, fake_depth2_interfaces, msg, DepthReading)() {
  fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_type_support_handle.typesupport_identifier) {
    fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &fake_depth2_interfaces__msg__DepthReading__rosidl_typesupport_introspection_c__DepthReading_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
