#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to fake_depth2_interfaces__srv__CalibrateDepth_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::CalibrateDepth_Request::default())
  }
}

impl rosidl_runtime_rs::Message for CalibrateDepth_Request {
  type RmwMsg = super::srv::rmw::CalibrateDepth_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        reset_to_zero: msg.reset_to_zero,
        requested_offset: msg.requested_offset,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      reset_to_zero: msg.reset_to_zero,
      requested_offset: msg.requested_offset,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      reset_to_zero: msg.reset_to_zero,
      requested_offset: msg.requested_offset,
    }
  }
}


// Corresponds to fake_depth2_interfaces__srv__CalibrateDepth_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CalibrateDepth_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub applied_offset: f32,

}



impl Default for CalibrateDepth_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::CalibrateDepth_Response::default())
  }
}

impl rosidl_runtime_rs::Message for CalibrateDepth_Response {
  type RmwMsg = super::srv::rmw::CalibrateDepth_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
        message: msg.message.as_str().into(),
        applied_offset: msg.applied_offset,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
        message: msg.message.as_str().into(),
      applied_offset: msg.applied_offset,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
      message: msg.message.to_string(),
      applied_offset: msg.applied_offset,
    }
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


