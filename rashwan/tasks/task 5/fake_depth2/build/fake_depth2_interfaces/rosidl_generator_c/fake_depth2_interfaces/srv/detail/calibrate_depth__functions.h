// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from fake_depth2_interfaces:srv/CalibrateDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__FUNCTIONS_H_
#define FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "fake_depth2_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "fake_depth2_interfaces/srv/detail/calibrate_depth__struct.h"

/// Initialize srv/CalibrateDepth message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * fake_depth2_interfaces__srv__CalibrateDepth_Request
 * )) before or use
 * fake_depth2_interfaces__srv__CalibrateDepth_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__init(fake_depth2_interfaces__srv__CalibrateDepth_Request * msg);

/// Finalize srv/CalibrateDepth message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__srv__CalibrateDepth_Request__fini(fake_depth2_interfaces__srv__CalibrateDepth_Request * msg);

/// Create srv/CalibrateDepth message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
fake_depth2_interfaces__srv__CalibrateDepth_Request *
fake_depth2_interfaces__srv__CalibrateDepth_Request__create();

/// Destroy srv/CalibrateDepth message.
/**
 * It calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__srv__CalibrateDepth_Request__destroy(fake_depth2_interfaces__srv__CalibrateDepth_Request * msg);

/// Check for srv/CalibrateDepth message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__are_equal(const fake_depth2_interfaces__srv__CalibrateDepth_Request * lhs, const fake_depth2_interfaces__srv__CalibrateDepth_Request * rhs);

/// Copy a srv/CalibrateDepth message.
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
fake_depth2_interfaces__srv__CalibrateDepth_Request__copy(
  const fake_depth2_interfaces__srv__CalibrateDepth_Request * input,
  fake_depth2_interfaces__srv__CalibrateDepth_Request * output);

/// Initialize array of srv/CalibrateDepth messages.
/**
 * It allocates the memory for the number of elements and calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__init(fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * array, size_t size);

/// Finalize array of srv/CalibrateDepth messages.
/**
 * It calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__fini(fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * array);

/// Create array of srv/CalibrateDepth messages.
/**
 * It allocates the memory for the array and calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence *
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__create(size_t size);

/// Destroy array of srv/CalibrateDepth messages.
/**
 * It calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__destroy(fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * array);

/// Check for srv/CalibrateDepth message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__are_equal(const fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * lhs, const fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * rhs);

/// Copy an array of srv/CalibrateDepth messages.
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
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__copy(
  const fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * input,
  fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * output);

/// Initialize srv/CalibrateDepth message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * fake_depth2_interfaces__srv__CalibrateDepth_Response
 * )) before or use
 * fake_depth2_interfaces__srv__CalibrateDepth_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__init(fake_depth2_interfaces__srv__CalibrateDepth_Response * msg);

/// Finalize srv/CalibrateDepth message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__srv__CalibrateDepth_Response__fini(fake_depth2_interfaces__srv__CalibrateDepth_Response * msg);

/// Create srv/CalibrateDepth message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
fake_depth2_interfaces__srv__CalibrateDepth_Response *
fake_depth2_interfaces__srv__CalibrateDepth_Response__create();

/// Destroy srv/CalibrateDepth message.
/**
 * It calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__srv__CalibrateDepth_Response__destroy(fake_depth2_interfaces__srv__CalibrateDepth_Response * msg);

/// Check for srv/CalibrateDepth message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__are_equal(const fake_depth2_interfaces__srv__CalibrateDepth_Response * lhs, const fake_depth2_interfaces__srv__CalibrateDepth_Response * rhs);

/// Copy a srv/CalibrateDepth message.
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
fake_depth2_interfaces__srv__CalibrateDepth_Response__copy(
  const fake_depth2_interfaces__srv__CalibrateDepth_Response * input,
  fake_depth2_interfaces__srv__CalibrateDepth_Response * output);

/// Initialize array of srv/CalibrateDepth messages.
/**
 * It allocates the memory for the number of elements and calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__init(fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * array, size_t size);

/// Finalize array of srv/CalibrateDepth messages.
/**
 * It calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__fini(fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * array);

/// Create array of srv/CalibrateDepth messages.
/**
 * It allocates the memory for the array and calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence *
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__create(size_t size);

/// Destroy array of srv/CalibrateDepth messages.
/**
 * It calls
 * fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
void
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__destroy(fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * array);

/// Check for srv/CalibrateDepth message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fake_depth2_interfaces
bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__are_equal(const fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * lhs, const fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * rhs);

/// Copy an array of srv/CalibrateDepth messages.
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
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__copy(
  const fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * input,
  fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__FUNCTIONS_H_
