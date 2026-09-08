#!/bin/bash
set -e

# Source the main ROS 2 Humble installation
source /opt/ros/humble/setup.bash

# Source the custom ros_gz bridge (built for Harmonic)
if [ -f /ros_gz_ws/install/setup.bash ]; then
  source /ros_gz_ws/install/setup.bash
fi

# Source your custom workspace
if [ -f /ros2_ws/install/setup.bash ]; then
  source /ros2_ws/install/setup.bash
fi

# Execute the command passed into the Docker container
exec "$@"
