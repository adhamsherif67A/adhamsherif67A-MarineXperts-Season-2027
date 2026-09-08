Markdown

# Orca ROV Simulation Environment

A high-fidelity, Dockerized simulation environment for the custom Orca ROV. This project integrates **ROS 2 Humble**, **Gazebo Harmonic**, and **ArduPilot SITL (ArduSub)** to provide an accurate physics and hydrodynamic testing ground for underwater robotics.

## 🚀 Features

*   **Accurate Hydrodynamics:** Custom-tuned graded buoyancy pool environment that accurately simulates the air-to-water physical transition at `Z = 0.0`.
*   **ArduSub SITL Integration:** Direct MAVLink communication with ArduSub via the ArduPilot Gazebo Plugin for realistic flight controller and joystick testing.
*   **Tuned Thruster Physics:** Blue Robotics T200 thrusters configured with accurate mass, inertia, and software-damped joints to prevent high-frequency physics oscillations.
*   **Sensor Suite:** Integrated ZED 2i RGBD camera and Bar30 depth/pressure sensor.
*   **Portable Docker Environment:** A fully containerized workspace that automatically builds the `ros_gz` bridge from source to ensure seamless compatibility between ROS 2 Humble and Gazebo Harmonic.

---

## 📋 Prerequisites

To run this simulation, you do not need ROS 2 or Gazebo installed on your host machine. You only need:
*   [Docker](https://docs.docker.com/get-docker/) installed and running.
*   An X11 server (native on Linux) to render the Gazebo GUI.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone [[https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)](https://github.com/adhamsherif67A/adhamsherif67A-MarineXperts-Season-2027.git)
cd YOUR_REPO_NAME

2. Build the Docker Image

The included Dockerfile will automatically pull ROS 2 Humble, install Gazebo Harmonic via OSRF repositories, compile ArduPilot SITL, and build your local ROS 2 workspace.

Note: The initial build may take 10-15 minutes as it compiles the ros_gz bridge and ArduPilot from source.
Bash

docker build -t rov_simulation .

3. Launch the Container (with GUI Support)

To allow the Docker container to open the Gazebo Harmonic window on your host machine, you must grant it access to your local X11 display server.

Run the following commands:
Bash

# Allow local Docker connections to the X server (Run once per terminal session)
xhost +local:root

# Spin up the container with X11 forwarding and host networking
docker run -it --rm \
    --net=host \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    rov_simulation

4. Run the Simulation

Once inside the running Docker container, your environment variables and ROS 2 workspaces are automatically sourced via the entrypoint.sh script.

Launch the Gazebo world and spawn the ROV:
Bash

# Replace 'robot_description' with your actual package name if different
ros2 launch robot_description gazebo.launch.py

Note: The ROV is configured to spawn at Z = -1.0 to ensure it is fully submerged and engages the graded buoyancy hydrodynamics immediately.
🗂️ Project Structure

    Dockerfile - The complete Ubuntu 22.04 environment definition.

    entrypoint.sh - Auto-sources ROS 2 Humble, the ros_gz bridge, and the custom workspace.

    src/robot_description/ - The core ROS 2 package containing:

        urdf/robot_description.urdf: The vehicle model, collision volumes, and Gazebo plugins.

        urdf/ardusub.urdf.xacro: ArduPilot motor channel mappings.

        worlds/CompetitionWorld2025.sdf: The physics environment featuring graded buoyancy.

        launch/gazebo.launch.py: The main launch script.
