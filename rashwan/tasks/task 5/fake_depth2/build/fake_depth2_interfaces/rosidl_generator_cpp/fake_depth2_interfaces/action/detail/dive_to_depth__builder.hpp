// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fake_depth2_interfaces:action/DiveToDepth.idl
// generated code does not contain a copyright notice

#ifndef FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__BUILDER_HPP_
#define FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fake_depth2_interfaces/action/detail/dive_to_depth__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fake_depth2_interfaces
{

namespace action
{

namespace builder
{

class Init_DiveToDepth_Goal_dive_rate
{
public:
  explicit Init_DiveToDepth_Goal_dive_rate(::fake_depth2_interfaces::action::DiveToDepth_Goal & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::action::DiveToDepth_Goal dive_rate(::fake_depth2_interfaces::action::DiveToDepth_Goal::_dive_rate_type arg)
  {
    msg_.dive_rate = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_Goal msg_;
};

class Init_DiveToDepth_Goal_target_depth
{
public:
  Init_DiveToDepth_Goal_target_depth()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DiveToDepth_Goal_dive_rate target_depth(::fake_depth2_interfaces::action::DiveToDepth_Goal::_target_depth_type arg)
  {
    msg_.target_depth = std::move(arg);
    return Init_DiveToDepth_Goal_dive_rate(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::action::DiveToDepth_Goal>()
{
  return fake_depth2_interfaces::action::builder::Init_DiveToDepth_Goal_target_depth();
}

}  // namespace fake_depth2_interfaces


namespace fake_depth2_interfaces
{

namespace action
{

namespace builder
{

class Init_DiveToDepth_Result_message
{
public:
  explicit Init_DiveToDepth_Result_message(::fake_depth2_interfaces::action::DiveToDepth_Result & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::action::DiveToDepth_Result message(::fake_depth2_interfaces::action::DiveToDepth_Result::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_Result msg_;
};

class Init_DiveToDepth_Result_final_depth
{
public:
  explicit Init_DiveToDepth_Result_final_depth(::fake_depth2_interfaces::action::DiveToDepth_Result & msg)
  : msg_(msg)
  {}
  Init_DiveToDepth_Result_message final_depth(::fake_depth2_interfaces::action::DiveToDepth_Result::_final_depth_type arg)
  {
    msg_.final_depth = std::move(arg);
    return Init_DiveToDepth_Result_message(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_Result msg_;
};

class Init_DiveToDepth_Result_success
{
public:
  Init_DiveToDepth_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DiveToDepth_Result_final_depth success(::fake_depth2_interfaces::action::DiveToDepth_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_DiveToDepth_Result_final_depth(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::action::DiveToDepth_Result>()
{
  return fake_depth2_interfaces::action::builder::Init_DiveToDepth_Result_success();
}

}  // namespace fake_depth2_interfaces


namespace fake_depth2_interfaces
{

namespace action
{

namespace builder
{

class Init_DiveToDepth_Feedback_percent_complete
{
public:
  explicit Init_DiveToDepth_Feedback_percent_complete(::fake_depth2_interfaces::action::DiveToDepth_Feedback & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::action::DiveToDepth_Feedback percent_complete(::fake_depth2_interfaces::action::DiveToDepth_Feedback::_percent_complete_type arg)
  {
    msg_.percent_complete = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_Feedback msg_;
};

class Init_DiveToDepth_Feedback_remaining_distance
{
public:
  explicit Init_DiveToDepth_Feedback_remaining_distance(::fake_depth2_interfaces::action::DiveToDepth_Feedback & msg)
  : msg_(msg)
  {}
  Init_DiveToDepth_Feedback_percent_complete remaining_distance(::fake_depth2_interfaces::action::DiveToDepth_Feedback::_remaining_distance_type arg)
  {
    msg_.remaining_distance = std::move(arg);
    return Init_DiveToDepth_Feedback_percent_complete(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_Feedback msg_;
};

class Init_DiveToDepth_Feedback_current_depth
{
public:
  Init_DiveToDepth_Feedback_current_depth()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DiveToDepth_Feedback_remaining_distance current_depth(::fake_depth2_interfaces::action::DiveToDepth_Feedback::_current_depth_type arg)
  {
    msg_.current_depth = std::move(arg);
    return Init_DiveToDepth_Feedback_remaining_distance(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::action::DiveToDepth_Feedback>()
{
  return fake_depth2_interfaces::action::builder::Init_DiveToDepth_Feedback_current_depth();
}

}  // namespace fake_depth2_interfaces


namespace fake_depth2_interfaces
{

namespace action
{

namespace builder
{

class Init_DiveToDepth_SendGoal_Request_goal
{
public:
  explicit Init_DiveToDepth_SendGoal_Request_goal(::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request goal(::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request msg_;
};

class Init_DiveToDepth_SendGoal_Request_goal_id
{
public:
  Init_DiveToDepth_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DiveToDepth_SendGoal_Request_goal goal_id(::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_DiveToDepth_SendGoal_Request_goal(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Request>()
{
  return fake_depth2_interfaces::action::builder::Init_DiveToDepth_SendGoal_Request_goal_id();
}

}  // namespace fake_depth2_interfaces


namespace fake_depth2_interfaces
{

namespace action
{

namespace builder
{

class Init_DiveToDepth_SendGoal_Response_stamp
{
public:
  explicit Init_DiveToDepth_SendGoal_Response_stamp(::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response stamp(::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response msg_;
};

class Init_DiveToDepth_SendGoal_Response_accepted
{
public:
  Init_DiveToDepth_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DiveToDepth_SendGoal_Response_stamp accepted(::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_DiveToDepth_SendGoal_Response_stamp(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::action::DiveToDepth_SendGoal_Response>()
{
  return fake_depth2_interfaces::action::builder::Init_DiveToDepth_SendGoal_Response_accepted();
}

}  // namespace fake_depth2_interfaces


namespace fake_depth2_interfaces
{

namespace action
{

namespace builder
{

class Init_DiveToDepth_GetResult_Request_goal_id
{
public:
  Init_DiveToDepth_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fake_depth2_interfaces::action::DiveToDepth_GetResult_Request goal_id(::fake_depth2_interfaces::action::DiveToDepth_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::action::DiveToDepth_GetResult_Request>()
{
  return fake_depth2_interfaces::action::builder::Init_DiveToDepth_GetResult_Request_goal_id();
}

}  // namespace fake_depth2_interfaces


namespace fake_depth2_interfaces
{

namespace action
{

namespace builder
{

class Init_DiveToDepth_GetResult_Response_result
{
public:
  explicit Init_DiveToDepth_GetResult_Response_result(::fake_depth2_interfaces::action::DiveToDepth_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::action::DiveToDepth_GetResult_Response result(::fake_depth2_interfaces::action::DiveToDepth_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_GetResult_Response msg_;
};

class Init_DiveToDepth_GetResult_Response_status
{
public:
  Init_DiveToDepth_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DiveToDepth_GetResult_Response_result status(::fake_depth2_interfaces::action::DiveToDepth_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_DiveToDepth_GetResult_Response_result(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::action::DiveToDepth_GetResult_Response>()
{
  return fake_depth2_interfaces::action::builder::Init_DiveToDepth_GetResult_Response_status();
}

}  // namespace fake_depth2_interfaces


namespace fake_depth2_interfaces
{

namespace action
{

namespace builder
{

class Init_DiveToDepth_FeedbackMessage_feedback
{
public:
  explicit Init_DiveToDepth_FeedbackMessage_feedback(::fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage feedback(::fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage msg_;
};

class Init_DiveToDepth_FeedbackMessage_goal_id
{
public:
  Init_DiveToDepth_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DiveToDepth_FeedbackMessage_feedback goal_id(::fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_DiveToDepth_FeedbackMessage_feedback(msg_);
  }

private:
  ::fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::fake_depth2_interfaces::action::DiveToDepth_FeedbackMessage>()
{
  return fake_depth2_interfaces::action::builder::Init_DiveToDepth_FeedbackMessage_goal_id();
}

}  // namespace fake_depth2_interfaces

#endif  // FAKE_DEPTH2_INTERFACES__ACTION__DETAIL__DIVE_TO_DEPTH__BUILDER_HPP_
