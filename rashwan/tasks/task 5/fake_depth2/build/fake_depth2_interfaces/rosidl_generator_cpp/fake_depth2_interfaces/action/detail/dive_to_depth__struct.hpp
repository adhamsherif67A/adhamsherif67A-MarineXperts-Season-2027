// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fake_depth2_interfaces:action/DiveToDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__STRUCT_HPP_
#define FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Goal __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Goal __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct DiveToDepth_Goal_
{
  using Type = DiveToDepth_Goal_<ContainerAllocator>;

  explicit DiveToDepth_Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_depth = 0.0f;
      this->dive_rate = 0.0f;
    }
  }

  explicit DiveToDepth_Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_depth = 0.0f;
      this->dive_rate = 0.0f;
    }
  }

  // field types and members
  using _target_depth_type =
    float;
  _target_depth_type target_depth;
  using _dive_rate_type =
    float;
  _dive_rate_type dive_rate;

  // setters for named parameter idiom
  Type & set__target_depth(
    const float & _arg)
  {
    this->target_depth = _arg;
    return *this;
  }
  Type & set__dive_rate(
    const float & _arg)
  {
    this->dive_rate = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Goal
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Goal
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DiveToDepth_Goal_ & other) const
  {
    if (this->target_depth != other.target_depth) {
      return false;
    }
    if (this->dive_rate != other.dive_rate) {
      return false;
    }
    return true;
  }
  bool operator!=(const DiveToDepth_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DiveToDepth_Goal_

// alias to use template instance with default allocator
using DiveToDepth_Goal =
  fake_depth2_interfaces::action::DiveToDepth_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace fake_depth2_interfaces


#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Result __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Result __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct DiveToDepth_Result_
{
  using Type = DiveToDepth_Result_<ContainerAllocator>;

  explicit DiveToDepth_Result_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->final_depth = 0.0f;
      this->message = "";
    }
  }

  explicit DiveToDepth_Result_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->final_depth = 0.0f;
      this->message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _final_depth_type =
    float;
  _final_depth_type final_depth;
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
  Type & set__final_depth(
    const float & _arg)
  {
    this->final_depth = _arg;
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
    fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Result
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Result
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DiveToDepth_Result_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->final_depth != other.final_depth) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const DiveToDepth_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DiveToDepth_Result_

// alias to use template instance with default allocator
using DiveToDepth_Result =
  fake_depth2_interfaces::action::DiveToDepth_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace fake_depth2_interfaces


