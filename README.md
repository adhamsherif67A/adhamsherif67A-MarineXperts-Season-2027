# MarineXperts2027
repo for all marinexperts software members

## Mako ROV simulation

This repository includes the ROS 2 Humble / Gazebo Harmonic Mako simulation,
ArduPilot SITL integration, and Operation MX pilot GUI. See [readme.md](readme.md)
for setup and [gui/README.md](gui/README.md) for the pilot application.

Optional RGB-D SLAM mapping is available in Operation MX via **Enable SLAM
mapping**. It uses ZED visual odometry and RTAB-Map, saves each run to a separate
database, and is disabled by default. See
[src/robot_description/ZED_VO.md](src/robot_description/ZED_VO.md) for details.
