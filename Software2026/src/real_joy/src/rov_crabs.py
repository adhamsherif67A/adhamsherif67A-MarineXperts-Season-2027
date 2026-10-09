#!/usr/bin/env python3
"""
MarineXperts ROV Control Station GUI
PyQt5 + ROS2 (rclpy) Dashboard
Handles: GStreamer H.264 UDP Stream, Pixhawk 2.4.8 via MAVROS, Screen+Mic Recording
+ YOLO real-time object detection overlay (toggle on/off without interrupting stream)

GStreamer pipeline (low-latency):
  udpsrc port=5000 → rtph264depay → h264parse → avdec_h264 → videoconvert → appsink
"""

import sys
import os

# ✅ IMPORTANT FIX (must be BEFORE PyQt5 & cv2)
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/usr/lib/x86_64-linux-gnu/qt5/plugins"
os.environ["QT_PLUGIN_PATH"] = "/usr/lib/x86_64-linux-gnu/qt5/plugins"


import time
import subprocess
import signal
import queue
import threading
from datetime import datetime

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QPushButton, QFrame, QProgressBar,
    QSizePolicy, QGroupBox, QSplitter
)
from PyQt5.QtCore import (
    Qt, QTimer, QThread, pyqtSignal, pyqtSlot, QSize
)
from PyQt5.QtGui import (
    QFont, QColor, QPixmap, QPainter, QPen, QImage
)

# ── ROS2 optional import ──────────────────────────────────────────────────────
try:
    import rclpy
    from rclpy.node import Node
    from rclpy.executors import MultiThreadedExecutor
    ROS2_AVAILABLE = True
except ImportError:
    ROS2_AVAILABLE = False
    print("[WARN] rclpy not found – running in demo/offline mode.")

# ── MAVROS message types (optional) ──────────────────────────────────────────
try:
    from mavros_msgs.msg import State, RCOut
    MAVROS_MSGS_AVAILABLE = True
except ImportError:
    MAVROS_MSGS_AVAILABLE = False
    print("[WARN] mavros_msgs not found – Pixhawk data simulated.")

# ── NumPy ─────────────────────────────────────────────────────────────────────
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    print("[WARN] numpy not found – video frame display disabled.")

# ── GStreamer — import ONLY, NO Gst.init() here ───────────────────────────────
try:
    import gi
    gi.require_version("Gst", "1.0")
    from gi.repository import Gst, GLib
    GST_AVAILABLE = True
except Exception as e:
    GST_AVAILABLE = False
    print(f"[WARN] GStreamer (gi) not found – video feed disabled. ({e})")

# ── YOLO (Ultralytics) ────────────────────────────────────────────────────────
try:
    from ultralytics import YOLO as UltralyticsYOLO
    YOLO_AVAILABLE = True
except ImportError:
    YOLO_AVAILABLE = False
    print("[WARN] ultralytics not found – YOLO detection disabled.")

# ── OpenCV (needed to draw YOLO boxes onto frames) ────────────────────────────
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False
    print("[WARN] opencv-python not found – YOLO overlay drawing disabled.")

# ─────────────────────────────────────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
THRUSTER_COUNT  = 6
PWM_MIN         = 1100
PWM_MAX         = 1900
PWM_NEUTRAL     = 1500
RECONNECT_DELAY = 3.0
APP_TITLE       = "MarineXperts — ROV Control Station"
TEAM_NAME       = "MarineXperts"
SUBTITLE        = "ROV Control Station"

THRUSTER_LABELS = [
    "T1 – Fwd-Right",
    "T2 – Fwd-Left",
    "T3 – Vert-FP",
    "T4 – Vert-FS",
    "T5 – Lat-Left",
    "T6 – Lat-Right",
]

P_ATMOSPHERE  = 101325.0
RHO_SEAWATER  = 1025.0
G_GRAVITY     = 9.81
DEPTH_TOPIC   = "/depth_cm"   # std_msgs/Float32  — value in centimetres

GST_UDP_PORT    = 5000
GST_RECONNECT_S = 4.0

# ── YOLO defaults ─────────────────────────────────────────────────────────────
# Point this to your .pt model file. Can also be overridden via env var YOLO_MODEL_PATH.
#YOLO_MODEL_PATH    = os.environ.get("/home/boda/Crab8.3/runs/detect/local_crab_specialist2/weights/best.pt", "yolov8n.pt")
YOLO_MODEL_PATH = os.environ.get("YOLO_MODEL_PATH", "/home/boda/Crab8.3/runs/detect/local_crab_specialist2/weights/best.pt")
YOLO_CONF_THRESH   = 0.8   # confidence threshold
YOLO_IOU_THRESH    = 0.45   # NMS IoU threshold
YOLO_MAX_QUEUE     = 2       # max frames waiting for inference (drop older ones)
YOLO_BOX_THICKNESS = 2
YOLO_FONT_SCALE    = 0.55
YOLO_FONT          = cv2.FONT_HERSHEY_SIMPLEX if CV2_AVAILABLE else None

# ─────────────────────────────────────────────────────────────────────────────
#  COLOUR PALETTE
# ─────────────────────────────────────────────────────────────────────────────
C = {
    "bg_dark":     "#050d14",
    "bg_panel":    "#0a1a26",
    "bg_card":     "#0f2236",
    "border":      "#1a3a54",
    "accent":      "#00c8ff",
    "accent2":     "#0082b0",
    "green":       "#00e676",
    "yellow":      "#ffd600",
    "red":         "#ff1744",
    "text_hi":     "#e8f4ff",
    "text_mid":    "#7db8d8",
    "text_lo":     "#3a6a88",
    "thruster_lo": "#0082b0",
    "thruster_hi": "#00c8ff",
    "yolo_active": "#00ff88",   # YOLO button active state
    "yolo_bg":     "#003322",   # YOLO button active background
}

