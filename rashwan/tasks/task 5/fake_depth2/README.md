
## Interfaces

**`DepthReading.msg`** — published on `/depth`:
```
std_msgs/Header header
float32 depth
float32 zero_offset
bool threshold_crossed
```

**`CalibrateDepth.srv`** — served at `/calibrate_depth`:
```
bool reset_to_zero
float32 requested_offset
---
bool success
string message
float32 applied_offset
```

**`DiveToDepth.action`** — served at `/dive_to_depth`:
```
float32 target_depth
float32 dive_rate
---
bool success
float32 final_depth
string message
---
float32 current_depth
float32 remaining_distance
float32 percent_complete
```

## Build

Requires ROS 2 (tested against Humble/Iron/Jazzy — any modern rolling
distro's ament_cmake + rclcpp + rclcpp_action should work) and colcon.

```bash
cd fake_depth2
rosdep install --from-paths src --ignore-src -r -y   # first time only
colcon build --symlink-install
source install/setup.bash
```

Build order is handled automatically by colcon: `fake_depth2_interfaces`
builds first (it generates the message/service/action C++ headers), then
`fake_depth2` builds against them.

## Run everything with the launch file

```bash
ros2 launch fake_depth2 fake_depth2.launch.py
```

This starts `depth_sensor_node` and `depth_monitor_node` together, both
configured from `config/params.yaml`, with a topic remapping wired through
consistently to both nodes.

Override the topic name or parameter file from the command line:

```bash
ros2 launch fake_depth2 fake_depth2.launch.py depth_topic:=depth_raw
ros2 launch fake_depth2 fake_depth2.launch.py params_file:=/absolute/path/to/custom_params.yaml
```

## Run nodes individually (for testing each piece)

```bash
# Terminal 1
ros2 run fake_depth2 depth_sensor_node --ros-args --params-file src/fake_depth2/config/params.yaml

# Terminal 2
ros2 run fake_depth2 depth_monitor_node --ros-args --params-file src/fake_depth2/config/params.yaml

# Terminal 3 — watch the topic
ros2 topic echo /depth
```


Check/set live, e.g.:
```bash
ros2 param get /depth_sensor_node warn_threshold
ros2 param set /depth_monitor_node depth_threshold 15.0
```

## Try the Service (calibration)

```bash
# Reset zero_offset to 0.0
ros2 run fake_depth2 calibrate_client --reset

# Set zero_offset to +2.5 m
ros2 run fake_depth2 calibrate_client 2.5

# Or call it directly with the generic CLI:
ros2 service call /calibrate_depth fake_depth2_interfaces/srv/CalibrateDepth \
  "{reset_to_zero: false, requested_offset: 2.5}"
```

## Try the Action (dive simulation)

```bash
# Dive to 25 m at the default rate
ros2 run fake_depth2 dive_client 25.0

# Dive to 3 m at 1.0 m/s, then Ctrl+C partway through to cancel
ros2 run fake_depth2 dive_client 3.0 1.0

# Or with the generic CLI (also shows feedback):
ros2 action send_goal /dive_to_depth fake_depth2_interfaces/action/DiveToDepth \
  "{target_depth: 20.0, dive_rate: 1.0}" --feedback
```


