// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fake_depth2_interfaces:srv/CalibrateDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__STRUCT_HPP_
#define FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__srv__CalibrateDepth_Request __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__srv__CalibrateDepth_Request __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct CalibrateDepth_Request_
{
  using Type = CalibrateDepth_Request_<ContainerAllocator>;

  explicit CalibrateDepth_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reset_to_zero = false;
      this->requested_offset = 0.0f;
    }
  }

  explicit CalibrateDepth_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reset_to_zero = false;
      this->requested_offset = 0.0f;
    }
  }

  // field types and members
  using _reset_to_zero_type =
    bool;
  _reset_to_zero_type reset_to_zero;
  using _requested_offset_type =
    float;
  _requested_offset_type requested_offset;

  // setters for named parameter idiom
  Type & set__reset_to_zero(
    const bool & _arg)
  {
    this->reset_to_zero = _arg;
    return *this;
  }
  Type & set__requested_offset(
    const float & _arg)
  {
    this->requested_offset = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__srv__CalibrateDepth_Request
    std::shared_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__srv__CalibrateDepth_Request
    std::shared_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CalibrateDepth_Request_ & other) const
  {
    if (this->reset_to_zero != other.reset_to_zero) {
      return false;
    }
    if (this->requested_offset != other.requested_offset) {
      return false;
    }
    return true;
  }
  bool operator!=(const CalibrateDepth_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CalibrateDepth_Request_

// alias to use template instance with default allocator
using CalibrateDepth_Request =
  fake_depth2_interfaces::srv::CalibrateDepth_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace fake_depth2_interfaces


#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__srv__CalibrateDepth_Response __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__srv__CalibrateDepth_Response __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct CalibrateDepth_Response_
{
  using Type = CalibrateDepth_Response_<ContainerAllocator>;

  explicit CalibrateDepth_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
      this->applied_offset = 0.0f;
    }
  }

  explicit CalibrateDepth_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
      this->applied_offset = 0.0f;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;
  using _applied_offset_type =
    float;
  _applied_offset_type applied_offset;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }
  Type & set__applied_offset(
    const float & _arg)
  {
    this->applied_offset = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__srv__CalibrateDepth_Response
    std::shared_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__srv__CalibrateDepth_Response
    std::shared_ptr<fake_depth2_interfaces::srv::CalibrateDepth_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CalibrateDepth_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    if (this->applied_offset != other.applied_offset) {
      return false;
    }
    return true;
  }
  bool operator!=(const CalibrateDepth_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CalibrateDepth_Response_

// alias to use template instance with default allocator
using CalibrateDepth_Response =
  fake_depth2_interfaces::srv::CalibrateDepth_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace fake_depth2_interfaces

namespace fake_depth2_interfaces
{

namespace srv
{

struct CalibrateDepth
{
  using Request = fake_depth2_interfaces::srv::CalibrateDepth_Request;
  using Response = fake_depth2_interfaces::srv::CalibrateDepth_Response;
};

}  // namespace srv

}  // namespace fake_depth2_interfaces

#endif  // FAKE_DEPTH2_INTERFACES__SRV__DETAIL__CALIBRATE_DEPTH__STRUCT_HPP_
