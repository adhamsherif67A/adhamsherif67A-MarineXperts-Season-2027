
#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_Goal() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__action__DiveToDepth_Goal__init(msg: *mut DiveToDepth_Goal) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Goal>, size: usize) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Goal>);
    fn fake_depth2_interfaces__action__DiveToDepth_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DiveToDepth_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Goal>) -> bool;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
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
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__action__DiveToDepth_Goal__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__action__DiveToDepth_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DiveToDepth_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DiveToDepth_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/action/DiveToDepth_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_Goal() }
  }
}


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_Result() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__action__DiveToDepth_Result__init(msg: *mut DiveToDepth_Result) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Result>, size: usize) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Result>);
    fn fake_depth2_interfaces__action__DiveToDepth_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DiveToDepth_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Result>) -> bool;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
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
    pub message: rosidl_runtime_rs::String,

}



impl Default for DiveToDepth_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__action__DiveToDepth_Result__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__action__DiveToDepth_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DiveToDepth_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DiveToDepth_Result where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/action/DiveToDepth_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_Result() }
  }
}


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__action__DiveToDepth_Feedback__init(msg: *mut DiveToDepth_Feedback) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Feedback>, size: usize) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Feedback>);
    fn fake_depth2_interfaces__action__DiveToDepth_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DiveToDepth_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_Feedback>) -> bool;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
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
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__action__DiveToDepth_Feedback__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__action__DiveToDepth_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DiveToDepth_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DiveToDepth_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/action/DiveToDepth_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_Feedback() }
  }
}


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__init(msg: *mut DiveToDepth_FeedbackMessage) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_FeedbackMessage>, size: usize) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_FeedbackMessage>);
    fn fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DiveToDepth_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_FeedbackMessage>) -> bool;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::DiveToDepth_Feedback,

}



impl Default for DiveToDepth_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DiveToDepth_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DiveToDepth_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/action/DiveToDepth_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_FeedbackMessage() }
  }
}




#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__init(msg: *mut DiveToDepth_SendGoal_Request) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_SendGoal_Request>, size: usize) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_SendGoal_Request>);
    fn fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DiveToDepth_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_SendGoal_Request>) -> bool;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::DiveToDepth_Goal,

}



impl Default for DiveToDepth_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DiveToDepth_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DiveToDepth_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/action/DiveToDepth_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Request() }
  }
}


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__init(msg: *mut DiveToDepth_SendGoal_Response) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_SendGoal_Response>, size: usize) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_SendGoal_Response>);
    fn fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DiveToDepth_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_SendGoal_Response>) -> bool;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for DiveToDepth_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DiveToDepth_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DiveToDepth_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/action/DiveToDepth_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_SendGoal_Response() }
  }
}


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__init(msg: *mut DiveToDepth_GetResult_Request) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_GetResult_Request>, size: usize) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_GetResult_Request>);
    fn fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DiveToDepth_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_GetResult_Request>) -> bool;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for DiveToDepth_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DiveToDepth_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DiveToDepth_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/action/DiveToDepth_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_GetResult_Request() }
  }
}


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__init(msg: *mut DiveToDepth_GetResult_Response) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_GetResult_Response>, size: usize) -> bool;
    fn fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_GetResult_Response>);
    fn fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DiveToDepth_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<DiveToDepth_GetResult_Response>) -> bool;
}

// Corresponds to fake_depth2_interfaces__action__DiveToDepth_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DiveToDepth_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::DiveToDepth_Result,

}



impl Default for DiveToDepth_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DiveToDepth_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__action__DiveToDepth_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DiveToDepth_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DiveToDepth_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/action/DiveToDepth_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__action__DiveToDepth_GetResult_Response() }
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


