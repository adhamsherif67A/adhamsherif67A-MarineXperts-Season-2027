#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "fake_depth2_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__msg__DepthReading() -> *const std::ffi::c_void;
}

#[link(name = "fake_depth2_interfaces__rosidl_generator_c")]
extern "C" {
    fn fake_depth2_interfaces__msg__DepthReading__init(msg: *mut DepthReading) -> bool;
    fn fake_depth2_interfaces__msg__DepthReading__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DepthReading>, size: usize) -> bool;
    fn fake_depth2_interfaces__msg__DepthReading__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DepthReading>);
    fn fake_depth2_interfaces__msg__DepthReading__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DepthReading>, out_seq: *mut rosidl_runtime_rs::Sequence<DepthReading>) -> bool;
}

// Corresponds to fake_depth2_interfaces__msg__DepthReading
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// A single simulated depth sensor reading.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DepthReading {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,

    /// Depth in meters, positive = deeper.
    pub depth: f32,

    /// The zero-offset (calibration) currently applied to this reading.
    pub zero_offset: f32,

    /// True if this reading crossed the configured warning threshold
    /// relative to the previous reading (edge-triggered).
    pub threshold_crossed: bool,

}



impl Default for DepthReading {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !fake_depth2_interfaces__msg__DepthReading__init(&mut msg as *mut _) {
        panic!("Call to fake_depth2_interfaces__msg__DepthReading__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DepthReading {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__msg__DepthReading__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__msg__DepthReading__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { fake_depth2_interfaces__msg__DepthReading__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DepthReading {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DepthReading where Self: Sized {
  const TYPE_NAME: &'static str = "fake_depth2_interfaces/msg/DepthReading";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__fake_depth2_interfaces__msg__DepthReading() }
  }
}


