
cd ~/ros2_ws/src

tar -xzf tf2_demo_pkg.tar.gz


cd ~/ros2_ws

colcon build --packages-select tf2_demo_pkg

source install/setup.bash


ros2 launch tf2_demo_pkg tf_demo_launch.py


ros2 run tf2_tools view_frames