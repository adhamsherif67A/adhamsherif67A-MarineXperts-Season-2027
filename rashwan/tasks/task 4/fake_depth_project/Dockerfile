FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    nano \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/rov

COPY rov /root/rov

SHELL ["/bin/bash", "-c"]

CMD ["bash"]