# ─────────────────────────────────────────────────────────────────────────────
#  STYLE SHEET
# ─────────────────────────────────────────────────────────────────────────────
STYLESHEET = f"""
QMainWindow, QWidget {{
    background-color: {C['bg_dark']};
    color: {C['text_hi']};
    font-family: 'Courier New', monospace;
}}
QGroupBox {{
    border: 1px solid {C['border']};
    border-radius: 6px;
    margin-top: 14px;
    background-color: {C['bg_panel']};
    font-family: 'Courier New', monospace;
    font-size: 11px;
    font-weight: bold;
    color: {C['accent']};
    letter-spacing: 2px;
    text-transform: uppercase;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: 12px;
    padding: 2px 8px;
    background-color: {C['bg_dark']};
    border-radius: 3px;
}}
QLabel {{
    color: {C['text_hi']};
    background: transparent;
}}
QPushButton {{
    background-color: {C['bg_card']};
    color: {C['accent']};
    border: 1px solid {C['accent2']};
    border-radius: 4px;
    padding: 7px 18px;
    font-family: 'Courier New', monospace;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 1px;
    text-transform: uppercase;
}}
QPushButton:hover {{
    background-color: {C['accent2']};
    color: {C['bg_dark']};
    border-color: {C['accent']};
}}
QPushButton:pressed {{
    background-color: {C['accent']};
    color: {C['bg_dark']};
}}
QPushButton:disabled {{
    color: {C['text_lo']};
    border-color: {C['text_lo']};
    background-color: {C['bg_dark']};
}}
QPushButton#btn_record {{
    color: {C['red']};
    border-color: {C['red']};
}}
QPushButton#btn_record:hover {{
    background-color: {C['red']};
    color: white;
}}
QPushButton#btn_stop {{
    color: {C['yellow']};
    border-color: {C['yellow']};
}}
QPushButton#btn_stop:hover {{
    background-color: {C['yellow']};
    color: {C['bg_dark']};
}}
QPushButton#btn_yolo_start {{
    color: {C['yolo_active']};
    border-color: {C['yolo_active']};
    background-color: {C['bg_card']};
}}
QPushButton#btn_yolo_start:hover {{
    background-color: {C['yolo_bg']};
    color: white;
    border-color: {C['yolo_active']};
}}
QPushButton#btn_yolo_stop {{
    color: {C['yellow']};
    border-color: {C['yellow']};
    background-color: {C['yolo_bg']};
}}
QPushButton#btn_yolo_stop:hover {{
    background-color: {C['yellow']};
    color: {C['bg_dark']};
}}
QProgressBar {{
    background-color: {C['bg_dark']};
    border: 1px solid {C['border']};
    border-radius: 3px;
    height: 14px;
    text-align: center;
    font-size: 9px;
    color: {C['text_hi']};
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {C['thruster_lo']}, stop:1 {C['thruster_hi']});
    border-radius: 3px;
}}
QStatusBar {{
    background-color: {C['bg_panel']};
    color: {C['text_mid']};
    font-size: 10px;
    border-top: 1px solid {C['border']};
}}
QFrame#separator {{
    background-color: {C['border']};
}}
"""


# ─────────────────────────────────────────────────────────────────────────────
#  GSTREAMER WORKER
# ─────────────────────────────────────────────────────────────────────────────
class GStreamerWorker(QThread):
    """
    Low-latency H.264/RTP → appsink pipeline with GPU decode auto-detection.
    Now also pushes raw numpy frames into a shared queue for YOLO consumption.
    """

    frame_signal     = pyqtSignal(QImage)
    connected_signal = pyqtSignal(bool)
    log_signal       = pyqtSignal(str)

    _BACKENDS = [
        (
            "NVIDIA RTX/GTX (nvh264dec + cudadownload)",
            "nvh264dec",
            "! cudadownload ! videoconvert",
        ),
        (
            "VA-API AMD/Intel (vaapih264dec)",
            "vaapih264dec",
            "! vaapipostproc ! videoconvert",
        ),
        (
            "CPU fallback (avdec_h264)",
            "avdec_h264 direct-rendering=false max-threads=2",
            "! videoconvert",
        ),
    ]

    def __init__(self, port: int = GST_UDP_PORT, parent=None):
        super().__init__(parent)
        self._port     = port
        self._running  = False
        self._pipeline = None
        self._backend  = None

        # ── Shared frame queue for YOLO ───────────────────────────────────────
        # Only holds numpy arrays (H×W×3 RGB). YOLO worker consumes from here.
        # maxsize=YOLO_MAX_QUEUE ensures old frames are dropped when inference
        # is slower than the stream — stream is NEVER blocked.
        self.yolo_frame_queue: queue.Queue = queue.Queue(maxsize=YOLO_MAX_QUEUE)

    def _build_pipeline(self, decoder: str, post: str) -> str:
        return (
            f'udpsrc port={self._port} '
            f'caps="application/x-rtp, media=video, encoding-name=H264, payload=96" '
            f'! rtph264depay '
            f'! decodebin '
            f'! videoconvert '
            f'! video/x-raw,format=RGB '
            f'! appsink name=sink emit-signals=true max-buffers=1 drop=true sync=false'
        )

    @staticmethod
    def _element_exists(name: str) -> bool:
        result = subprocess.run(
            ["gst-inspect-1.0", "--exists", name.split()[0]],
            capture_output=True,
        )
        return result.returncode == 0

    def _detect_backend(self) -> tuple:
        for name, decoder, post in self._BACKENDS:
            elem_name = decoder.split()[0]
            if self._element_exists(elem_name):
                self.log_signal.emit(f"[GST] Decoder selected: {name}  ({elem_name})")
                return name, decoder, post
        self.log_signal.emit("[GST] WARNING: no suitable decoder found, using CPU fallback.")
        return self._BACKENDS[-1]

    def run(self):
        self._running = True

        if not GST_AVAILABLE:
            self.log_signal.emit("[GST] GStreamer unavailable – stream disabled.")
            self.connected_signal.emit(False)
            return

        if not NUMPY_AVAILABLE:
            self.log_signal.emit("[GST] numpy unavailable – stream disabled.")
            self.connected_signal.emit(False)
            return

        GLib.threads_init()
        Gst.init(None)

        name, decoder, post = self._detect_backend()
        self._backend = name

        while self._running:
            self._run_pipeline(decoder, post)
            if self._running:
                self.log_signal.emit(
                    f"[GST] Pipeline stopped – retrying in {GST_RECONNECT_S:.0f}s…"
                )
                self.connected_signal.emit(False)
                time.sleep(GST_RECONNECT_S)

    def _run_pipeline(self, decoder: str, post: str):
        desc = self._build_pipeline(decoder, post)
        self.log_signal.emit(
            f"[GST] Starting — backend: {self._backend} — port: {self._port}"
        )

        try:
            pipeline = Gst.parse_launch(desc)
        except Exception as e:
            self.log_signal.emit(f"[GST] parse_launch failed: {e}")
            if "avdec" not in decoder:
                self.log_signal.emit("[GST] Falling back to CPU decoder…")
                _, cpu_dec, cpu_post = self._BACKENDS[-1]
                self._backend = "CPU (avdec_h264)"
                self._run_pipeline(cpu_dec, cpu_post)
            return

        sink = pipeline.get_by_name("sink")
        if sink is None:
            self.log_signal.emit("[GST] appsink element not found in pipeline.")
            pipeline.set_state(Gst.State.NULL)
            return

        sink.connect("new-sample", self._on_new_sample)
        pipeline.set_state(Gst.State.PLAYING)
        self._pipeline = pipeline

        bus = pipeline.get_bus()
        bus.add_signal_watch()

        first_error = True

        while self._running:
            msg = bus.timed_pop_filtered(
                200 * Gst.MSECOND,
                Gst.MessageType.ERROR | Gst.MessageType.EOS,
            )
            if msg is None:
                continue

            if msg.type == Gst.MessageType.ERROR:
                err, dbg = msg.parse_error()
                self.log_signal.emit(f"[GST] Error: {err.message}  ({dbg})")

                if first_error and "avdec" not in decoder:
                    first_error = False
                    pipeline.set_state(Gst.State.NULL)
                    self._pipeline = None
                    self.log_signal.emit("[GST] GPU decoder error — falling back to CPU.")
                    self._backend = "CPU (avdec_h264)"
                    _, cpu_dec, cpu_post = self._BACKENDS[-1]
                    self._run_pipeline(cpu_dec, cpu_post)
                    return
                break

            if msg.type == Gst.MessageType.EOS:
                self.log_signal.emit("[GST] End-of-stream.")
                break

        pipeline.set_state(Gst.State.NULL)
        self._pipeline = None
        self.connected_signal.emit(False)

    def _on_new_sample(self, sink) -> int:
        sample = sink.emit("pull-sample")
        if sample is None:
            return Gst.FlowReturn.OK

        buf       = sample.get_buffer()
        structure = sample.get_caps().get_structure(0)
        width     = structure.get_value("width")
        height    = structure.get_value("height")

        ok, mapinfo = buf.map(Gst.MapFlags.READ)
        if not ok:
            return Gst.FlowReturn.OK

        try:
            frame = np.frombuffer(mapinfo.data, dtype=np.uint8)
            if frame.size < width * height * 3:
                return Gst.FlowReturn.OK

            # Make a contiguous copy for display AND for YOLO
            frame_copy = frame[:width * height * 3].reshape((height, width, 3)).copy()

            # ── Push to YOLO queue (non-blocking — drop frame if queue full) ──
            # This never blocks the GStreamer callback, preserving stream latency.
            try:
                self.yolo_frame_queue.put_nowait(frame_copy)
            except queue.Full:
                pass   # YOLO is slower than stream — silently drop

            # ── Emit raw QImage to display ────────────────────────────────────
            qi = QImage(
                frame_copy.data,
                width, height,
                width * 3,
                QImage.Format_RGB888,
            ).copy()

        except Exception as e:
            self.log_signal.emit(f"[GST] Frame convert error: {e}")
            return Gst.FlowReturn.OK
        finally:
            buf.unmap(mapinfo)

        self.frame_signal.emit(qi)
        self.connected_signal.emit(True)
        return Gst.FlowReturn.OK

    def stop(self):
        self._running = False
        if self._pipeline:
            try:
                self._pipeline.set_state(Gst.State.NULL)
            except Exception:
                pass
        self.quit()
        self.wait(3000)


