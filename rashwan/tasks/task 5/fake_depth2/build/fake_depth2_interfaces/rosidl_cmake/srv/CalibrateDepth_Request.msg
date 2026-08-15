# Request: how to calibrate / reset the fake depth sensor.
#
# If reset_to_zero is true, the node's zero_offset is reset to 0.0
# and 'requested_offset' is ignored.
# If reset_to_zero is false, the node's zero_offset is set to
# 'requested_offset' instead.
bool reset_to_zero
float32 requested_offset
