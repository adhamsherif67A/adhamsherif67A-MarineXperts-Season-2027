
#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to fake_depth2_interfaces__action__DiveToDepth_Goal

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_Goal {
    /// Target depth in meters (positive = deeper).
    pub target_depth: f32,

    /// Rate at which simulated depth approaches the target, in meters/second.
    /// If <= 0.0, the server falls back to its default dive rate parameter.
    pub dive_rate: f32,

}



impl Default for DiveToDepth_Goal {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::action::rmw::DiveToDepth_Goal::default())
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_Goal {
  type RmwMsg = super::action::rmw::DiveToDepth_Goal;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        target_depth: msg.target_depth,
        dive_rate: msg.dive_rate,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      target_depth: msg.target_depth,
      dive_rate: msg.dive_rate,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      target_depth: msg.target_depth,
      dive_rate: msg.dive_rate,
    }
  }
}


// Corresponds to fake_depth2_interfaces__action__DiveToDepth_Result

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_Result {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub final_depth: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: std::string::String,

}



impl Default for DiveToDepth_Result {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::action::rmw::DiveToDepth_Result::default())
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_Result {
  type RmwMsg = super::action::rmw::DiveToDepth_Result;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
        final_depth: msg.final_depth,
        message: msg.message.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
      final_depth: msg.final_depth,
        message: msg.message.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
      final_depth: msg.final_depth,
      message: msg.message.to_string(),
    }
  }
}


// Corresponds to fake_depth2_interfaces__action__DiveToDepth_Feedback

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_Feedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub current_depth: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub remaining_distance: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub percent_complete: f32,

}



impl Default for DiveToDepth_Feedback {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::action::rmw::DiveToDepth_Feedback::default())
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_Feedback {
  type RmwMsg = super::action::rmw::DiveToDepth_Feedback;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        current_depth: msg.current_depth,
        remaining_distance: msg.remaining_distance,
        percent_complete: msg.percent_complete,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      current_depth: msg.current_depth,
      remaining_distance: msg.remaining_distance,
      percent_complete: msg.percent_complete,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      current_depth: msg.current_depth,
      remaining_distance: msg.remaining_distance,
      percent_complete: msg.percent_complete,
    }
  }
}


// Corresponds to fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::action::DiveToDepth_Feedback,

}



impl Default for DiveToDepth_FeedbackMessage {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::action::rmw::DiveToDepth_FeedbackMessage::default())
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_FeedbackMessage {
  type RmwMsg = super::action::rmw::DiveToDepth_FeedbackMessage;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        goal_id: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Owned(msg.goal_id)).into_owned(),
        feedback: super::action::DiveToDepth_Feedback::into_rmw_message(std::borrow::Cow::Owned(msg.feedback)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        goal_id: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Borrowed(&msg.goal_id)).into_owned(),
        feedback: super::action::DiveToDepth_Feedback::into_rmw_message(std::borrow::Cow::Borrowed(&msg.feedback)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      goal_id: unique_identifier_msgs::msg::UUID::from_rmw_message(msg.goal_id),
      feedback: super::action::DiveToDepth_Feedback::from_rmw_message(msg.feedback),
    }
  }
}






// Corresponds to fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::action::DiveToDepth_Goal,

}



impl Default for DiveToDepth_SendGoal_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::action::rmw::DiveToDepth_SendGoal_Request::default())
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_SendGoal_Request {
  type RmwMsg = super::action::rmw::DiveToDepth_SendGoal_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        goal_id: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Owned(msg.goal_id)).into_owned(),
        goal: super::action::DiveToDepth_Goal::into_rmw_message(std::borrow::Cow::Owned(msg.goal)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        goal_id: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Borrowed(&msg.goal_id)).into_owned(),
        goal: super::action::DiveToDepth_Goal::into_rmw_message(std::borrow::Cow::Borrowed(&msg.goal)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      goal_id: unique_identifier_msgs::msg::UUID::from_rmw_message(msg.goal_id),
      goal: super::action::DiveToDepth_Goal::from_rmw_message(msg.goal),
    }
  }
}


// Corresponds to fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::Time,

}



impl Default for DiveToDepth_SendGoal_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::action::rmw::DiveToDepth_SendGoal_Response::default())
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_SendGoal_Response {
  type RmwMsg = super::action::rmw::DiveToDepth_SendGoal_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        accepted: msg.accepted,
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.stamp)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      accepted: msg.accepted,
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.stamp)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      accepted: msg.accepted,
      stamp: builtin_interfaces::msg::Time::from_rmw_message(msg.stamp),
    }
  }
}


// Corresponds to fake_depth2_interfaces__action__DiveToDepth_GetResult_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::UUID,

}



impl Default for DiveToDepth_GetResult_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::action::rmw::DiveToDepth_GetResult_Request::default())
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_GetResult_Request {
  type RmwMsg = super::action::rmw::DiveToDepth_GetResult_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        goal_id: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Owned(msg.goal_id)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        goal_id: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Borrowed(&msg.goal_id)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      goal_id: unique_identifier_msgs::msg::UUID::from_rmw_message(msg.goal_id),
    }
  }
}


// Corresponds to fake_depth2_interfaces__action__DiveToDepth_GetResult_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::action::DiveToDepth_Result,

}