# ─────────────────────────────────────────────────────────────────────────────
#  YOLO WORKER
# ─────────────────────────────────────────────────────────────────────────────
class YOLOWorker(QThread):
    """
    Runs YOLO inference on frames pulled from GStreamerWorker.yolo_frame_queue.

    Design principles:
    - Model is loaded ONCE when the worker starts (expensive operation).
    - Inference runs in its own QThread — never blocks Qt UI or GStreamer.
    - Stream is COMPLETELY unaffected: if YOLO is slow, it drops frames
      (queue has maxsize=YOLO_MAX_QUEUE). The raw stream always flows through.
    - Stopping the worker (stop()) is instant: sets _running=False, the thread
      exits its loop within one inference cycle, then the next start() reuses
      the already-loaded model (no reload cost).
    - annotated_frame_signal emits QImage with boxes drawn via OpenCV.
    - status_signal emits a short status string for the GUI label.
    - error_signal emits a human-readable error string on failure.
    """

    annotated_frame_signal = pyqtSignal(QImage)   # frame with boxes
    status_signal          = pyqtSignal(str)       # e.g. "3 obj | 28 ms"
    log_signal             = pyqtSignal(str)
    error_signal           = pyqtSignal(str)       # shown in GUI on failure
    loading_signal         = pyqtSignal(bool)      # True while model loads

    # Class-level model cache — survives stop/start cycles within same session
    _model_cache: dict = {}   # path → YOLO model instance

    def __init__(self, frame_queue: queue.Queue, model_path: str = YOLO_MODEL_PATH, parent=None):
        super().__init__(parent)
        self._queue      = frame_queue
        self._model_path = model_path
        self._running    = False
        self._model      = None

    def run(self):
        self._running = True

        if not YOLO_AVAILABLE:
            self.error_signal.emit("ultralytics not installed — pip install ultralytics")
            return

        if not CV2_AVAILABLE:
            self.error_signal.emit("opencv-python not installed — pip install opencv-python")
            return

        if not NUMPY_AVAILABLE:
            self.error_signal.emit("numpy not available")
            return

        # ── Load model (use cache to avoid reloading on toggle) ───────────────
        if self._model_path not in YOLOWorker._model_cache:
            self.log_signal.emit(f"[YOLO] Loading model: {self._model_path}")
            self.loading_signal.emit(True)
            try:
                YOLOWorker._model_cache[self._model_path] = UltralyticsYOLO(self._model_path)
                self.log_signal.emit(f"[YOLO] Model loaded: {self._model_path}")
            except Exception as e:
                self.error_signal.emit(f"Model load failed: {e}")
                self.loading_signal.emit(False)
                return
            self.loading_signal.emit(False)
        else:
            self.log_signal.emit(f"[YOLO] Reusing cached model: {self._model_path}")

        self._model = YOLOWorker._model_cache[self._model_path]
        self.status_signal.emit("YOLO ACTIVE")

        # ── Inference loop ────────────────────────────────────────────────────
        while self._running:
            try:
                # Block up to 0.5 s waiting for a frame — allows clean shutdown
                frame_rgb = self._queue.get(timeout=0.5)
            except queue.Empty:
                continue

            t0 = time.monotonic()

            try:
                # Ultralytics expects BGR for most ops but accepts numpy arrays;
                # We pass RGB directly — works fine with ultralytics >= 8.0.
                results = self._model.predict(
                    source=frame_rgb,
                    conf=YOLO_CONF_THRESH,
                    iou=YOLO_IOU_THRESH,
                    verbose=False,
                    stream=False,
                )
            except Exception as e:
                self.log_signal.emit(f"[YOLO] Inference error: {e}")
                continue

            dt_ms = (time.monotonic() - t0) * 1000

            # ── Draw detections onto a copy of the frame ──────────────────────
            annotated = frame_rgb.copy()   # RGB numpy array
            n_det = 0

            for result in results:
                boxes = result.boxes
                if boxes is None:
                    continue
                for box in boxes:
                    n_det += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    conf  = float(box.conf[0])
                    cls_i = int(box.cls[0])
                    label_text = (
                        result.names[cls_i] if result.names and cls_i in result.names
                        else str(cls_i)
                    )
                    tag = f"{label_text} {conf:.2f}"

                    # Colour per class index (cycling through palette)
                    hue = (cls_i * 47) % 180
                    # Convert HSV→BGR for cv2, then back to RGB
                    hsv  = np.array([[[hue, 255, 220]]], dtype=np.uint8)
                    bgr  = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)[0][0]
                    colour = (int(bgr[2]), int(bgr[1]), int(bgr[0]))   # BGR→RGB

                    # Bounding box
                    cv2.rectangle(annotated, (x1, y1), (x2, y2), colour, YOLO_BOX_THICKNESS)

                    # Label background
                    (tw, th), _ = cv2.getTextSize(tag, YOLO_FONT, YOLO_FONT_SCALE, 1)
                    lbl_y = max(y1 - 4, th + 4)
                    cv2.rectangle(
                        annotated,
                        (x1, lbl_y - th - 4),
                        (x1 + tw + 4, lbl_y + 2),
                        colour, -1,
                    )
                    # Label text (dark on coloured background)
                    cv2.putText(
                        annotated, tag,
                        (x1 + 2, lbl_y),
                        YOLO_FONT, YOLO_FONT_SCALE,
                        (10, 10, 10), 1, cv2.LINE_AA,
                    )

            # ── YOLO overlay badge (top-left corner) ──────────────────────────
            badge = f"YOLO  {n_det} obj  {dt_ms:.0f}ms"
            cv2.rectangle(annotated, (6, 6), (len(badge) * 8 + 10, 26), (0, 20, 10), -1)
            cv2.putText(annotated, badge, (10, 20), YOLO_FONT, 0.5, (0, 255, 136), 1, cv2.LINE_AA)

            # ── Emit as QImage ────────────────────────────────────────────────
            h, w, _ = annotated.shape
            qi = QImage(annotated.data, w, h, w * 3, QImage.Format_RGB888).copy()
            self.annotated_frame_signal.emit(qi)
            self.status_signal.emit(f"{n_det} obj  |  {dt_ms:.0f} ms")

        self.status_signal.emit("YOLO OFF")
        self.log_signal.emit("[YOLO] Worker stopped.")

    def stop(self):
        self._running = False
        self.quit()
        self.wait(3000)


