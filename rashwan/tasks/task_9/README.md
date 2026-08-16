# Task 9 — MAVROS Flight State Monitor

## 1. Project Overview

This project implements a ROS 2 Flight State Monitor for MAVROS/ArduSub.

The monitor subscribes to:

```text
/mavros/state
```

and displays a human-readable message whenever one of the following values changes:

* Connection status
* Armed state
* Flight mode

The project is fully containerized using Docker and ROS 2 Humble.

For testing purposes, the project includes a **Mock MAVROS State Publisher** that simulates the `/mavros/state` topic.

---

## 2. Project Architecture

In a real ArduSub system, the communication flow is:

```text
ROS 2 Node
    |
    v
  MAVROS
    |
    v
  MAVLink
    |
    v
  ArduSub
```

For this project, the real MAVROS/ArduSub system is replaced with a mock publisher:

```text
Mock MAVROS State Publisher
            |
            v
      /mavros/state
            |
            v
    Flight State Monitor
            |
            v
 Connection / Armed / Mode
```

---

## 3. Requirements

The host machine needs:

* Docker
* Internet connection during the first Docker image build

The project itself uses:

* Ubuntu
* Docker
* ROS 2 Humble
* C++
* Python
* `mavros_msgs`

No ArduSub hardware or SITL is required to test this version of the project.

---

## 4. Project Structure

```text
task_9/
├── Dockerfile
├── README.md
└── ros2_ws/
    └── src/
        └── flight_state_monitor/
            ├── CMakeLists.txt
            ├── package.xml
            ├── include/
            │   └── flight_state_monitor/
            │       └── state_monitor.hpp
            ├── scripts/
            │   └── mock_mavros_state.py
            └── src/
                └── state_monitor.cpp
```

### Main files

**`state_monitor.cpp`**

Contains the main Flight State Monitor node.

**`state_monitor.hpp`**

Contains the class definition and subscriber declarations.

**`mock_mavros_state.py`**

Simulates MAVROS by publishing different states to `/mavros/state`.

**`Dockerfile`**

Creates the complete ROS 2 Humble environment and builds the workspace.

---

# 5. Build the Docker Image

Open a terminal and go to the project directory:

```bash
cd ~/task_9
```

Build the Docker image:

```bash
docker build -t task_9_image .
```

After the build finishes, verify that the image exists:

```bash
docker images | grep task_9
```

Expected result:

```text
task_9_image
```

---

# 6. Start the Docker Container

Run:

```bash
docker run -it --name task_9_container task_9_image
```

If Docker reports that the container name is already in use, check the existing container:

```bash
docker ps -a | grep task_9_container
```

If the container already exists, start and attach to it:

```bash
docker start -ai task_9_container
```

---

# 7. Source the ROS 2 Environment

Inside the container, run:

```bash
source /opt/ros/humble/setup.bash
source /task_9/ros2_ws/install/setup.bash
```

Verify that the package is available:

```bash
ros2 pkg list | grep flight_state_monitor
```

Expected:

```text
flight_state_monitor
```

---

# 8. Run the Flight State Monitor

The monitor needs to stay running in one terminal.

Run:

```bash
ros2 run flight_state_monitor state_monitor
```

Expected output:

```text
Flight State Monitor started.
Waiting for /mavros/state ...
```

At this point the monitor is waiting for `/mavros/state`.

---

# 9. Run the Mock MAVROS Publisher

Open a **second terminal on the host machine**.

Connect to the same running container:

```bash
docker exec -it task_9_container bash
```

Source the environment:

```bash
source /opt/ros/humble/setup.bash
source /task_9/ros2_ws/install/setup.bash
```

Run the mock publisher:

```bash
ros2 run flight_state_monitor mock_mavros_state.py
```

The publisher will periodically publish different vehicle states to:

```text
/mavros/state
```

Example:

```text
Published -> connected=False, armed=False, mode=MANUAL
Published -> connected=True, armed=False, mode=MANUAL
Published -> connected=True, armed=True, mode=MANUAL
Published -> connected=True, armed=True, mode=STABILIZE
```