impl Default for DiveToDepth_GetResult_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::action::rmw::DiveToDepth_GetResult_Response::default())
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_GetResult_Response {
  type RmwMsg = super::action::rmw::DiveToDepth_GetResult_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        status: msg.status,
        result: super::action::DiveToDepth_Result::into_rmw_message(std::borrow::Cow::Owned(msg.result)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      status: msg.status,
        result: super::action::DiveToDepth_Result::into_rmw_message(std::borrow::Cow::Borrowed(&msg.result)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      status: msg.status,
      result: super::action::DiveToDepth_Result::from_rmw_message(msg.result),
    }
  }
}






#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct DiveToDepth_SendGoal;

impl rosidl_runtime_rs::Service for DiveToDepth_SendGoal {
    type Request = DiveToDepth_SendGoal_Request;
    type Response = DiveToDepth_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_SendGoal() }
    }
}




#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct DiveToDepth_GetResult;

impl rosidl_runtime_rs::Service for DiveToDepth_GetResult {
    type Request = DiveToDepth_GetResult_Request;
    type Response = DiveToDepth_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_GetResult() }
    }
}






#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_action_type_support_handle__fake_depth2_interfaces__action__DiveToDepth() -> *const std::ffi::c_void;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth
#[allow(missing_docs, non_camel_case_types)]
pub struct DiveToDepth;

impl rosidl_runtime_rs::Action for DiveToDepth {
  // --- Associated types for client library users ---
  /// The goal message defined in the action definition.
  type Goal = DiveToDepth_Goal;

  /// The result message defined in the action definition.
  type Result = DiveToDepth_Result;

  /// The feedback message defined in the action definition.
  type Feedback = DiveToDepth_Feedback;

  // --- Associated types for client library implementation ---
  /// The feedback message with generic fields which wraps the feedback message.
  type FeedbackMessage = super::action::DiveToDepth_FeedbackMessage;

  /// The send_goal service using a wrapped version of the goal message as a request.
  type SendGoalService = super::action::DiveToDepth_SendGoal;

  /// The generic service to cancel a goal.
  type CancelGoalService = action_msgs::srv::rmw::CancelGoal;

  /// The get_result service using a wrapped version of the result message as a response.
  type GetResultService = super::action::DiveToDepth_GetResult;

  // --- Methods for client library implementation ---
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_action_type_support_handle__fake_depth2_interfaces__action__DiveToDepth() }
  }

  fn create_goal_request(
    goal_id: &[u8; 16],
    goal: super::action::rmw::DiveToDepth_Goal,
  ) -> super::action::rmw::DiveToDepth_SendGoal_Request {
   super::action::rmw::DiveToDepth_SendGoal_Request {
      goal_id: unique_identifier_msgs::msg::rmw::UUID { uuid: *goal_id },
      goal,
    }
  }

  fn split_goal_request(
    request: super::action::rmw::DiveToDepth_SendGoal_Request,
  ) -> (
    [u8; 16],
   super::action::rmw::DiveToDepth_Goal,
  ) {
    (request.goal_id.uuid, request.goal)
  }

  fn create_goal_response(
    accepted: bool,
    stamp: (i32, u32),
  ) -> super::action::rmw::DiveToDepth_SendGoal_Response {
   super::action::rmw::DiveToDepth_SendGoal_Response {
      accepted,
      stamp: builtin_interfaces::msg::rmw::Time {
        sec: stamp.0,
        nanosec: stamp.1,
      },
    }
  }

  fn get_goal_response_accepted(
    response: &super::action::rmw::DiveToDepth_SendGoal_Response,
  ) -> bool {
    response.accepted
  }

  fn get_goal_response_stamp(
    response: &super::action::rmw::DiveToDepth_SendGoal_Response,
  ) -> (i32, u32) {
    (response.stamp.sec, response.stamp.nanosec)
  }

  fn create_feedback_message(
    goal_id: &[u8; 16],
    feedback: super::action::rmw::DiveToDepth_Feedback,
  ) -> super::action::rmw::DiveToDepth_FeedbackMessage {
    let mut message = super::action::rmw::DiveToDepth_FeedbackMessage::default();
    message.goal_id.uuid = *goal_id;
    message.feedback = feedback;
    message
  }

  fn split_feedback_message(
    feedback: super::action::rmw::DiveToDepth_FeedbackMessage,
  ) -> (
    [u8; 16],
   super::action::rmw::DiveToDepth_Feedback,
  ) {
    (feedback.goal_id.uuid, feedback.feedback)
  }

  fn create_result_request(
    goal_id: &[u8; 16],
  ) -> super::action::rmw::DiveToDepth_GetResult_Request {
   super::action::rmw::DiveToDepth_GetResult_Request {
      goal_id: unique_identifier_msgs::msg::rmw::UUID { uuid: *goal_id },
    }
  }

  fn get_result_request_uuid(
    request: &super::action::rmw::DiveToDepth_GetResult_Request,
  ) -> &[u8; 16] {
    &request.goal_id.uuid
  }

  fn create_result_response(
    status: i8,
    result: super::action::rmw::DiveToDepth_Result,
  ) -> super::action::rmw::DiveToDepth_GetResult_Response {
   super::action::rmw::DiveToDepth_GetResult_Response {
      status,
      result,
    }
  }

  fn split_result_response(
    response: super::action::rmw::DiveToDepth_GetResult_Response
  ) -> (
    i8,
   super::action::rmw::DiveToDepth_Result,
  ) {
    (response.status, response.result)
  }
}