# ─────────────────────────────────────────────────────────────────────────────
#  LOGO WIDGET
# ─────────────────────────────────────────────────────────────────────────────
class LogoWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(64, 64)
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.jpeg")
        if os.path.exists(logo_path):
            pix = QPixmap(logo_path).scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(pix)
        else:
            self._draw_fallback()

    def _draw_fallback(self):
        pix = QPixmap(64, 64)
        pix.fill(Qt.transparent)
        p = QPainter(pix)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(QPen(QColor(C['accent']), 2))
        p.setBrush(QColor(C['bg_card']))
        p.drawEllipse(2, 2, 60, 60)
        p.setPen(QPen(QColor(C['accent']), 2.5))
        p.drawLine(32, 12, 32, 52)
        p.drawLine(20, 20, 44, 20)
        p.drawArc(14, 36, 18, 18, 0, -180 * 16)
        p.drawArc(32, 36, 18, 18, 0, -180 * 16)
        p.drawLine(14, 45, 20, 52)
        p.drawLine(50, 45, 44, 52)
        p.drawEllipse(26, 8, 12, 12)
        p.end()
        self.setPixmap(pix)


# ─────────────────────────────────────────────────────────────────────────────
#  STATUS INDICATOR
# ─────────────────────────────────────────────────────────────────────────────
class StatusDot(QWidget):
    def __init__(self, label: str, parent=None):
        super().__init__(parent)
        self._state = "disconnected"
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(6)

        self._dot = QLabel("●")
        self._dot.setFixedWidth(16)
        self._dot.setFont(QFont("Courier New", 14))

        self._lbl = QLabel(label)
        self._lbl.setFont(QFont("Courier New", 10))
        self._lbl.setStyleSheet(f"color:{C['text_mid']};")

        lay.addWidget(self._dot)
        lay.addWidget(self._lbl)
        lay.addStretch()
        self._apply()

    def set_state(self, state: str):
        self._state = state
        self._apply()

    def _apply(self):
        colours = {
            "connected":    C['green'],
            "disconnected": C['red'],
            "warning":      C['yellow'],
        }
        self._dot.setStyleSheet(f"color:{colours.get(self._state, C['red'])};")


# ─────────────────────────────────────────────────────────────────────────────
#  THRUSTER PWM ROW
# ─────────────────────────────────────────────────────────────────────────────
class ThrusterRow(QWidget):
    def __init__(self, index: int, parent=None):
        super().__init__(parent)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(4, 2, 4, 2)
        lay.setSpacing(8)

        self._lbl = QLabel(THRUSTER_LABELS[index])
        self._lbl.setFixedWidth(120)
        self._lbl.setFont(QFont("Courier New", 9))
        self._lbl.setStyleSheet(f"color:{C['text_mid']};")

        self._bar = QProgressBar()
        self._bar.setMinimum(0)
        self._bar.setMaximum(PWM_MAX - PWM_MIN)
        self._bar.setValue(PWM_NEUTRAL - PWM_MIN)
        self._bar.setFormat("")
        self._bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self._bar.setFixedHeight(14)

        self._val = QLabel(f"{PWM_NEUTRAL} µs")
        self._val.setFixedWidth(72)
        self._val.setFont(QFont("Courier New", 9, QFont.Bold))
        self._val.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._val.setStyleSheet(f"color:{C['accent']};")

        self._dir = QLabel("  ●")
        self._dir.setFixedWidth(20)
        self._dir.setFont(QFont("Courier New", 10))
        self._dir.setStyleSheet(f"color:{C['text_lo']};")

        lay.addWidget(self._lbl)
        lay.addWidget(self._bar)
        lay.addWidget(self._val)
        lay.addWidget(self._dir)

    def update_pwm(self, pwm: int):
        pwm = max(PWM_MIN, min(PWM_MAX, pwm))
        self._bar.setValue(pwm - PWM_MIN)
        self._val.setText(f"{pwm} µs")
        delta = pwm - PWM_NEUTRAL
        if abs(delta) < 30:
            self._dir.setStyleSheet(f"color:{C['text_lo']};")
            self._dir.setText("  ●")
        elif delta > 0:
            self._dir.setStyleSheet(f"color:{C['green']};")
            self._dir.setText("  ▲")
        else:
            self._dir.setStyleSheet(f"color:{C['yellow']};")
            self._dir.setText("  ▼")