---

# 10. Expected Monitor Output

Go back to the first terminal where the monitor is running.

The monitor should report the state changes:

```text
[STATE CHANGE]
Connection: Disconnected
Armed: Disarmed
Mode: MANUAL
```

Then:

```text
[STATE CHANGE]
Connection: Connected
Armed: Disarmed
Mode: MANUAL
```

Then:

```text
[STATE CHANGE]
Connection: Connected
Armed: Armed
Mode: MANUAL
```

Then:

```text
[STATE CHANGE]
Connection: Connected
Armed: Armed
Mode: STABILIZE
```

The monitor does **not** print repeated messages when the state remains unchanged.

---

# 11. Verify the ROS 2 Topic

Open another terminal connected to the container:

```bash
docker exec -it task_9_container bash
```

Source ROS 2:

```bash
source /opt/ros/humble/setup.bash
source /task_9/ros2_ws/install/setup.bash
```

List available topics:

```bash
ros2 topic list
```

You should see:

```text
/mavros/state
/parameter_events
/rosout
```

---

# 12. Inspect `/mavros/state`

Check the topic information:

```bash
ros2 topic info /mavros/state
```

You should have:

```text
Publisher count: 1
Subscription count: 1
```

This means:

```text
Mock Publisher
      |
      v
/mavros/state
      |
      v
Flight State Monitor
```

You can also inspect the actual messages:

```bash
ros2 topic echo /mavros/state
```

Example:

```text
connected: true
armed: false
mode: MANUAL
```

---

# 13. Check Running Nodes

Run:

```bash
ros2 node list
```

Expected:

```text
/flight_state_monitor
/mock_mavros_state
```

---

# 14. Important Note About the Mock Publisher

The `mock_mavros_state.py` node is used only for testing.

In a real ArduSub system, the data would come from:

```text
ArduSub
   ↓
MAVLink
   ↓
MAVROS
   ↓
/mavros/state
   ↓
Flight State Monitor
```

Therefore, the Flight State Monitor does not depend on the mock publisher itself.

It only depends on receiving the correct MAVROS state message on:

```text
/mavros/state
```

---

# 15. Stopping the Project

To stop a running ROS 2 node:

```text
Ctrl + C
```

To exit the container:

```bash
exit
```

If you want to stop the container from the host:

```bash
docker stop task_9_container
```

To start the same container again later:

```bash
docker start -ai task_9_container
```

---

# 16. Rebuilding After Code Changes

If the source code is modified, rebuild the workspace inside the container:

```bash
cd /task_9/ros2_ws

source /opt/ros/humble/setup.bash

colcon build

source install/setup.bash
```

Then run the nodes again.

If the Dockerfile or dependencies are modified, rebuild the Docker image from the host:

```bash
cd ~/task_9

docker build -t task_9_image .
```

---

# 17. Project Goal

The goal of Task 9 is to understand how MAVROS provides vehicle state information to ROS 2.

The project demonstrates how a ROS 2 node can monitor:

* MAVROS connection status
* Vehicle armed state
* Current flight mode

without directly communicating with raw MAVLink messages.

The main concept is:

```text
ROS 2
  ↕
MAVROS
  ↕
MAVLink
  ↕
ArduSub
```

The Flight State Monitor represents the ROS 2 side of this communication.

---

# 18. Quick Start

For someone who already has Docker installed, the shortest way to run the project is:

### Terminal 1

```bash
cd ~/task_9

docker build -t task_9_image .

docker run -it --name task_9_container task_9_image
```

Inside the container:

```bash
source /opt/ros/humble/setup.bash
source /task_9/ros2_ws/install/setup.bash

ros2 run flight_state_monitor state_monitor
```

### Terminal 2

```bash
docker exec -it task_9_container bash

source /opt/ros/humble/setup.bash
source /task_9/ros2_ws/install/setup.bash

ros2 run flight_state_monitor mock_mavros_state.py
```

If the monitor prints the connection, armed state, and mode changes, the project is working correctly.

