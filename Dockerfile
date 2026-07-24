FROM ros:humble-ros-base

WORKDIR /app

SHELL ["/bin/bash", "-c"]

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

RUN source /opt/ros/humble/setup.bash && ros2 topic list

CMD ["/bin/bash"]
