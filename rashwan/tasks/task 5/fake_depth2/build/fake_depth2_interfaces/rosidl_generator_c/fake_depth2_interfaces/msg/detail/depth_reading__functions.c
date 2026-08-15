// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fake_depth2_interfaces:msg/DepthReading.idl
// generated code does not contain a copyright notice
#include "fake_depth2_interfaces/msg/detail/depth_reading__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
fake_depth2_interfaces__msg__DepthReading__init(fake_depth2_interfaces__msg__DepthReading * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    fake_depth2_interfaces__msg__DepthReading__fini(msg);
    return false;
  }
  // depth
  // zero_offset
  // threshold_crossed
  return true;
}

void
fake_depth2_interfaces__msg__DepthReading__fini(fake_depth2_interfaces__msg__DepthReading * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // depth
  // zero_offset
  // threshold_crossed
}

bool
fake_depth2_interfaces__msg__DepthReading__are_equal(const fake_depth2_interfaces__msg__DepthReading * lhs, const fake_depth2_interfaces__msg__DepthReading * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // depth
  if (lhs->depth != rhs->depth) {
    return false;
  }
  // zero_offset
  if (lhs->zero_offset != rhs->zero_offset) {
    return false;
  }
  // threshold_crossed
  if (lhs->threshold_crossed != rhs->threshold_crossed) {
    return false;
  }
  return true;
}

bool
fake_depth2_interfaces__msg__DepthReading__copy(
  const fake_depth2_interfaces__msg__DepthReading * input,
  fake_depth2_interfaces__msg__DepthReading * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // depth
  output->depth = input->depth;
  // zero_offset
  output->zero_offset = input->zero_offset;
  // threshold_crossed
  output->threshold_crossed = input->threshold_crossed;
  return true;
}

fake_depth2_interfaces__msg__DepthReading *
fake_depth2_interfaces__msg__DepthReading__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__msg__DepthReading * msg = (fake_depth2_interfaces__msg__DepthReading *)allocator.allocate(sizeof(fake_depth2_interfaces__msg__DepthReading), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fake_depth2_interfaces__msg__DepthReading));
  bool success = fake_depth2_interfaces__msg__DepthReading__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fake_depth2_interfaces__msg__DepthReading__destroy(fake_depth2_interfaces__msg__DepthReading * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fake_depth2_interfaces__msg__DepthReading__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fake_depth2_interfaces__msg__DepthReading__Sequence__init(fake_depth2_interfaces__msg__DepthReading__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__msg__DepthReading * data = NULL;

  if (size) {
    data = (fake_depth2_interfaces__msg__DepthReading *)allocator.zero_allocate(size, sizeof(fake_depth2_interfaces__msg__DepthReading), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fake_depth2_interfaces__msg__DepthReading__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fake_depth2_interfaces__msg__DepthReading__fini(&data[i - 1]);
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
fake_depth2_interfaces__msg__DepthReading__Sequence__fini(fake_depth2_interfaces__msg__DepthReading__Sequence * array)
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
      fake_depth2_interfaces__msg__DepthReading__fini(&array->data[i]);
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

fake_depth2_interfaces__msg__DepthReading__Sequence *
fake_depth2_interfaces__msg__DepthReading__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fake_depth2_interfaces__msg__DepthReading__Sequence * array = (fake_depth2_interfaces__msg__DepthReading__Sequence *)allocator.allocate(sizeof(fake_depth2_interfaces__msg__DepthReading__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fake_depth2_interfaces__msg__DepthReading__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fake_depth2_interfaces__msg__DepthReading__Sequence__destroy(fake_depth2_interfaces__msg__DepthReading__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fake_depth2_interfaces__msg__DepthReading__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fake_depth2_interfaces__msg__DepthReading__Sequence__are_equal(const fake_depth2_interfaces__msg__DepthReading__Sequence * lhs, const fake_depth2_interfaces__msg__DepthReading__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fake_depth2_interfaces__msg__DepthReading__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fake_depth2_interfaces__msg__DepthReading__Sequence__copy(
  const fake_depth2_interfaces__msg__DepthReading__Sequence * input,
  fake_depth2_interfaces__msg__DepthReading__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fake_depth2_interfaces__msg__DepthReading);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fake_depth2_interfaces__msg__DepthReading * data =
      (fake_depth2_interfaces__msg__DepthReading *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fake_depth2_interfaces__msg__DepthReading__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fake_depth2_interfaces__msg__DepthReading__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fake_depth2_interfaces__msg__DepthReading__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
