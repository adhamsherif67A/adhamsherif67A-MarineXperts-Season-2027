// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from depth_interfaces:srv/Calibrate.idl
// generated code does not contain a copyright notice

#ifndef DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__STRUCT_HPP_
#define DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__depth_interfaces__srv__Calibrate_Request __attribute__((deprecated))
#else
# define DEPRECATED__depth_interfaces__srv__Calibrate_Request __declspec(deprecated)
#endif

namespace depth_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Calibrate_Request_
{
  using Type = Calibrate_Request_<ContainerAllocator>;

  explicit Calibrate_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->zero_offset = 0.0f;
    }
  }

  explicit Calibrate_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->zero_offset = 0.0f;
    }
  }

  // field types and members
  using _zero_offset_type =
    float;
  _zero_offset_type zero_offset;

  // setters for named parameter idiom
  Type & set__zero_offset(
    const float & _arg)
  {
    this->zero_offset = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    depth_interfaces::srv::Calibrate_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const depth_interfaces::srv::Calibrate_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<depth_interfaces::srv::Calibrate_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<depth_interfaces::srv::Calibrate_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      depth_interfaces::srv::Calibrate_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<depth_interfaces::srv::Calibrate_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      depth_interfaces::srv::Calibrate_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<depth_interfaces::srv::Calibrate_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<depth_interfaces::srv::Calibrate_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<depth_interfaces::srv::Calibrate_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__depth_interfaces__srv__Calibrate_Request
    std::shared_ptr<depth_interfaces::srv::Calibrate_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__depth_interfaces__srv__Calibrate_Request
    std::shared_ptr<depth_interfaces::srv::Calibrate_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Calibrate_Request_ & other) const
  {
    if (this->zero_offset != other.zero_offset) {
      return false;
    }
    return true;
  }
  bool operator!=(const Calibrate_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Calibrate_Request_

// alias to use template instance with default allocator
using Calibrate_Request =
  depth_interfaces::srv::Calibrate_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace depth_interfaces


#ifndef _WIN32
# define DEPRECATED__depth_interfaces__srv__Calibrate_Response __attribute__((deprecated))
#else
# define DEPRECATED__depth_interfaces__srv__Calibrate_Response __declspec(deprecated)
#endif

namespace depth_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Calibrate_Response_
{
  using Type = Calibrate_Response_<ContainerAllocator>;

  explicit Calibrate_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  explicit Calibrate_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

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

  // constant declarations

  // pointer types
  using RawPtr =
    depth_interfaces::srv::Calibrate_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const depth_interfaces::srv::Calibrate_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<depth_interfaces::srv::Calibrate_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<depth_interfaces::srv::Calibrate_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      depth_interfaces::srv::Calibrate_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<depth_interfaces::srv::Calibrate_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      depth_interfaces::srv::Calibrate_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<depth_interfaces::srv::Calibrate_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<depth_interfaces::srv::Calibrate_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<depth_interfaces::srv::Calibrate_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__depth_interfaces__srv__Calibrate_Response
    std::shared_ptr<depth_interfaces::srv::Calibrate_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__depth_interfaces__srv__Calibrate_Response
    std::shared_ptr<depth_interfaces::srv::Calibrate_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Calibrate_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const Calibrate_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Calibrate_Response_

// alias to use template instance with default allocator
using Calibrate_Response =
  depth_interfaces::srv::Calibrate_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace depth_interfaces

namespace depth_interfaces
{

namespace srv
{

struct Calibrate
{
  using Request = depth_interfaces::srv::Calibrate_Request;
  using Response = depth_interfaces::srv::Calibrate_Response;
};

}  // namespace srv

}  // namespace depth_interfaces

#endif  // DEPTH_INTERFACES__SRV__DETAIL__CALIBRATE__STRUCT_HPP_