# ─────────────────────────────────────────────────────────────────────────────
#  VIDEO PANEL  (receives QImage from GStreamerWorker OR YOLOWorker)
# ─────────────────────────────────────────────────────────────────────────────
class ZedPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._connected    = False
        self._yolo_active  = False   # when True, display annotated frames instead

        lay = QVBoxLayout(self)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        self._feed = QLabel()
        self._feed.setMinimumSize(320, 220)
        self._feed.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._feed.setAlignment(Qt.AlignCenter)
        self._feed.setStyleSheet(
            f"background-color:{C['bg_dark']};"
            f"border:1px solid {C['border']};"
            f"border-radius:4px;"
        )
        self._draw_offline()

        status_row = QHBoxLayout()
        self._dot   = StatusDot("Video Stream")

        self._yolo_status = QLabel("")
        self._yolo_status.setFont(QFont("Courier New", 8, QFont.Bold))
        self._yolo_status.setStyleSheet(f"color:{C['yolo_active']};")
        self._yolo_status.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self._info  = QLabel(f"UDP port {GST_UDP_PORT}  |  H.264/RTP  |  GStreamer")
        self._info.setFont(QFont("Courier New", 8))
        self._info.setStyleSheet(f"color:{C['text_lo']};")
        status_row.addWidget(self._dot)
        status_row.addWidget(self._yolo_status)
        status_row.addStretch()
        status_row.addWidget(self._info)

        lay.addWidget(self._feed)
        lay.addLayout(status_row)

    def _draw_offline(self):
        size = self._feed.size() if self._feed.width() > 1 else QSize(320, 220)
        pix  = QPixmap(size)
        pix.fill(QColor(C['bg_dark']))
        p = QPainter(pix)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(QPen(QColor(C['border']), 1))
        for x in range(0, pix.width(), 40):
            p.drawLine(x, 0, x, pix.height())
        for y in range(0, pix.height(), 40):
            p.drawLine(0, y, pix.width(), y)
        p.setPen(QColor(C['text_lo']))
        p.setFont(QFont("Courier New", 11, QFont.Bold))
        p.drawText(
            pix.rect(), Qt.AlignCenter,
            f"NO SIGNAL\n\nWaiting for H.264 stream\nUDP port {GST_UDP_PORT}",
        )
        p.end()
        self._feed.setPixmap(pix)

    @pyqtSlot(bool)
    def set_connected(self, ok: bool):
        self._connected = ok
        self._dot.set_state("connected" if ok else "disconnected")
        if not ok:
            self._draw_offline()

    @pyqtSlot(QImage)
    def update_frame(self, qi: QImage):
        """Called with RAW frames from GStreamer — only display if YOLO is off."""
        if self._yolo_active:
            return   # YOLO worker will send its own annotated frames
        self._display(qi)

    @pyqtSlot(QImage)
    def update_yolo_frame(self, qi: QImage):
        """Called with YOLO-annotated frames — only display if YOLO is active."""
        if not self._yolo_active:
            return
        self._display(qi)

    def _display(self, qi: QImage):
        pix = QPixmap.fromImage(qi).scaled(
            self._feed.width(),
            self._feed.height(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation,
        )
        self._feed.setPixmap(pix)

    def set_yolo_active(self, active: bool):
        self._yolo_active = active
        if not active:
            self._yolo_status.setText("")

    @pyqtSlot(str)
    def update_yolo_status(self, text: str):
        self._yolo_status.setText(f"⬡ YOLO  {text}")


# ─────────────────────────────────────────────────────────────────────────────
#  PIXHAWK PANEL
# ─────────────────────────────────────────────────────────────────────────────
class PixhawkPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(10)

        info_box = QGroupBox("FLIGHT CONTROLLER")
        info_lay = QGridLayout(info_box)
        info_lay.setContentsMargins(10, 18, 10, 10)
        info_lay.setSpacing(8)

        def kv(key, row):
            k = QLabel(key)
            k.setFont(QFont("Courier New", 9))
            k.setStyleSheet(f"color:{C['text_lo']};")
            v = QLabel("—")
            v.setFont(QFont("Courier New", 10, QFont.Bold))
            v.setStyleSheet(f"color:{C['accent']};")
            info_lay.addWidget(k, row, 0)
            info_lay.addWidget(v, row, 1)
            return v

        self._dot       = StatusDot("MAVLink/MAVROS")
        self._lbl_mode  = kv("MODE :", 1)
        self._lbl_armed = kv("ARMED :", 2)
        info_lay.addWidget(self._dot, 0, 0, 1, 2)
        info_lay.setColumnStretch(1, 1)

        thr_box = QGroupBox("THRUSTER PWM  (µs)")
        thr_lay = QVBoxLayout(thr_box)
        thr_lay.setContentsMargins(8, 20, 8, 8)
        thr_lay.setSpacing(4)

        self._thruster_rows: list[ThrusterRow] = []
        for i in range(THRUSTER_COUNT):
            row = ThrusterRow(i)
            self._thruster_rows.append(row)
            thr_lay.addWidget(row)

        legend = QHBoxLayout()
        for txt, align in [("1100", Qt.AlignLeft), ("1500 (neutral)", Qt.AlignCenter), ("1900", Qt.AlignRight)]:
            l = QLabel(txt)
            l.setAlignment(align)
            l.setFont(QFont("Courier New", 8))
            l.setStyleSheet(f"color:{C['text_lo']};")
            legend.addWidget(l, 1)
        thr_lay.addLayout(legend)

        lay.addWidget(info_box)
        lay.addWidget(thr_box)
        lay.addStretch()

    def update_state(self, connected, armed, guided, mode, **_):
        self._dot.set_state("connected" if connected else "disconnected")
        self._lbl_mode.setText(mode or "UNKNOWN")
        self._lbl_armed.setText(
            ("⬛ ARMED" if armed else "◻  DISARMED") if connected else "—"
        )
        self._lbl_armed.setStyleSheet(
            f"color:{'#c0392b' if armed else '#1b7a34'};" if connected
            else f"color:{C['text_lo']};"
        )

    def update_pwm(self, channels: list):
        for i, pwm in enumerate(channels[:THRUSTER_COUNT]):
            self._thruster_rows[i].update_pwm(pwm)


# ─────────────────────────────────────────────────────────────────────────────
#  PRESSURE PANEL
# ─────────────────────────────────────────────────────────────────────────────
class PressurePanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(8)

        self._dot = StatusDot("Depth Sensor")

        depth_row = QHBoxLayout()
        depth_icon = QLabel("▼")
        depth_icon.setFont(QFont("Courier New", 22, QFont.Bold))
        depth_icon.setStyleSheet(f"color:{C['accent2']};")
        depth_icon.setFixedWidth(30)

        depth_val_block = QVBoxLayout()
        depth_val_block.setSpacing(0)
        self._lbl_depth_val  = QLabel("—")
        self._lbl_depth_val.setFont(QFont("Courier New", 32, QFont.Bold))
        self._lbl_depth_val.setStyleSheet(f"color:{C['accent']};")
        self._lbl_depth_unit = QLabel("metres depth")
        self._lbl_depth_unit.setFont(QFont("Courier New", 9))
        self._lbl_depth_unit.setStyleSheet(f"color:{C['text_lo']};")
        depth_val_block.addWidget(self._lbl_depth_val)
        depth_val_block.addWidget(self._lbl_depth_unit)
        depth_row.addWidget(depth_icon, 0, Qt.AlignVCenter)
        depth_row.addLayout(depth_val_block)
        depth_row.addStretch()

        self._depth_bar = QProgressBar()
        self._depth_bar.setMinimum(0)
        self._depth_bar.setMaximum(100)
        self._depth_bar.setValue(0)
        self._depth_bar.setFormat("")
        self._depth_bar.setFixedHeight(10)
        self._depth_bar.setStyleSheet(
            f"QProgressBar {{ background:{C['bg_dark']}; border:1px solid {C['border']}; border-radius:2px; }}"
            f"QProgressBar::chunk {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"stop:0 {C['thruster_lo']}, stop:1 {C['accent']}); border-radius:2px; }}"
        )

        depth_scale = QHBoxLayout()
        for txt, a in [("0 m", Qt.AlignLeft), ("50 m", Qt.AlignCenter), ("100 m", Qt.AlignRight)]:
            l = QLabel(txt)
            l.setAlignment(a)
            l.setFont(QFont("Courier New", 7))
            l.setStyleSheet(f"color:{C['text_lo']};")
            depth_scale.addWidget(l, 1)

        grid_box = QGroupBox("RAW READINGS")
        grid = QGridLayout(grid_box)
        grid.setContentsMargins(10, 18, 10, 10)
        grid.setSpacing(6)

        def kv(label, row):
            k = QLabel(label)
            k.setFont(QFont("Courier New", 9))
            k.setStyleSheet(f"color:{C['text_lo']};")
            v = QLabel("—")
            v.setFont(QFont("Courier New", 10, QFont.Bold))
            v.setStyleSheet(f"color:{C['accent']};")
            grid.addWidget(k, row, 0)
            grid.addWidget(v, row, 1)
            return v

        self._lbl_depth_cm  = kv("DEPTH (cm)  :", 0)
        self._lbl_depth_m   = kv("DEPTH (m)   :", 1)
        self._lbl_topic     = kv("TOPIC       :", 2)
        self._lbl_topic.setText(DEPTH_TOPIC)
        self._lbl_topic.setStyleSheet(f"color:{C['text_lo']}; font-size:8px;")
        grid.setColumnStretch(1, 1)

        lay.addWidget(self._dot)
        lay.addLayout(depth_row)
        lay.addWidget(self._depth_bar)
        lay.addLayout(depth_scale)
        lay.addWidget(grid_box)
        lay.addStretch()

    def update_depth(self, depth_cm: float):
        self._dot.set_state("connected")
        depth_m = depth_cm / 100.0
        self._lbl_depth_val.setText(f"{depth_m:6.2f}")
        self._depth_bar.setValue(int(min(100, depth_m)))
        self._lbl_depth_cm.setText(f"{depth_cm:.1f} cm")
        self._lbl_depth_m.setText(f"{depth_m:.4f} m")
        col = C['green'] if depth_m < 10 else (C['accent'] if depth_m < 50 else C['red'])
        self._lbl_depth_val.setStyleSheet(f"color:{col};")

    def set_disconnected(self):
        self._dot.set_state("disconnected")
        for lbl in (self._lbl_depth_val, self._lbl_depth_cm, self._lbl_depth_m):
            lbl.setText("—")
        self._depth_bar.setValue(0)


