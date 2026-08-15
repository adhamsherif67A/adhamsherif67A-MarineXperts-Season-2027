#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to fake_depth2_interfaces__msg__DepthReading
/// A single simulated depth sensor reading.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DepthReading {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,

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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::DepthReading::default())
  }
}

impl rosidl_runtime_rs::Message for DepthReading {
  type RmwMsg = super::msg::rmw::DepthReading;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        depth: msg.depth,
        zero_offset: msg.zero_offset,
        threshold_crossed: msg.threshold_crossed,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      depth: msg.depth,
      zero_offset: msg.zero_offset,
      threshold_crossed: msg.threshold_crossed,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      depth: msg.depth,
      zero_offset: msg.zero_offset,
      threshold_crossed: msg.threshold_crossed,
    }
  }
}


