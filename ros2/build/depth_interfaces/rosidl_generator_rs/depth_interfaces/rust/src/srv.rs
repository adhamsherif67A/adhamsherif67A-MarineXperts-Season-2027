#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to depth_interfaces__srv__Calibrate_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Calibrate_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub zero_offset: f32,

}



impl Default for Calibrate_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Calibrate_Request::default())
  }
}

impl rosidl_runtime_rs::Message for Calibrate_Request {
  type RmwMsg = super::srv::rmw::Calibrate_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        zero_offset: msg.zero_offset,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      zero_offset: msg.zero_offset,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      zero_offset: msg.zero_offset,
    }
  }
}


// Corresponds to depth_interfaces__srv__Calibrate_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Calibrate_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: std::string::String,

}



impl Default for Calibrate_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Calibrate_Response::default())
  }
}

impl rosidl_runtime_rs::Message for Calibrate_Response {
  type RmwMsg = super::srv::rmw::Calibrate_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
        message: msg.message.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
        message: msg.message.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
      message: msg.message.to_string(),
    }
  }
}






#[link(name = "depth_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__depth_interfaces__srv__Calibrate() -> *const std::ffi::c_void;
}

// Corresponds to depth_interfaces__srv__Calibrate
#[allow(missing_docs, non_camel_case_types)]
pub struct Calibrate;

impl rosidl_runtime_rs::Service for Calibrate {
    type Request = Calibrate_Request;
    type Response = Calibrate_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__depth_interfaces__srv__Calibrate() }
    }
}


