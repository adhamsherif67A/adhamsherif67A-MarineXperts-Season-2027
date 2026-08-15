#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__srv__CalibrateDepth_Request() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__srv__CalibrateDepth_Request__init(msg: *mut CalibrateDepth_Request) -> bool;
    fn fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<CalibrateDepth_Request>, size: usize) -> bool;
    fn fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<CalibrateDepth_Request>);
    fn fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<CalibrateDepth_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<CalibrateDepth_Request>) -> bool;
}

// Corresponds to fake_depth2_interfaces__srv__CalibrateDepth_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CalibrateDepth_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub reset_to_zero: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub requested_offset: f32,

}



impl Default for CalibrateDepth_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__srv__CalibrateDepth_Request__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__srv__CalibrateDepth_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for CalibrateDepth_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__srv__CalibrateDepth_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for CalibrateDepth_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for CalibrateDepth_Request where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/srv/CalibrateDepth_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__srv__CalibrateDepth_Request() }
  }
}


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__srv__CalibrateDepth_Response() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__srv__CalibrateDepth_Response__init(msg: *mut CalibrateDepth_Response) -> bool;
    fn fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<CalibrateDepth_Response>, size: usize) -> bool;
    fn fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<CalibrateDepth_Response>);
    fn fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<CalibrateDepth_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<CalibrateDepth_Response>) -> bool;
}

// Corresponds to fake_depth2_interfaces__srv__CalibrateDepth_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CalibrateDepth_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub applied_offset: f32,

}



impl Default for CalibrateDepth_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__srv__CalibrateDepth_Response__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__srv__CalibrateDepth_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for CalibrateDepth_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__srv__CalibrateDepth_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for CalibrateDepth_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for CalibrateDepth_Response where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/srv/CalibrateDepth_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__srv__CalibrateDepth_Response() }
  }
}






#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__fake_depth2_interfaces__srv__CalibrateDepth() -> *const std::ffi::c_void;
}

// Corresponds to fake_depth2_interfaces__srv__CalibrateDepth
#[allow(missing_docs, non_camel_case_types)]
pub struct CalibrateDepth;

impl rosidl_runtime_rs::Service for CalibrateDepth {
    type Request = CalibrateDepth_Request;
    type Response = CalibrateDepth_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__fake_depth2_interfaces__srv__CalibrateDepth() }
    }
}


