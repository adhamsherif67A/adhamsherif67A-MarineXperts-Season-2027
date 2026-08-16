FROM ros:humble

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    ros-humble-mavros-msgs \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /task_9

RUN mkdir -p /task_9/ros2_ws/src

COPY ros2_ws/src /task_9/ros2_ws/src

WORKDIR /task_9/ros2_ws

RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build"

COPY README.md /task_9/README.md

RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
RUN echo "source /task_9/ros2_ws/install/setup.bash" >> /root/.bashrc

CMD ["/bin/bash"]
