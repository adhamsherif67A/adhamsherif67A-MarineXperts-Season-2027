#!/usr/bin/env python3
"""
MarineXperts ROV Control Station GUI
PyQt5 + ROS2 (rclpy) Dashboard
Handles: GStreamer H.264 UDP Stream, Pixhawk 2.4.8 via MAVROS, Screen+Mic Recording

GStreamer pipeline (low-latency):
  udpsrc port=5000 → rtph264depay → h264parse → avdec_h264 → videoconvert → appsink
"""

import sys
import os
import time
import subprocess
import signal
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
# FIX #2: Gst.init() must NOT run at module level (before QApplication).
# It is called safely inside GStreamerWorker.run().
try:
    import gi
    gi.require_version("Gst", "1.0")
    from gi.repository import Gst, GLib
    GST_AVAILABLE = True
except Exception as e:
    GST_AVAILABLE = False
    print(f"[WARN] GStreamer (gi) not found – video feed disabled. ({e})")

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

    Priority order (tried at startup, falls back automatically):
      1. NVIDIA NVDEC  — nvh264dec   (requires gstreamer1.0-plugins-bad + CUDA)
      2. VA-API        — vaapih264dec (requires gstreamer1.0-vaapi, AMD/Intel/NVIDIA)
      3. CPU fallback  — avdec_h264  (always available)

    Latency knobs (apply to all backends):
      appsink drop=true max-buffers=1  →  always show newest frame, never queue
      sync=false                       →  skip clock wait, display immediately
      config-interval=-1               →  inline SPS/PPS on every IDR
      udpsrc buffer-size=524288        →  large OS socket buffer
    """

    frame_signal     = pyqtSignal(QImage)
    connected_signal = pyqtSignal(bool)
    log_signal       = pyqtSignal(str)

    # Each backend: (display_name, decoder_element, post_decoder_elements)
    #
    # Desktop NVIDIA (RTX/GTX):
    #   nvh264dec decodes into CUDA memory → cudadownload moves it to system RAM
    #   nvvidconv is Jetson-ONLY and will crash on desktop — do NOT use it
    #
    # AMD / Intel:
    #   vaapih264dec decodes on GPU → vaapipostproc converts YUV on GPU → videoconvert
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
        self._backend  = None   # set after detection

    # ── Build pipeline string for a specific backend ──────────────────────────
    def _build_pipeline(self, decoder: str, post: str) -> str:
        caps = (
            "application/x-rtp,"
            "media=video,"
            "clock-rate=90000,"
            "encoding-name=H264,"
            "payload=96"
        )
        return (
            f'udpsrc port={self._port} buffer-size=524288 caps="{caps}" '
            f'! rtph264depay '
            f'! h264parse config-interval=-1 '
            f'! {decoder} '
            f'{post} '
            f'! video/x-raw,format=RGB '
            f'! appsink name=sink emit-signals=true max-buffers=1 drop=true sync=false'
        )

    # ── Probe which GStreamer elements are actually installed ─────────────────
    @staticmethod
    def _element_exists(name: str) -> bool:
        """Returns True if the GStreamer element factory is registered."""
        # Use gst-inspect via subprocess — avoids any Gst.init() side effects
        result = subprocess.run(
            ["gst-inspect-1.0", "--exists", name.split()[0]],
            capture_output=True,
        )
        return result.returncode == 0

    # ── Detect best available backend at runtime ──────────────────────────────
    def _detect_backend(self) -> tuple:
        for name, decoder, post in self._BACKENDS:
            elem_name = decoder.split()[0]   # first word = element name
            if self._element_exists(elem_name):
                self.log_signal.emit(f"[GST] Decoder selected: {name}  ({elem_name})")
                return name, decoder, post
        # Should never reach here — avdec_h264 is in gstreamer1.0-libav (always present)
        self.log_signal.emit("[GST] WARNING: no suitable decoder found, using CPU fallback.")
        return self._BACKENDS[-1]

    # ── FIX #2: Gst.init() inside thread, after Qt is fully up ───────────────
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

        # Detect GPU backend once, then reuse on every reconnect
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
            # If GPU pipeline fails to parse, automatically retry with CPU
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

        # Watch for first ERROR message — if it happens within 3 s of startup
        # it's likely a GPU driver issue, so we fall back to CPU
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

                # Auto-fallback: if GPU decoder failed, switch to CPU once
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
            # ── Zero-copy path ────────────────────────────────────────────────
            # np.frombuffer creates a VIEW into the GStreamer buffer (no copy).
            # QImage(...).copy() makes exactly ONE copy and owns that memory.
            # Total: 1 copy per frame instead of 2 (bytes() + QImage.copy()).
            frame = np.frombuffer(mapinfo.data, dtype=np.uint8)
            if frame.size < width * height * 3:
                return Gst.FlowReturn.OK

            qi = QImage(
                frame.data,        # memoryview — still mapped here
                width, height,
                width * 3,
                QImage.Format_RGB888,
            ).copy()               # .copy() detaches from the GStreamer buffer
            # Now safe to unmap — QImage owns its own copy
        except Exception as e:
            self.log_signal.emit(f"[GST] Frame convert error: {e}")
            return Gst.FlowReturn.OK
        finally:
            buf.unmap(mapinfo)     # always release GStreamer buffer

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
#  VIDEO PANEL  (receives QImage from GStreamerWorker)
# ─────────────────────────────────────────────────────────────────────────────
class ZedPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._connected = False

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
        self._info  = QLabel(f"UDP port {GST_UDP_PORT}  |  H.264/RTP  |  GStreamer")
        self._info.setFont(QFont("Courier New", 8))
        self._info.setStyleSheet(f"color:{C['text_lo']};")
        status_row.addWidget(self._dot)
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
        pix = QPixmap.fromImage(qi).scaled(
            self._feed.width(),
            self._feed.height(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation,   # faster than SmoothTransformation
        )
        self._feed.setPixmap(pix)


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
    """
    Displays depth received directly from the /depth_cm topic (std_msgs/Float32).
    Value is in centimetres → converted to metres for display.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(8)

        self._dot = StatusDot("Depth Sensor")

        # ── Big depth display ─────────────────────────────────────────────────
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

        # ── Depth bar (0–100 m range) ─────────────────────────────────────────
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

        # ── Raw readings ──────────────────────────────────────────────────────
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

    # ── Public update — called with depth in centimetres ──────────────────────
    def update_depth(self, depth_cm: float):
        """
        depth_cm : value from /depth_cm topic (std_msgs/Float32), unit = cm
        """
        self._dot.set_state("connected")

        depth_m = depth_cm / 100.0   # cm → m

        # Big display
        self._lbl_depth_val.setText(f"{depth_m:6.2f}")

        # Progress bar (capped at 100 m)
        self._depth_bar.setValue(int(min(100, depth_m)))

        # Raw grid
        self._lbl_depth_cm.setText(f"{depth_cm:.1f} cm")
        self._lbl_depth_m.setText(f"{depth_m:.4f} m")

        # Colour zones: green < 10 m, accent 10–50 m, red > 50 m
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
#  ROS2 WORKER  (Pixhawk + Pressure only)
# ─────────────────────────────────────────────────────────────────────────────
class RosWorker(QThread):
    pixhawk_state_signal = pyqtSignal(bool, bool, bool, str)
    pixhawk_pwm_signal   = pyqtSignal(list)
    depth_signal         = pyqtSignal(float)   # depth in centimetres from /depth_cm
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

        # ── /depth_cm  (std_msgs/Float32, value in centimetres) ──────────────
        try:
            from std_msgs.msg import Float32
            self._node.create_subscription(
                Float32, DEPTH_TOPIC, self._on_depth_cm, 10
            )
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
        self.depth_signal.emit(-1.0)   # sentinel: negative = disconnected

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
        """Callback for /depth_cm (std_msgs/Float32). Emits value in cm."""
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
            # Simulate depth oscillating 0–500 cm (0–5 m)
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
#  HEADER
# ─────────────────────────────────────────────────────────────────────────────
class HeaderWidget(QWidget):
    record_start = pyqtSignal()
    record_stop  = pyqtSignal()

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

    def _tick(self):
        now = datetime.now()
        self._lbl_date.setText(now.strftime("%A, %d %B %Y"))
        self._lbl_time.setText(now.strftime("%H:%M:%S"))

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

        self._header.record_start.connect(self._recorder.start)
        self._header.record_stop.connect(self._recorder.stop)

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
        self._gst.stop()
        self._ros.stop()
        event.accept()


# ─────────────────────────────────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────
def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # ── FIX #1: setAttribute MUST come before QApplication() ─────────────────
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
