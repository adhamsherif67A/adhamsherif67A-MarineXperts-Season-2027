// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from fake_depth2_interfaces:msg/DepthReading.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__FUNCTIONS_H_
#define FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "fake_depth2_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "fake_depth2_interfaces/msg/detail/depth_reading__struct.h"

/// Initialize msg/DepthReading message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * fake_depth2_interfaces__msg__DepthReading
 * )) before or use
 * fake_depth2_interfaces__msg__DepthReading__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__msg__DepthReading__init(fake_depth2_interfaces__msg__DepthReading * msg);

/// Finalize msg/DepthReading message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__msg__DepthReading__fini(fake_depth2_interfaces__msg__DepthReading * msg);

/// Create msg/DepthReading message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * fake_depth2_interfaces__msg__DepthReading__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
fake_depth2_interfaces__msg__DepthReading *
fake_depth2_interfaces__msg__DepthReading__create();

/// Destroy msg/DepthReading message.
/**
 * It calls
 * fake_depth2_interfaces__msg__DepthReading__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__msg__DepthReading__destroy(fake_depth2_interfaces__msg__DepthReading * msg);

/// Check for msg/DepthReading message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__msg__DepthReading__are_equal(const fake_depth2_interfaces__msg__DepthReading * lhs, const fake_depth2_interfaces__msg__DepthReading * rhs);

/// Copy a msg/DepthReading message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__msg__DepthReading__copy(
  const fake_depth2_interfaces__msg__DepthReading * input,
  fake_depth2_interfaces__msg__DepthReading * output);

/// Initialize array of msg/DepthReading messages.
/**
 * It allocates the memory for the number of elements and calls
 * fake_depth2_interfaces__msg__DepthReading__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__msg__DepthReading__Sequence__init(fake_depth2_interfaces__msg__DepthReading__Sequence * array, size_t size);

/// Finalize array of msg/DepthReading messages.
/**
 * It calls
 * fake_depth2_interfaces__msg__DepthReading__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__msg__DepthReading__Sequence__fini(fake_depth2_interfaces__msg__DepthReading__Sequence * array);

/// Create array of msg/DepthReading messages.
/**
 * It allocates the memory for the array and calls
 * fake_depth2_interfaces__msg__DepthReading__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
fake_depth2_interfaces__msg__DepthReading__Sequence *
fake_depth2_interfaces__msg__DepthReading__Sequence__create(size_t size);

/// Destroy array of msg/DepthReading messages.
/**
 * It calls
 * fake_depth2_interfaces__msg__DepthReading__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__msg__DepthReading__Sequence__destroy(fake_depth2_interfaces__msg__DepthReading__Sequence * array);

/// Check for msg/DepthReading message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__msg__DepthReading__Sequence__are_equal(const fake_depth2_interfaces__msg__DepthReading__Sequence * lhs, const fake_depth2_interfaces__msg__DepthReading__Sequence * rhs);

/// Copy an array of msg/DepthReading messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__msg__DepthReading__Sequence__copy(
  const fake_depth2_interfaces__msg__DepthReading__Sequence * input,
  fake_depth2_interfaces__msg__DepthReading__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__FUNCTIONS_H_