#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Feedback __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct DiveToDepth_Feedback_
{
  using Type = DiveToDepth_Feedback_<ContainerAllocator>;

  explicit DiveToDepth_Feedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->current_depth = 0.0f;
      this->remaining_distance = 0.0f;
      this->percent_complete = 0.0f;
    }
  }

  explicit DiveToDepth_Feedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->current_depth = 0.0f;
      this->remaining_distance = 0.0f;
      this->percent_complete = 0.0f;
    }
  }

  // field types and members
  using _current_depth_type =
    float;
  _current_depth_type current_depth;
  using _remaining_distance_type =
    float;
  _remaining_distance_type remaining_distance;
  using _percent_complete_type =
    float;
  _percent_complete_type percent_complete;

  // setters for named parameter idiom
  Type & set__current_depth(
    const float & _arg)
  {
    this->current_depth = _arg;
    return *this;
  }
  Type & set__remaining_distance(
    const float & _arg)
  {
    this->remaining_distance = _arg;
    return *this;
  }
  Type & set__percent_complete(
    const float & _arg)
  {
    this->percent_complete = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Feedback
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_Feedback
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DiveToDepth_Feedback_ & other) const
  {
    if (this->current_depth != other.current_depth) {
      return false;
    }
    if (this->remaining_distance != other.remaining_distance) {
      return false;
    }
    if (this->percent_complete != other.percent_complete) {
      return false;
    }
    return true;
  }
  bool operator!=(const DiveToDepth_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DiveToDepth_Feedback_

// alias to use template instance with default allocator
using DiveToDepth_Feedback =
  fake_depth2_interfaces::action::DiveToDepth_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace fake_depth2_interfaces


// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'goal'
#include "fake_depth2_interfaces/action/detail/dive_to_depth__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct DiveToDepth_SendGoal_Request_
{
  using Type = DiveToDepth_SendGoal_Request_<ContainerAllocator>;

  explicit DiveToDepth_SendGoal_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit DiveToDepth_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const fake_depth2_interfaces::action::DiveToDepth_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DiveToDepth_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const DiveToDepth_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DiveToDepth_SendGoal_Request_

// alias to use template instance with default allocator
using DiveToDepth_SendGoal_Request =
  fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace fake_depth2_interfaces


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct DiveToDepth_SendGoal_Response_
{
  using Type = DiveToDepth_SendGoal_Response_<ContainerAllocator>;

  explicit DiveToDepth_SendGoal_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit DiveToDepth_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DiveToDepth_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const DiveToDepth_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DiveToDepth_SendGoal_Response_

// alias to use template instance with default allocator
using DiveToDepth_SendGoal_Response =
  fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace fake_depth2_interfaces
{

namespace action
{

struct DiveToDepth_SendGoal
{
  using Request = fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request;
  using Response = fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response;
};

}  // namespace action

}  // namespace fake_depth2_interfaces


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_GetResult_Request __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct DiveToDepth_GetResult_Request_
{
  using Type = DiveToDepth_GetResult_Request_<ContainerAllocator>;

  explicit DiveToDepth_GetResult_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit DiveToDepth_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_GetResult_Request
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_GetResult_Request
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DiveToDepth_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const DiveToDepth_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DiveToDepth_GetResult_Request_

// alias to use template instance with default allocator
using DiveToDepth_GetResult_Request =
  fake_depth2_interfaces::action::DiveToDepth_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace fake_depth2_interfaces


// Include directives for member types
// Member 'result'
// already included above
// #include "fake_depth2_interfaces/action/detail/dive_to_depth__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_GetResult_Response __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct DiveToDepth_GetResult_Response_
{
  using Type = DiveToDepth_GetResult_Response_<ContainerAllocator>;

  explicit DiveToDepth_GetResult_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit DiveToDepth_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const fake_depth2_interfaces::action::DiveToDepth_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_GetResult_Response
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_GetResult_Response
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DiveToDepth_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const DiveToDepth_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DiveToDepth_GetResult_Response_

// alias to use template instance with default allocator
using DiveToDepth_GetResult_Response =
  fake_depth2_interfaces::action::DiveToDepth_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace fake_depth2_interfaces

namespace fake_depth2_interfaces
{

namespace action
{

struct DiveToDepth_GetResult
{
  using Request = fake_depth2_interfaces::action::DiveToDepth_GetResult_Request;
  using Response = fake_depth2_interfaces::action::DiveToDepth_GetResult_Response;
};

}  // namespace action

}  // namespace fake_depth2_interfaces


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "fake_depth2_interfaces/action/detail/dive_to_depth__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage __declspec(deprecated)
#endif

namespace fake_depth2_interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct DiveToDepth_FeedbackMessage_
{
  using Type = DiveToDepth_FeedbackMessage_<ContainerAllocator>;

  explicit DiveToDepth_FeedbackMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit DiveToDepth_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const fake_depth2_interfaces::action::DiveToDepth_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage
    std::shared_ptr<fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DiveToDepth_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const DiveToDepth_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DiveToDepth_FeedbackMessage_

// alias to use template instance with default allocator
using DiveToDepth_FeedbackMessage =
  fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace fake_depth2_interfaces

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace fake_depth2_interfaces
{

namespace action
{

struct DiveToDepth
{
  /// The goal message defined in the action definition.
  using Goal = fake_depth2_interfaces::action::DiveToDepth_Goal;
  /// The result message defined in the action definition.
  using Result = fake_depth2_interfaces::action::DiveToDepth_Result;
  /// The feedback message defined in the action definition.
  using Feedback = fake_depth2_interfaces::action::DiveToDepth_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = fake_depth2_interfaces::action::DiveToDepth_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = fake_depth2_interfaces::action::DiveToDepth_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct DiveToDepth DiveToDepth;

}  // namespace action

}  // namespace fake_depth2_interfaces

#endif  // FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__STRUCT_HPP_
