#!/usr/bin/env bash
set -euo pipefail
image="${MAKO_IMAGE:-marinexperts/mako:boda}"
name="${MAKO_CONTAINER_NAME:-mako-sim}"
headless=false;nvidia=false
simulation_args=()
for argument in "$@"; do
  case "$argument" in
    --nvidia) nvidia=true ;;
    --headless) headless=true;simulation_args+=("$argument") ;;
    --help) echo 'Usage: docker/run.sh [--world pool.world|ocean.world] [--headless] [--nvidia] [--odometry-source ground_truth|vision] [--pilot-fps 30|60]';exit 0 ;;
    *) simulation_args+=("$argument") ;;
  esac
done
command -v docker >/dev/null || { echo 'Install Docker first; see readme.md.' >&2;exit 1; }
docker image inspect "$image" >/dev/null 2>&1 || { echo 'Run ./docker/build.sh first.' >&2;exit 1; }
options=(--rm --init --name "$name" --network host --ipc host --stop-timeout 15
         --env "ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-42}" --env RMW_IMPLEMENTATION=rmw_fastrtps_cpp)
if [[ -n "${LIBGL_ALWAYS_SOFTWARE:-}" ]]; then options+=(--env LIBGL_ALWAYS_SOFTWARE);fi
if [[ -t 0 && -t 1 ]]; then options+=(-it);fi
for device in /dev/dri/card* /dev/dri/renderD*; do
  [[ -c "$device" ]] || continue
  options+=(--device "$device" --group-add "$(stat -c '%g' "$device")")
done
if $nvidia; then options+=(--gpus all --env NVIDIA_DRIVER_CAPABILITIES=graphics,utility,compute);fi
cookie=''
cleanup() { if [[ -n "$cookie" ]]; then rm -f -- "$cookie";fi; }
trap cleanup EXIT
if ! $headless; then
  [[ -n "${DISPLAY:-}" && -d /tmp/.X11-unix ]] || { echo 'An X11/XWayland display is required; use --headless on servers.' >&2;exit 1; }
  command -v xauth >/dev/null || { echo 'Install host package xauth for GUI access, or use --headless.' >&2;exit 1; }
  cookie="$(mktemp)";chmod 644 "$cookie"
  xauth nlist "$DISPLAY" | sed 's/^..../ffff/' | xauth -f "$cookie" nmerge -
  [[ -s "$cookie" ]] || { echo 'No X11 authentication cookie found for DISPLAY.' >&2;exit 1; }
  options+=(--env DISPLAY --env QT_X11_NO_MITSHM=1 --env XAUTHORITY=/tmp/mako.xauth
            --volume /tmp/.X11-unix:/tmp/.X11-unix:rw --volume "$cookie:/tmp/mako.xauth:ro")
fi
docker run "${options[@]}" "$image" simulation "${simulation_args[@]}"
