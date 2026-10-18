#!/usr/bin/env bash
set -e
source /opt/ros/humble/setup.bash
source /home/boda/mako_ws/install/setup.bash
source /home/boda/Software2026/install/local_setup.bash
export MAKO_WORKSPACE=/home/boda/mako_ws
export MAKO_SOFTWARE_WORKSPACE=/home/boda/Software2026
exec python3 /home/boda/Software2026/src/real_joy/src/rov_gui_gst.py "$@"
