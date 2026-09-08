# Use ROS 2 Humble (Ubuntu 22.04 Jammy)
FROM ros:humble-ros-base-jammy

# Prevent interactive prompts during apt installations
ENV DEBIAN_FRONTEND=noninteractive
ENV GZ_VERSION=harmonic

# 1. Install System Dependencies & Add Official Gazebo Repo
RUN apt-get update && apt-get install -y \
    git sudo wget curl tzdata lsb-release gnupg \
    python3-pip python3-setuptools python3-wheel \
    python3-rosdep python3-colcon-common-extensions \
    build-essential cmake

# Ubuntu 22.04 does not have Harmonic by default. We must add the OSRF repo.
RUN wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null \
    && apt-get update \
    && apt-get install -y gz-harmonic

# 2. Build the ros_gz bridge from source for Harmonic compatibility
WORKDIR /ros_gz_ws
RUN git clone https://github.com/gazebosim/ros_gz.git -b humble src/ros_gz \
    && apt-get update \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src -y -r --rosdistro humble \
    && /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build --cmake-args -DGZ_VERSION=harmonic"

# 3. Install and Build ArduPilot SITL (ArduSub)
WORKDIR /ardupilot
RUN git clone --recurse-submodules https://github.com/ArduPilot/ardupilot.git . \
    && USER=root Tools/environment_install/install-prereqs-ubuntu.sh -y \
    && ./waf configure --board sitl \
    && ./waf sub

# 4. Install and Build the ArduPilot Gazebo Plugin
WORKDIR /ardupilot_gazebo
RUN git clone https://github.com/ArduPilot/ardupilot_gazebo.git . \
    && mkdir build && cd build \
    && cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    && make -j4

# 5. Setup Your Custom ROS 2 Workspace
WORKDIR /ros2_ws
# Copy your local 'src' directory into the container
COPY ./src /ros2_ws/src

# Install workspace dependencies and compile
RUN apt-get update \
    && rosdep install --from-paths src --ignore-src -y -r --rosdistro humble \
    && rm -rf /var/lib/apt/lists/*
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && source /ros_gz_ws/install/setup.bash && colcon build --symlink-install"

# 6. Export Environment Variables
ENV GZ_SIM_SYSTEM_PLUGIN_PATH=/ardupilot_gazebo/build:${GZ_SIM_SYSTEM_PLUGIN_PATH}
ENV GZ_SIM_RESOURCE_PATH=/ros2_ws/install/share:${GZ_SIM_RESOURCE_PATH}

# 7. Set up the Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
