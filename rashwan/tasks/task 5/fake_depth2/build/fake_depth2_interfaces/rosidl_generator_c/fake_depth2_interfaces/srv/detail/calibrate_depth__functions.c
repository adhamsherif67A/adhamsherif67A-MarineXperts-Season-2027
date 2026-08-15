// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fake_depth2_interfaces:srv/CalibrateDepth.idl
// generated code does not contain a copyright notice
#include "fake_depth2_interfaces/srv/detail/calibrate_depth__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__init(fake_depth2_interfaces__srv__CalibrateDepth_Request * msg)
{
  if (!msg) {
    return false;
  }
  // reset_to_zero
  // requested_offset
  return true;
}

void
fake_depth2_interfaces__srv__CalibrateDepth_Request__fini(fake_depth2_interfaces__srv__CalibrateDepth_Request * msg)
{
  if (!msg) {
    return;
  }
  // reset_to_zero
  // requested_offset
}

bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__are_equal(const fake_depth2_interfaces__srv__CalibrateDepth_Request * lhs, const fake_depth2_interfaces__srv__CalibrateDepth_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // reset_to_zero
  if (lhs->reset_to_zero != rhs->reset_to_zero) {
    return false;
  }
  // requested_offset
  if (lhs->requested_offset != rhs->requested_offset) {
    return false;
  }
  return true;
}

bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__copy(
  const fake_depth2_interfaces__srv__CalibrateDepth_Request * input,
  fake_depth2_interfaces__srv__CalibrateDepth_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // reset_to_zero
  output->reset_to_zero = input->reset_to_zero;
  // requested_offset
  output->requested_offset = input->requested_offset;
  return true;
}

fake_depth2_interfaces__srv__CalibrateDepth_Request *
fake_depth2_interfaces__srv__CalibrateDepth_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__srv__CalibrateDepth_Request * msg = (fake_depth2_interfaces__srv__CalibrateDepth_Request *)allocator.allocate(sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Request));
  bool success = fake_depth2_interfaces__srv__CalibrateDepth_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fake_depth2_interfaces__srv__CalibrateDepth_Request__destroy(fake_depth2_interfaces__srv__CalibrateDepth_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fake_depth2_interfaces__srv__CalibrateDepth_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__init(fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__srv__CalibrateDepth_Request * data = NULL;

  if (size) {
    data = (fake_depth2_interfaces__srv__CalibrateDepth_Request *)allocator.zero_allocate(size, sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fake_depth2_interfaces__srv__CalibrateDepth_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fake_depth2_interfaces__srv__CalibrateDepth_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__fini(fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      fake_depth2_interfaces__srv__CalibrateDepth_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence *
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * array = (fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence *)allocator.allocate(sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__destroy(fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__are_equal(const fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * lhs, const fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fake_depth2_interfaces__srv__CalibrateDepth_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__copy(
  const fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * input,
  fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fake_depth2_interfaces__srv__CalibrateDepth_Request * data =
      (fake_depth2_interfaces__srv__CalibrateDepth_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fake_depth2_interfaces__srv__CalibrateDepth_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fake_depth2_interfaces__srv__CalibrateDepth_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fake_depth2_interfaces__srv__CalibrateDepth_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__init(fake_depth2_interfaces__srv__CalibrateDepth_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    fake_depth2_interfaces__srv__CalibrateDepth_Response__fini(msg);
    return false;
  }
  // applied_offset
  return true;
}

void
fake_depth2_interfaces__srv__CalibrateDepth_Response__fini(fake_depth2_interfaces__srv__CalibrateDepth_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // message
  rosidl_runtime_c__String__fini(&msg->message);
  // applied_offset
}

bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__are_equal(const fake_depth2_interfaces__srv__CalibrateDepth_Response * lhs, const fake_depth2_interfaces__srv__CalibrateDepth_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message), &(rhs->message)))
  {
    return false;
  }
  // applied_offset
  if (lhs->applied_offset != rhs->applied_offset) {
    return false;
  }
  return true;
}

bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__copy(
  const fake_depth2_interfaces__srv__CalibrateDepth_Response * input,
  fake_depth2_interfaces__srv__CalibrateDepth_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // message
  if (!rosidl_runtime_c__String__copy(
      &(input->message), &(output->message)))
  {
    return false;
  }
  // applied_offset
  output->applied_offset = input->applied_offset;
  return true;
}

fake_depth2_interfaces__srv__CalibrateDepth_Response *
fake_depth2_interfaces__srv__CalibrateDepth_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__srv__CalibrateDepth_Response * msg = (fake_depth2_interfaces__srv__CalibrateDepth_Response *)allocator.allocate(sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Response));
  bool success = fake_depth2_interfaces__srv__CalibrateDepth_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fake_depth2_interfaces__srv__CalibrateDepth_Response__destroy(fake_depth2_interfaces__srv__CalibrateDepth_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fake_depth2_interfaces__srv__CalibrateDepth_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__init(fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__srv__CalibrateDepth_Response * data = NULL;

  if (size) {
    data = (fake_depth2_interfaces__srv__CalibrateDepth_Response *)allocator.zero_allocate(size, sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fake_depth2_interfaces__srv__CalibrateDepth_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fake_depth2_interfaces__srv__CalibrateDepth_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__fini(fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      fake_depth2_interfaces__srv__CalibrateDepth_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence *
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * array = (fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence *)allocator.allocate(sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__destroy(fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__are_equal(const fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * lhs, const fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fake_depth2_interfaces__srv__CalibrateDepth_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__copy(
  const fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * input,
  fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fake_depth2_interfaces__srv__CalibrateDepth_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fake_depth2_interfaces__srv__CalibrateDepth_Response * data =
      (fake_depth2_interfaces__srv__CalibrateDepth_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fake_depth2_interfaces__srv__CalibrateDepth_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fake_depth2_interfaces__srv__CalibrateDepth_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fake_depth2_interfaces__srv__CalibrateDepth_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
