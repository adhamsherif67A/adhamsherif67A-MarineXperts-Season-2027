#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
import cv2
import numpy as np
import threading
import message_filters

# ---------------------------------------------------------------------------
# TUNEABLE CONSTANTS
# ---------------------------------------------------------------------------

# -- Dome port refraction correction ----------------------------------------
# Set True if camera is behind an underwater dome port.
USE_DOME_CORRECTION = False

N_WATER   = 1.333   # Refractive index of water
N_ACRYLIC = 1.491   # Refractive index of dome material
R_INNER   = 0.2    # Inner dome radius (metres)
R_OUTER   = 0.21    # Outer dome radius (metres)

# Apparent-to-true depth scalar  (> 1 → ZED underestimates, correction inflates)
DOME_K = (N_WATER / N_ACRYLIC) * (R_OUTER / R_INNER)

# -- Depth sampling ----------------------------------------------------------
SAMPLE_RADIUS    = 4    # Pixels around click (smaller → less edge bleed)
DEPTH_BUFFER_LEN = 5    # Frames kept for temporal median (0 = single frame)

# ---------------------------------------------------------------------------


class DepthMeasurementNode(Node):
    def __init__(self):
        super().__init__('zed_depth_measurement_node')
        self.bridge  = CvBridge()
        self._lock   = threading.Lock()

        # Latest data
        self.latest_rgb   = None
        self.depth_buffer = []   # Rolling list of depth frames (numpy float32)
        self.intrinsics   = None # {fx, fy, cx, cy}

        # Click state
        self.points      = []   # [(u, v), ...]         – pixel coords
        self.world_pts   = []   # [(X, Y, Z), ...]      – 3-D world coords
        self.last_result = None # String shown on screen

        # Subscriptions -------------------------------------------------------
        self.info_sub = self.create_subscription(
            CameraInfo,
            '/zed/zed_node/depth/camera_info',
            self.info_callback,
            10,
        )

        self.rgb_sub   = message_filters.Subscriber(
            self, Image, '/zed/zed_node/rgb/image_rect_color')
        self.depth_sub = message_filters.Subscriber(
            self, Image, '/zed/zed_node/depth/depth_registered')

        self.ts = message_filters.ApproximateTimeSynchronizer(
            [self.rgb_sub, self.depth_sub], queue_size=10, slop=0.05)
        self.ts.registerCallback(self.sync_callback)

        # GUI -----------------------------------------------------------------
        cv2.namedWindow('ZED Depth Measurement')
        cv2.setMouseCallback('ZED Depth Measurement', self.mouse_callback)
        self.timer = self.create_timer(0.033, self.timer_callback)

        self.get_logger().info(
            f'Node ready.  DOME_CORRECTION={USE_DOME_CORRECTION}  '
            f'DOME_K={DOME_K:.4f}  SAMPLE_RADIUS={SAMPLE_RADIUS}  '
            f'DEPTH_BUFFER_LEN={DEPTH_BUFFER_LEN}'
        )
        self.get_logger().info('Waiting for CameraInfo and images…')

    # -------------------------------------------------------------------------
    # ROS callbacks
    # -------------------------------------------------------------------------

    def info_callback(self, msg: CameraInfo):
        """Cache intrinsic parameters from CameraInfo."""
        with self._lock:
            if self.intrinsics is not None:
                return  # Already have them; update only on change if needed.
            # K = [fx, 0, cx, 0, fy, cy, 0, 0, 1]
            self.intrinsics = {
                'fx': msg.k[0],
                'fy': msg.k[4],
                'cx': msg.k[2],
                'cy': msg.k[5],
            }
            self.get_logger().info(
                f'Intrinsics received: fx={msg.k[0]:.2f} fy={msg.k[4]:.2f} '
                f'cx={msg.k[2]:.2f} cy={msg.k[5]:.2f}'
            )

    def sync_callback(self, rgb_msg: Image, depth_msg: Image):
        """Store latest RGB and append depth frame to the rolling buffer."""
        rgb   = self.bridge.imgmsg_to_cv2(rgb_msg, 'bgr8')
        # ZED depth_registered → 32FC1 in metres
        depth = self.bridge.imgmsg_to_cv2(depth_msg, '32FC1')

        with self._lock:
            self.latest_rgb = rgb

            if DEPTH_BUFFER_LEN > 1:
                self.depth_buffer.append(depth)
                if len(self.depth_buffer) > DEPTH_BUFFER_LEN:
                    self.depth_buffer.pop(0)
            else:
                # Single-frame mode – keep exactly one entry
                self.depth_buffer = [depth]

    # -------------------------------------------------------------------------
    # Core depth → 3-D logic
    # -------------------------------------------------------------------------

    def _get_stable_depth_map(self) -> np.ndarray | None:
        """
        Returns a per-pixel median depth map across the rolling buffer.
        Must be called inside self._lock.
        """
        if not self.depth_buffer:
            return None
        if len(self.depth_buffer) == 1:
            return self.depth_buffer[0]
        stack = np.stack(self.depth_buffer, axis=0)          # (T, H, W)
        return np.nanmedian(stack, axis=0).astype(np.float32) # (H, W)

    def _sample_depth(self, depth_map: np.ndarray, u: int, v: int) -> float | None:
        """
        Robust depth estimate at pixel (u, v) using:
          1. A square patch of radius SAMPLE_RADIUS
          2. Removal of NaN / Inf / near-zero values
          3. IQR-based outlier rejection (handles depth edges)
          4. Median of surviving values
        Returns depth in metres, or None if insufficient valid data.
        """
        h, w = depth_map.shape
        u0, u1 = max(0, u - SAMPLE_RADIUS), min(w, u + SAMPLE_RADIUS + 1)
        v0, v1 = max(0, v - SAMPLE_RADIUS), min(h, v + SAMPLE_RADIUS + 1)

        roi = depth_map[v0:v1, u0:u1].ravel()

        # Step 1 – remove invalid pixels
        valid = roi[np.isfinite(roi) & (roi > 0.01)]
        if len(valid) < 3:
            return None

        # Step 2 – IQR outlier rejection (guards against edge bleed)
        q25, q75 = np.percentile(valid, [25, 75])
        iqr = q75 - q25
        if iqr > 0:
            lo, hi = q25 - 1.5 * iqr, q75 + 1.5 * iqr
            valid = valid[(valid >= lo) & (valid <= hi)]

        if len(valid) < 3:
            return None

        return float(np.median(valid))

    def _get_3d_point(self, u: int, v: int) -> tuple[float, float, float] | None:
        """
        Converts pixel (u, v) to corrected world coordinates (X, Y, Z) in metres.

        Dome correction (when enabled):
          The ZED's stereo algorithm assumes light travels straight (air).
          Inside water the apparent (measured) depth is shallower than truth.
          We scale the raw depth by DOME_K before back-projecting so that
          X, Y and Z are all derived from the same corrected Z.
        """
        with self._lock:
            depth_map = self._get_stable_depth_map()
            if depth_map is None or self.intrinsics is None:
                return None

            z_raw = self._sample_depth(depth_map, u, v)
            if z_raw is None:
                return None

            # Apply dome refraction correction BEFORE back-projection
            z = z_raw * DOME_K if USE_DOME_CORRECTION else z_raw

            fx = self.intrinsics['fx']
            fy = self.intrinsics['fy']
            cx = self.intrinsics['cx']
            cy = self.intrinsics['cy']

            x = (u - cx) * z / fx
            y = (v - cy) * z / fy

        return (float(x), float(y), float(z))

    # -------------------------------------------------------------------------
    # Mouse / UI
    # -------------------------------------------------------------------------

    def mouse_callback(self, event, x: int, y: int, flags, param):
        if event != cv2.EVENT_LBUTTONDOWN:
            return

        if len(self.points) >= 2:
            self._reset()

        pt_3d = self._get_3d_point(x, y)
        if pt_3d:
            self.points.append((x, y))
            self.world_pts.append(pt_3d)
            self.get_logger().info(
                f'Point {len(self.points)} locked: '
                f'X={pt_3d[0]:+.3f}m  Y={pt_3d[1]:+.3f}m  Z={pt_3d[2]:.3f}m'
            )
            if len(self.points) == 2:
                self._calculate_metrics()
        else:
            self.get_logger().warn(
                f'Could not get reliable depth at pixel ({x}, {y}). '
                'Try clicking on a well-lit, non-edge surface.'
            )

    def _calculate_metrics(self):
        p1 = np.array(self.world_pts[0])
        p2 = np.array(self.world_pts[1])

        dist_3d  = np.linalg.norm(p1 - p2)
        dist_h   = np.linalg.norm([p1[0] - p2[0], p1[2] - p2[2]])  # XZ plane
        dist_v   = abs(p1[1] - p2[1])                               # Y axis

        self.last_result = (
            f'3D: {dist_3d*100:.1f}cm  '
            f'H: {dist_h*100:.1f}cm  '
            f'V: {dist_v*100:.1f}cm'
        )
        self.get_logger().info(f'Measurement → {self.last_result}')

    def timer_callback(self):
        with self._lock:
            if self.latest_rgb is None:
                return
            img = self.latest_rgb.copy()

        # Draw clicked points
        for i, p in enumerate(self.points):
            cv2.circle(img, p, 6, (0, 0, 255), -1)
            label = (
                f'P{i+1}  '
                f'X={self.world_pts[i][0]:+.2f}  '
                f'Y={self.world_pts[i][1]:+.2f}  '
                f'Z={self.world_pts[i][2]:.2f}m'
            )
            cv2.putText(img, label, (p[0] + 8, p[1] - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # Draw measurement line and result
        if len(self.points) == 2:
            cv2.line(img, self.points[0], self.points[1], (0, 255, 0), 2)
            cv2.putText(img, self.last_result,
                        (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # HUD
        dome_str = f'Dome corr ON  K={DOME_K:.3f}' if USE_DOME_CORRECTION else 'Dome corr OFF'
        cv2.putText(img, dome_str,
                    (20, img.shape[0] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (200, 200, 0), 1)
        cv2.putText(img, 'Click 2 points | R = reset',
                    (20, img.shape[0] - 35), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (200, 200, 0), 1)

        cv2.imshow('ZED Depth Measurement', img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            self._reset()

    def _reset(self):
        self.points      = []
        self.world_pts   = []
        self.last_result = None
        self.get_logger().info('Reset.')


# -----------------------------------------------------------------------------

def main():
    rclpy.init()
    node = DepthMeasurementNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
