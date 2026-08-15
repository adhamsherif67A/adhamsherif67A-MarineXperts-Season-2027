// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fake_depth2_interfaces:msg/DepthReading.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__STRUCT_HPP_
#define FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__msg__DepthReading __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__msg__DepthReading __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DepthReading_
{
  using Type = DepthReading_<ContainerAllocator>;

  explicit DepthReading_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->depth = 0.0f;
      this->zero_offset = 0.0f;
      this->threshold_crossed = false;
    }
  }

  explicit DepthReading_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->depth = 0.0f;
      this->zero_offset = 0.0f;
      this->threshold_crossed = false;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _depth_type =
    float;
  _depth_type depth;
  using _zero_offset_type =
    float;
  _zero_offset_type zero_offset;
  using _threshold_crossed_type =
    bool;
  _threshold_crossed_type threshold_crossed;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__depth(
    const float & _arg)
  {
    this->depth = _arg;
    return *this;
  }
  Type & set__zero_offset(
    const float & _arg)
  {
    this->zero_offset = _arg;
    return *this;
  }
  Type & set__threshold_crossed(
    const bool & _arg)
  {
    this->threshold_crossed = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__msg__DepthReading
    std::shared_ptr<fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__msg__DepthReading
    std::shared_ptr<fake_depth2_interfaces::msg::DepthReading_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DepthReading_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->depth != other.depth) {
      return false;
    }
    if (this->zero_offset != other.zero_offset) {
      return false;
    }
    if (this->threshold_crossed != other.threshold_crossed) {
      return false;
    }
    return true;
  }
  bool operator!=(const DepthReading_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DepthReading_

// alias to use template instance with default allocator
using DepthReading =
  fake_depth2_interfaces::msg::DepthReading_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace fake_depth2_interfaces

#endif  // FAKE_DEPTH2_INTERFACES__MSG__DETAIL__DEPTH_READING__STRUCT_HPP_