# ─────────────────────────────────────────────────────────────────────────────
#  RECORDING MANAGER
# ─────────────────────────────────────────────────────────────────────────────
class RecordingManager:
    def __init__(self, status_callback=None):
        self._proc = None
        self._cb   = status_callback or (lambda m: None)
        self._file = ""

    def is_recording(self) -> bool:
        return self._proc is not None and self._proc.poll() is None

    def start(self):
        if self.is_recording():
            return
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._file = os.path.expanduser(f"~/rov_recording_{ts}.mp4")
        cmd = self._build_cmd(self._file)
        if cmd is None:
            self._cb("[REC] ffmpeg not found.")
            return
        try:
            self._proc = subprocess.Popen(
                cmd, stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            self._cb(f"[REC] Recording → {self._file}")
        except Exception as e:
            self._cb(f"[REC] Failed: {e}")
            self._proc = None

    def stop(self):
        if not self.is_recording():
            return
        try:
            self._proc.stdin.write(b"q\n")
            self._proc.stdin.flush()
            self._proc.wait(timeout=5)
        except Exception:
            self._proc.kill()
        self._cb(f"[REC] Saved → {self._file}")
        self._proc = None

    def _build_cmd(self, outfile):
        if subprocess.run(["which", "ffmpeg"], capture_output=True).returncode != 0:
            return None
        display = os.environ.get("DISPLAY", ":0.0")
        return [
            "ffmpeg", "-y",
            "-f", "x11grab", "-r", "30", "-i", display,
            "-f", "pulse", "-i", "default",
            "-c:v", "libx264", "-preset", "ultrafast",
            "-c:a", "aac", "-b:a", "128k",
            outfile,
        ]


# ─────────────────────────────────────────────────────────────────────────────
#  ROS2 WORKER
# ─────────────────────────────────────────────────────────────────────────────
class RosWorker(QThread):
    pixhawk_state_signal = pyqtSignal(bool, bool, bool, str)
    pixhawk_pwm_signal   = pyqtSignal(list)
    depth_signal         = pyqtSignal(float)
    log_signal           = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._running  = False
        self._node     = None
        self._executor = None

    def run(self):
        self._running = True
        self.log_signal.emit("[ROS2] Worker thread started.")

        if not ROS2_AVAILABLE:
            self.log_signal.emit("[ROS2] rclpy unavailable – demo mode active.")
            self._demo_loop()
            return

        try:
            rclpy.init()
        except Exception as e:
            self.log_signal.emit(f"[ROS2] Init failed: {e}")
            self._demo_loop()
            return

        while self._running:
            try:
                self._create_node()
                self.log_signal.emit("[ROS2] Node created, spinning…")
                self._executor.spin()
            except Exception as e:
                self.log_signal.emit(f"[ROS2] Node error: {e} — retrying in {RECONNECT_DELAY}s")
                self._cleanup_node()
                self._emit_disconnected()
                time.sleep(RECONNECT_DELAY)

        self._cleanup_node()
        try:
            rclpy.shutdown()
        except Exception:
            pass

    def _create_node(self):
        self._node     = Node("marinexpert_gui")
        self._executor = MultiThreadedExecutor()
        self._executor.add_node(self._node)

        if MAVROS_MSGS_AVAILABLE:
            self._node.create_subscription(State, "/mavros/state",  self._on_state,  10)
            self._node.create_subscription(RCOut, "/mavros/rc/out", self._on_rcout, 10)

        try:
            from std_msgs.msg import Float32
            self._node.create_subscription(Float32, DEPTH_TOPIC, self._on_depth_cm, 10)
            self.log_signal.emit(f"[DEPTH] Subscribed to {DEPTH_TOPIC}")
        except Exception as e:
            self.log_signal.emit(f"[DEPTH] Subscription error: {e}")

    def _cleanup_node(self):
        try:
            if self._executor:
                self._executor.shutdown(timeout_sec=1)
            if self._node:
                self._node.destroy_node()
        except Exception:
            pass
        self._node = self._executor = None

    def _emit_disconnected(self):
        self.pixhawk_state_signal.emit(False, False, False, "—")
        self.depth_signal.emit(-1.0)

    def _on_state(self, msg):
        try:
            self.pixhawk_state_signal.emit(msg.connected, msg.armed, msg.guided, msg.mode)
        except Exception as e:
            self.log_signal.emit(f"[PIX] State error: {e}")

    def _on_rcout(self, msg):
        try:
            channels = list(msg.channels[:THRUSTER_COUNT])
            while len(channels) < THRUSTER_COUNT:
                channels.append(PWM_NEUTRAL)
            self.pixhawk_pwm_signal.emit(channels)
        except Exception as e:
            self.log_signal.emit(f"[PIX] RCOut error: {e}")

    def _on_depth_cm(self, msg):
        try:
            self.depth_signal.emit(float(msg.data))
        except Exception as e:
            self.log_signal.emit(f"[DEPTH] Callback error: {e}")

    def _demo_loop(self):
        import math
        t = 0
        while self._running:
            t += 0.1
            pwms = [int(PWM_NEUTRAL + 150 * math.sin(t + i * 0.8)) for i in range(THRUSTER_COUNT)]
            sim_depth_cm = 500.0 * (0.5 + 0.5 * math.sin(t * 0.3))
            self.pixhawk_state_signal.emit(True, False, True, "STABILIZE")
            self.pixhawk_pwm_signal.emit(pwms)
            self.depth_signal.emit(sim_depth_cm)
            time.sleep(0.1)

    def stop(self):
        self._running = False
        if self._executor:
            try:
                self._executor.shutdown(timeout_sec=1)
            except Exception:
                pass
        self.quit()
        self.wait(3000)


# ─────────────────────────────────────────────────────────────────────────────
#  HEADER  (now includes YOLO toggle button)
# ─────────────────────────────────────────────────────────────────────────────
class HeaderWidget(QWidget):
    record_start = pyqtSignal()
    record_stop  = pyqtSignal()
    yolo_start   = pyqtSignal()   # emitted when user clicks "START YOLO"
    yolo_stop    = pyqtSignal()   # emitted when user clicks "STOP YOLO"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(88)
        self.setStyleSheet(
            f"background: qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"stop:0 {C['bg_panel']}, stop:0.5 {C['bg_card']}, stop:1 {C['bg_panel']});"
            f"border-bottom: 1px solid {C['border']};"
        )
        lay = QHBoxLayout(self)
        lay.setContentsMargins(18, 8, 18, 8)
        lay.setSpacing(14)

        lay.addWidget(LogoWidget(), 0, Qt.AlignVCenter)

        name_block = QVBoxLayout()
        name_block.setSpacing(0)
        t = QLabel(TEAM_NAME)
        t.setFont(QFont("Courier New", 22, QFont.Bold))
        t.setStyleSheet(f"color:{C['accent']}; letter-spacing:4px;")
        s = QLabel(SUBTITLE)
        s.setFont(QFont("Courier New", 10))
        s.setStyleSheet(f"color:{C['text_mid']}; letter-spacing:2px;")
        name_block.addWidget(t)
        name_block.addWidget(s)
        lay.addLayout(name_block)
        lay.addStretch()

        dt_block = QVBoxLayout()
        dt_block.setSpacing(2)
        self._lbl_date = QLabel()
        self._lbl_date.setFont(QFont("Courier New", 11, QFont.Bold))
        self._lbl_date.setStyleSheet(f"color:{C['text_hi']};")
        self._lbl_date.setAlignment(Qt.AlignRight)
        self._lbl_time = QLabel()
        self._lbl_time.setFont(QFont("Courier New", 18, QFont.Bold))
        self._lbl_time.setStyleSheet(f"color:{C['accent']}; letter-spacing:2px;")
        self._lbl_time.setAlignment(Qt.AlignRight)
        dt_block.addWidget(self._lbl_date)
        dt_block.addWidget(self._lbl_time)
        lay.addLayout(dt_block)

        sep = QFrame()
        sep.setFrameShape(QFrame.VLine)
        sep.setStyleSheet(f"color:{C['border']};")
        lay.addWidget(sep)

        # ── YOLO block ────────────────────────────────────────────────────────
        yolo_block = QVBoxLayout()
        yolo_block.setSpacing(4)
        self._btn_yolo_start = QPushButton("⬡  YOLO ON")
        self._btn_yolo_start.setObjectName("btn_yolo_start")
        self._btn_yolo_start.setFixedWidth(120)
        self._btn_yolo_start.setEnabled(YOLO_AVAILABLE and CV2_AVAILABLE)
        self._btn_yolo_stop = QPushButton("⬡  YOLO OFF")
        self._btn_yolo_stop.setObjectName("btn_yolo_stop")
        self._btn_yolo_stop.setFixedWidth(120)
        self._btn_yolo_stop.setEnabled(False)
        self._lbl_yolo = QLabel("● IDLE")
        self._lbl_yolo.setFont(QFont("Courier New", 8))
        self._lbl_yolo.setAlignment(Qt.AlignCenter)
        self._lbl_yolo.setStyleSheet(f"color:{C['text_lo']};")
        if not (YOLO_AVAILABLE and CV2_AVAILABLE):
            self._lbl_yolo.setText("NOT INSTALLED")
            self._lbl_yolo.setStyleSheet(f"color:{C['red']}; font-size:7px;")
        self._btn_yolo_start.clicked.connect(self._on_yolo_start)
        self._btn_yolo_stop.clicked.connect(self._on_yolo_stop)
        yolo_block.addWidget(self._btn_yolo_start)
        yolo_block.addWidget(self._btn_yolo_stop)
        yolo_block.addWidget(self._lbl_yolo)
        lay.addLayout(yolo_block)

        sep2 = QFrame()
        sep2.setFrameShape(QFrame.VLine)
        sep2.setStyleSheet(f"color:{C['border']};")
        lay.addWidget(sep2)

        # ── Recording block ───────────────────────────────────────────────────
        rec_block = QVBoxLayout()
        rec_block.setSpacing(4)
        self._btn_rec  = QPushButton("⏺  REC")
        self._btn_rec.setObjectName("btn_record")
        self._btn_rec.setFixedWidth(110)
        self._btn_stop = QPushButton("⏹  STOP")
        self._btn_stop.setObjectName("btn_stop")
        self._btn_stop.setFixedWidth(110)
        self._btn_stop.setEnabled(False)
        self._lbl_rec  = QLabel("● IDLE")
        self._lbl_rec.setFont(QFont("Courier New", 8))
        self._lbl_rec.setAlignment(Qt.AlignCenter)
        self._lbl_rec.setStyleSheet(f"color:{C['text_lo']};")
        self._btn_rec.clicked.connect(self._on_rec)
        self._btn_stop.clicked.connect(self._on_stop)
        rec_block.addWidget(self._btn_rec)
        rec_block.addWidget(self._btn_stop)
        rec_block.addWidget(self._lbl_rec)
        lay.addLayout(rec_block)

        self._clock = QTimer(self)
        self._clock.timeout.connect(self._tick)
        self._clock.start(500)
        self._tick()

        self._blink = False
        self._blink_timer = QTimer(self)
        self._blink_timer.timeout.connect(self._blink_tick)

        self._yolo_blink       = False
        self._yolo_blink_timer = QTimer(self)
        self._yolo_blink_timer.timeout.connect(self._yolo_blink_tick)

    def _tick(self):
        now = datetime.now()
        self._lbl_date.setText(now.strftime("%A, %d %B %Y"))
        self._lbl_time.setText(now.strftime("%H:%M:%S"))

    # ── YOLO button handlers ──────────────────────────────────────────────────
    def _on_yolo_start(self):
        self._btn_yolo_start.setEnabled(False)
        self._btn_yolo_stop.setEnabled(True)
        self._lbl_yolo.setStyleSheet(f"color:{C['yellow']};")
        self._lbl_yolo.setText("LOADING…")
        self.yolo_start.emit()

    def _on_yolo_stop(self):
        self._btn_yolo_start.setEnabled(True)
        self._btn_yolo_stop.setEnabled(False)
        self._lbl_yolo.setStyleSheet(f"color:{C['text_lo']};")
        self._lbl_yolo.setText("● IDLE")
        self._yolo_blink_timer.stop()
        self.yolo_stop.emit()

    def set_yolo_loading(self, loading: bool):
        """Called when model is loading (show spinner text)."""
        if loading:
            self._lbl_yolo.setStyleSheet(f"color:{C['yellow']};")
            self._lbl_yolo.setText("LOADING…")
        else:
            self._lbl_yolo.setStyleSheet(f"color:{C['yolo_active']};")
            self._lbl_yolo.setText("● ACTIVE")
            self._yolo_blink_timer.start(1000)

    def set_yolo_error(self, msg: str):
        self._btn_yolo_start.setEnabled(YOLO_AVAILABLE and CV2_AVAILABLE)
        self._btn_yolo_stop.setEnabled(False)
        self._lbl_yolo.setStyleSheet(f"color:{C['red']}; font-size:7px;")
        self._lbl_yolo.setText("ERROR")
        self._yolo_blink_timer.stop()

    def _yolo_blink_tick(self):
        self._yolo_blink = not self._yolo_blink
        self._lbl_yolo.setStyleSheet(
            f"color:{C['yolo_active'] if self._yolo_blink else C['text_lo']};"
        )
        self._lbl_yolo.setText("● ACTIVE" if self._yolo_blink else "○ ACTIVE")

    # ── Recording button handlers ─────────────────────────────────────────────
    def _on_rec(self):
        self._btn_rec.setEnabled(False)
        self._btn_stop.setEnabled(True)
        self._lbl_rec.setStyleSheet(f"color:{C['red']};")
        self._lbl_rec.setText("● REC")
        self._blink_timer.start(800)
        self.record_start.emit()

    def _on_stop(self):
        self._btn_rec.setEnabled(True)
        self._btn_stop.setEnabled(False)
        self._lbl_rec.setStyleSheet(f"color:{C['text_lo']};")
        self._lbl_rec.setText("● IDLE")
        self._blink_timer.stop()
        self.record_stop.emit()

    def _blink_tick(self):
        self._blink = not self._blink
        self._lbl_rec.setStyleSheet(f"color:{C['red'] if self._blink else C['text_lo']};")
        self._lbl_rec.setText("● REC" if self._blink else "○ REC")


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN WINDOW
# ─────────────────────────────────────────────────────────────────────────────
class ROVMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.setMinimumSize(1100, 680)
        self.setStyleSheet(STYLESHEET)

        self._header   = HeaderWidget()
        self._zed      = ZedPanel()
        self._pixhawk  = PixhawkPanel()
        self._pressure = PressurePanel()
        self._recorder = RecordingManager(status_callback=self._log)
        self._yolo_worker: YOLOWorker | None = None

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)
        root.addWidget(self._header)

        content = QSplitter(Qt.Horizontal)
        content.setStyleSheet("QSplitter::handle { background-color: #6aafd4; width: 2px; }")

        zed_grp = QGroupBox("H.264 UDP STREAM  —  GStreamer")
        zed_lay = QVBoxLayout(zed_grp)
        zed_lay.setContentsMargins(6, 18, 6, 6)
        zed_lay.addWidget(self._zed)
        content.addWidget(zed_grp)

        right = QSplitter(Qt.Vertical)
        right.setStyleSheet("QSplitter::handle { background-color: #6aafd4; height: 2px; }")

        pix_grp = QGroupBox("PIXHAWK 2.4.8  —  MAVROS")
        pix_lay = QVBoxLayout(pix_grp)
        pix_lay.setContentsMargins(6, 18, 6, 6)
        pix_lay.addWidget(self._pixhawk)
        right.addWidget(pix_grp)

        pres_grp = QGroupBox("PRESSURE SENSOR  —  DEPTH")
        pres_lay = QVBoxLayout(pres_grp)
        pres_lay.setContentsMargins(6, 18, 6, 6)
        pres_lay.addWidget(self._pressure)
        right.addWidget(pres_grp)

        right.setStretchFactor(0, 3)
        right.setStretchFactor(1, 2)
        content.addWidget(right)
        content.setStretchFactor(0, 3)
        content.setStretchFactor(1, 2)

        body = QWidget()
        body_lay = QVBoxLayout(body)
        body_lay.setContentsMargins(10, 10, 10, 4)
        body_lay.addWidget(content)
        root.addWidget(body, 1)

        self._status_bar = self.statusBar()
        self._ros_lbl    = QLabel("  ROS2: initialising…")
        self._ros_lbl.setFont(QFont("Courier New", 9))
        self._ros_lbl.setStyleSheet(f"color:{C['text_mid']};")
        self._status_bar.addPermanentWidget(self._ros_lbl)
        self._log("GUI initialised.")

        # ── Wire up header signals ────────────────────────────────────────────
        self._header.record_start.connect(self._recorder.start)
        self._header.record_stop.connect(self._recorder.stop)
        self._header.yolo_start.connect(self._start_yolo)
        self._header.yolo_stop.connect(self._stop_yolo)

        # ── GStreamer worker ──────────────────────────────────────────────────
        self._gst = GStreamerWorker(port=GST_UDP_PORT)
        self._gst.frame_signal.connect(self._zed.update_frame)
        self._gst.connected_signal.connect(self._zed.set_connected)
        self._gst.log_signal.connect(self._log)
        self._gst.start()

        # ── ROS2 worker ───────────────────────────────────────────────────────
        self._ros = RosWorker()
        self._ros.pixhawk_state_signal.connect(self._on_pixhawk_state)
        self._ros.pixhawk_pwm_signal.connect(self._on_pixhawk_pwm)
        self._ros.depth_signal.connect(self._on_depth)
        self._ros.log_signal.connect(self._log)
        self._ros.start()

    # ── YOLO lifecycle ────────────────────────────────────────────────────────
    @pyqtSlot()
    def _start_yolo(self):
        """Create and start the YOLO worker. Stream is unaffected."""
        if self._yolo_worker is not None:
            return   # already running

        self._log(f"[YOLO] Starting — model: {YOLO_MODEL_PATH}")
        self._zed.set_yolo_active(True)

        self._yolo_worker = YOLOWorker(
            frame_queue=self._gst.yolo_frame_queue,
            model_path=YOLO_MODEL_PATH,
        )
        self._yolo_worker.annotated_frame_signal.connect(self._zed.update_yolo_frame)
        self._yolo_worker.status_signal.connect(self._zed.update_yolo_status)
        self._yolo_worker.log_signal.connect(self._log)
        self._yolo_worker.loading_signal.connect(self._header.set_yolo_loading)
        self._yolo_worker.error_signal.connect(self._on_yolo_error)
        self._yolo_worker.start()

    @pyqtSlot()
    def _stop_yolo(self):
        """Stop the YOLO worker. GStreamer pipeline keeps running normally."""
        if self._yolo_worker is None:
            return

        self._log("[YOLO] Stopping…")
        self._yolo_worker.stop()
        self._yolo_worker = None
        self._zed.set_yolo_active(False)
        self._zed.update_yolo_status("")
        self._log("[YOLO] Stopped. Stream unaffected.")

    @pyqtSlot(str)
    def _on_yolo_error(self, msg: str):
        self._log(f"[YOLO] ERROR: {msg}")
        self._header.set_yolo_error(msg)
        self._zed.set_yolo_active(False)
        self._yolo_worker = None

    # ── ROS / Pixhawk / Depth slots ───────────────────────────────────────────
    @pyqtSlot(bool, bool, bool, str)
    def _on_pixhawk_state(self, connected, armed, guided, mode):
        self._pixhawk.update_state(connected, armed, guided, mode)

    @pyqtSlot(list)
    def _on_pixhawk_pwm(self, channels):
        self._pixhawk.update_pwm(channels)

    @pyqtSlot(float)
    def _on_depth(self, depth_cm: float):
        if depth_cm < 0:
            self._pressure.set_disconnected()
        else:
            self._pressure.update_depth(depth_cm)

    def _log(self, msg: str):
        ts   = datetime.now().strftime("%H:%M:%S")
        full = f"[{ts}]  {msg}"
        print(full)
        self._status_bar.showMessage(full, 8000)
        if "ROS2" in msg or "ros2" in msg.lower():
            self._ros_lbl.setText(f"  {msg[:60]}")

    def closeEvent(self, event):
        self._log("Shutting down…")
        if self._recorder.is_recording():
            self._recorder.stop()
        self._stop_yolo()
        self._gst.stop()
        self._ros.stop()
        event.accept()


# ─────────────────────────────────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────
def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName(APP_TITLE)
    app.setOrganizationName("MarineXperts")

    window = ROVMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()