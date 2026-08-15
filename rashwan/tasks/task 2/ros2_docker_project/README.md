ROS 2 Humble Docker Project

Base OS:
Ubuntu 22.04

ROS 2:
ROS 2 Humble

Extra Dependency:
RViz2

Build:
docker build -t ros2-humble-project .

Run:
docker run -it --name ros2_humble_container ros2-humble-project

Verification:
ros2 topic list

Expected output:
/parameter_events
/rosout
