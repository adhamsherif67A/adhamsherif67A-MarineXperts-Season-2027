ROS 2 Fake Depth Sensor
=======================

How to Run the Project
======================

1. Open a terminal and go to the project folder:

cd ~/task\ 4/fake_depth_project


2. Build the Docker image:

docker build -t ros2_fake_depth .


3. Start the Docker container:

docker run -it --name fake_depth_container ros2_fake_depth


4. Inside the container, source ROS 2:

source /opt/ros/humble/setup.bash


5. Go to the ROS 2 workspace:

cd ~/rov


6. Build the ROS 2 workspace:

colcon build


7. Source the workspace:

source ~/rov/install/setup.bash


8. Check that the package exists:

ros2 pkg list | grep fake_depth_sensor


Expected output:

fake_depth_sensor


9. Run the Publisher:

ros2 run fake_depth_sensor depth_publisher


Keep this terminal running.


10. Open another terminal on the host computer.

Go to the project folder:

cd ~/task\ 4/fake_depth_project


11. Open another terminal inside the running Docker container:

docker exec -it fake_depth_container bash


12. Source ROS 2:

source /opt/ros/humble/setup.bash


13. Source the workspace:

source ~/rov/install/setup.bash


14. Run the Subscriber:

ros2 run fake_depth_sensor depth_subscriber


The project is now running.


ROS 2 Commands
==============

Check the running nodes:

ros2 node list


Check the available topics:

ros2 topic list


Check the depth values:

ros2 topic echo /depth


Check information about the /depth topic:

ros2 topic info /depth


Check Publisher information:

ros2 node info /depth_publisher


Check Subscriber information:

ros2 node info /depth_subscriber


Stopping the Project
====================

Press:

Ctrl + C

to stop a running node.


If the Container Already Exists
================================

If you already created the container before, do not use:

docker run -it --name fake_depth_container ros2_fake_depth

Instead use:

docker start -ai fake_depth_container


Then source ROS 2:

source /opt/ros/humble/setup.bash


And source the workspace:

source ~/rov/install/setup.bash


To open another terminal inside the running container:

docker exec -it fake_depth_container bash
