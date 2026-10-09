#!/usr/bin/env python3
"""
MarineXperts ROV Control Station GUI  —  Modern Edition v4
PyQt5 + ROS2 (rclpy) Dashboard
Handles: GStreamer H.264 UDP Stream, Pixhawk 2.4.8 via MAVROS, Screen+Mic Recording
"""

import sys
import os
import time
import subprocess
import signal
from collections import Counter
from datetime import datetime

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QPushButton, QFrame, QProgressBar,
    QSizePolicy, QGroupBox, QSplitter
)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, pyqtSlot, QSize
from PyQt5.QtGui import QFont, QColor, QPixmap, QPainter, QPen, QImage, QBrush

# ── ROS2 ──────────────────────────────────────────────────────────────────────
try:
    import rclpy
    from rclpy.node import Node
    from rclpy.executors import MultiThreadedExecutor
    ROS2_AVAILABLE = True
except ImportError:
    ROS2_AVAILABLE = False
    print("[WARN] rclpy not found – demo mode.")

# ── MAVROS ────────────────────────────────────────────────────────────────────
try:
    from mavros_msgs.msg import State, RCOut
    MAVROS_MSGS_AVAILABLE = True
except ImportError:
    MAVROS_MSGS_AVAILABLE = False

# ── NumPy ─────────────────────────────────────────────────────────────────────
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False

# ── GStreamer ─────────────────────────────────────────────────────────────────
try:
    import gi
    gi.require_version("Gst", "1.0")
    from gi.repository import Gst, GLib
    GST_AVAILABLE = True
except Exception:
    GST_AVAILABLE = False

# ─────────────────────────────────────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
THRUSTER_COUNT  = 6
PWM_MIN         = 1100
PWM_MAX         = 1900
PWM_NEUTRAL     = 1500
RECONNECT_DELAY = 3.0
APP_TITLE       = "MARINEXPERTS  EXP 07  —  ROV Control Station"
TEAM_NAME       = "MARINEXPERTS  EXP 07"
SUBTITLE        = "ROV CONTROL STATION  ·  ORCA"
LOGO_PATH       = "/home/adham/logomarine.png"

THRUSTER_LABELS = ["T1  FWD-R", "T2  FWD-L", "T3  VRT-FP",
                   "T4  VRT-FS", "T5  LAT-L", "T6  LAT-R"]

DEPTH_TOPIC     = "/depth_cm"
GST_UDP_PORT    = 5000
GST_RECONNECT_S = 4.0

# ─────────────────────────────────────────────────────────────────────────────
#  PALETTE
# ─────────────────────────────────────────────────────────────────────────────
C = {
    "bg_dark":      "#0a0412",
    "bg_panel":     "#110820",
    "bg_card":      "#1a0c30",
    "border":       "#2e1448",
    "border_hi":    "#5a2080",
    "accent":       "#c800ff",
    "accent2":      "#7a00b0",
    "green":        "#00e676",
    "yellow":       "#ffd600",
    "yellow_dim":   "#5a4800",
    "red":          "#ff1744",
    "red_dim":      "#5a0018",
    "text_hi":      "#f0e6ff",
    "text_mid":     "#a06cc0",
    "text_lo":      "#4a2868",
    "thruster_lo":  "#6600aa",
    "thruster_hi":  "#cc00ff",
}

# ─────────────────────────────────────────────────────────────────────────────
#  STYLESHEET
# ─────────────────────────────────────────────────────────────────────────────
STYLESHEET = f"""
QMainWindow, QWidget {{
    background-color: {C['bg_dark']};
    color: {C['text_hi']};
    font-family: 'Courier New', monospace;
}}
QGroupBox {{
    border: 1px solid {C['border']};
    border-radius: 7px;
    margin-top: 16px;
    background-color: {C['bg_panel']};
    font-family: 'Courier New', monospace;
    font-size: 9px;
    font-weight: bold;
    color: {C['accent']};
    letter-spacing: 2px;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 10px;
    top: 0px;
    padding: 2px 8px;
    background-color: {C['bg_dark']};
    border: 1px solid {C['border']};
    border-radius: 3px;
    color: {C['accent']};
}}
QLabel {{ color: {C['text_hi']}; background: transparent; }}
QPushButton {{
    background-color: {C['bg_card']};
    color: {C['accent']};
    border: 1px solid {C['accent2']};
    border-radius: 4px;
    padding: 4px 10px;
    font-family: 'Courier New', monospace;
    font-size: 9px;
    font-weight: bold;
    letter-spacing: 1px;
}}
QPushButton:hover   {{ background-color:{C['accent2']}; color:{C['bg_dark']}; border-color:{C['accent']}; }}
QPushButton:pressed {{ background-color:{C['accent']};  color:{C['bg_dark']}; }}
QPushButton:disabled {{ color:{C['text_lo']}; border-color:{C['text_lo']}; background-color:{C['bg_dark']}; }}
QPushButton#btn_record {{ color:{C['red']};    border-color:{C['red']};    background-color:{C['red_dim']}; }}
QPushButton#btn_record:hover {{ background-color:{C['red']}; color:white; }}
QPushButton#btn_stop   {{ color:{C['yellow']}; border-color:{C['yellow']}; background-color:{C['yellow_dim']}; }}
QPushButton#btn_stop:hover   {{ background-color:{C['yellow']}; color:{C['bg_dark']}; }}
QPushButton#btn_reset_timer {{
    color: {C['text_mid']};
    border-color: {C['border_hi']};
    background-color: {C['bg_dark']};
    border-radius: 3px;
    padding: 1px 6px;
    font-size: 8px;
    letter-spacing: 1px;
}}
QPushButton#btn_reset_timer:hover {{
    background-color: {C['border_hi']};
    color: {C['text_hi']};
    border-color: {C['accent2']};
}}
QPushButton#btn_reset_timer:pressed {{
    background-color: {C['accent2']};
    color: {C['bg_dark']};
}}
QProgressBar {{
    background-color: {C['bg_dark']};
    border: 1px solid {C['border']};
    border-radius: 3px;
    height: 6px;
    text-align: center;
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 {C['thruster_lo']}, stop:1 {C['thruster_hi']});
    border-radius: 3px;
}}
QStatusBar {{
    background-color: {C['bg_panel']};
    color: {C['text_mid']};
    font-size: 9px;
    border-top: 1px solid {C['border']};
}}
QSplitter::handle       {{ background-color:{C['border']}; width:1px; height:1px; }}
QSplitter::handle:hover {{ background-color:{C['accent2']}; }}
"""

# ─────────────────────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def _vsep(h: int = 40) -> QFrame:
    f = QFrame()
    f.setFrameShape(QFrame.VLine)
    f.setFrameShadow(QFrame.Plain)
    f.setFixedSize(1, h)
    f.setStyleSheet(f"background:{C['border']}; border:none;")
    return f


# ─────────────────────────────────────────────────────────────────────────────
#  GSTREAMER WORKER
# ─────────────────────────────────────────────────────────────────────────────
class GStreamerWorker(QThread):
    frame_signal     = pyqtSignal(QImage)
    frame_raw_signal = pyqtSignal(object)
    connected_signal = pyqtSignal(bool)
    log_signal       = pyqtSignal(str)

    _BACKENDS = [
        ("NVIDIA RTX/GTX (nvh264dec)",    "nvh264dec",
         "! cudadownload ! videoconvert"),
        ("VA-API AMD/Intel (vaapih264dec)", "vaapih264dec",
         "! vaapipostproc ! videoconvert"),
        ("CPU fallback (avdec_h264)",
         "avdec_h264 direct-rendering=false max-threads=2", "! videoconvert"),
    ]

    def __init__(self, port: int = GST_UDP_PORT, parent=None):
        super().__init__(parent)
        self._port     = port
        self._running  = False
        self._pipeline = None
        self._backend  = None

    def _build_pipeline(self, decoder, post):
        return (
            f'udpsrc port={self._port} '
            f'caps="application/x-rtp,media=video,encoding-name=H264,payload=96" '
            f'! rtph264depay ! decodebin ! videoconvert '
            f'! video/x-raw,format=RGB '
            f'! appsink name=sink emit-signals=true max-buffers=1 drop=true sync=false'
        )

    @staticmethod
    def _element_exists(name):
        return subprocess.run(
            ["gst-inspect-1.0", "--exists", name.split()[0]],
            capture_output=True).returncode == 0

    def _detect_backend(self):
        for name, decoder, post in self._BACKENDS:
            if self._element_exists(decoder.split()[0]):
                self.log_signal.emit(f"[GST] Decoder: {name}")
                return name, decoder, post
        return self._BACKENDS[-1]

    def run(self):
        self._running = True
        if not (GST_AVAILABLE and NUMPY_AVAILABLE):
            self.connected_signal.emit(False); return
        GLib.threads_init(); Gst.init(None)
        name, decoder, post = self._detect_backend()
        self._backend = name
        while self._running:
            self._run_pipeline(decoder, post)
            if self._running:
                self.connected_signal.emit(False)
                time.sleep(GST_RECONNECT_S)

    def _run_pipeline(self, decoder, post):
        try:
            pipeline = Gst.parse_launch(self._build_pipeline(decoder, post))
        except Exception as e:
            self.log_signal.emit(f"[GST] parse error: {e}"); return
        sink = pipeline.get_by_name("sink")
        if not sink:
            pipeline.set_state(Gst.State.NULL); return
        sink.connect("new-sample", self._on_new_sample)
        pipeline.set_state(Gst.State.PLAYING)
        self._pipeline = pipeline
        bus = pipeline.get_bus(); bus.add_signal_watch()
        first_err = True
        while self._running:
            msg = bus.timed_pop_filtered(
                200 * Gst.MSECOND,
                Gst.MessageType.ERROR | Gst.MessageType.EOS)
            if msg is None: continue
            if msg.type == Gst.MessageType.ERROR:
                err, _ = msg.parse_error()
                self.log_signal.emit(f"[GST] Error: {err.message}")
                if first_err and "avdec" not in decoder:
                    first_err = False
                    pipeline.set_state(Gst.State.NULL); self._pipeline = None
                    _, d, p = self._BACKENDS[-1]; self._backend = "CPU"
                    self._run_pipeline(d, p); return
                break
            if msg.type == Gst.MessageType.EOS: break
        pipeline.set_state(Gst.State.NULL); self._pipeline = None
        self.connected_signal.emit(False)

    def _on_new_sample(self, sink):
        sample = sink.emit("pull-sample")
        if not sample: return Gst.FlowReturn.OK
        buf  = sample.get_buffer()
        st   = sample.get_caps().get_structure(0)
        w, h = st.get_value("width"), st.get_value("height")
        ok, mapinfo = buf.map(Gst.MapFlags.READ)
        if not ok: return Gst.FlowReturn.OK
        try:
            frame = np.frombuffer(mapinfo.data, dtype=np.uint8)
            if frame.size < w * h * 3: return Gst.FlowReturn.OK
            rgb = frame[:w * h * 3].reshape((h, w, 3)).copy()
            self.frame_raw_signal.emit(rgb)
            qi = QImage(rgb.data, w, h, w * 3, QImage.Format_RGB888).copy()
        except Exception as e:
            self.log_signal.emit(f"[GST] Frame error: {e}")
            return Gst.FlowReturn.OK
        finally:
            buf.unmap(mapinfo)
        self.frame_signal.emit(qi); self.connected_signal.emit(True)
        return Gst.FlowReturn.OK

    def stop(self):
        self._running = False
        if self._pipeline:
            try: self._pipeline.set_state(Gst.State.NULL)
            except: pass
        self.quit(); self.wait(3000)


# ─────────────────────────────────────────────────────────────────────────────
#  LOGO WIDGET
# ─────────────────────────────────────────────────────────────────────────────
class LogoWidget(QLabel):
    def __init__(self, size: int = 54, parent=None):
        super().__init__(parent)
        self.setFixedSize(size, size)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background:transparent; border:none;")

        if os.path.exists(LOGO_PATH):
            src    = QPixmap(LOGO_PATH)
            scaled = src.scaled(size, size, Qt.KeepAspectRatio,
                                Qt.SmoothTransformation)
            img    = scaled.toImage().convertToFormat(QImage.Format_ARGB32)
            iw, ih = img.width(), img.height()

            corners = [QColor(img.pixel(0,      0     )),
                       QColor(img.pixel(iw - 1, 0     )),
                       QColor(img.pixel(0,      ih - 1)),
                       QColor(img.pixel(iw - 1, ih - 1))]
            bg_r, bg_g, bg_b = Counter(
                (c.red(), c.green(), c.blue()) for c in corners
            ).most_common(1)[0][0]

            thr = 45
            for x in range(iw):
                for y in range(ih):
                    px = QColor(img.pixel(x, y))
                    d  = ((px.red()   - bg_r) ** 2 +
                          (px.green() - bg_g) ** 2 +
                          (px.blue()  - bg_b) ** 2) ** 0.5
                    if d < thr:
                        img.setPixel(x, y, QColor(0, 0, 0, 0).rgba())
            self.setPixmap(QPixmap.fromImage(img))
        else:
            self._draw_fallback(size)

    def _draw_fallback(self, size):
        pix = QPixmap(size, size); pix.fill(Qt.transparent)
        p = QPainter(pix); p.setRenderHint(QPainter.Antialiasing)
        p.setPen(QPen(QColor(C['accent']), 2)); p.setBrush(QColor(C['bg_card']))
        p.drawEllipse(2, 2, size - 4, size - 4)
        cx = size // 2
        p.drawLine(cx, 8, cx, size - 8)
        p.drawLine(size // 3, size // 3, size * 2 // 3, size // 3)
        p.end(); self.setPixmap(pix)


# ─────────────────────────────────────────────────────────────────────────────
#  SIGNAL BARS
# ─────────────────────────────────────────────────────────────────────────────
class SignalBarsWidget(QWidget):
    def __init__(self, bars: int = 5, parent=None):
        super().__init__(parent)
        self._bars  = bars
        self._level = 3
        self.setFixedSize(bars * 6 + (bars - 1) * 2, 20)

    def set_level(self, level: int):
        self._level = max(0, min(self._bars, level)); self.update()

    def paintEvent(self, _):
        p = QPainter(self); p.setRenderHint(QPainter.Antialiasing)
        bw, gap = 5, 2
        for i in range(self._bars):
            bh = 4 + i * 3
            x  = i * (bw + gap)
            y  = self.height() - bh
            if i < self._level:
                c = QColor(C['accent'])
                c.setAlpha(160 + int(95 * i / max(self._bars - 1, 1)))
            else:
                c = QColor(C['border'])
            p.fillRect(x, y, bw, bh, c)
        p.end()


# ─────────────────────────────────────────────────────────────────────────────
#  STATUS DOT
# ─────────────────────────────────────────────────────────────────────────────
class StatusDot(QWidget):
    _COLORS = {"connected": "green", "disconnected": "red", "warning": "yellow"}

    def __init__(self, label: str, parent=None):
        super().__init__(parent)
        self._state = "disconnected"
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(5)
        lay.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        self._dot = QLabel("●")
        self._dot.setFixedWidth(14)
        self._dot.setFont(QFont("Courier New", 11))
        self._lbl = QLabel(label)
        self._lbl.setFont(QFont("Courier New", 8))
        self._lbl.setStyleSheet(f"color:{C['text_mid']};")

        lay.addWidget(self._dot); lay.addWidget(self._lbl); lay.addStretch()
        self._apply()

    def set_state(self, state: str):
        self._state = state; self._apply()

    def _apply(self):
        key = self._COLORS.get(self._state, "red")
        self._dot.setStyleSheet(f"color:{C[key]}; background:transparent;")


# ─────────────────────────────────────────────────────────────────────────────
#  KPI CELL
# ─────────────────────────────────────────────────────────────────────────────
class KpiCell(QWidget):
    def __init__(self, label: str, unit: str = "", parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            f"background:{C['bg_panel']}; border-right:1px solid {C['border']};")
        lay = QVBoxLayout(self)
        lay.setContentsMargins(14, 0, 14, 0)
        lay.setSpacing(2)
        lay.setAlignment(Qt.AlignVCenter)

        self._key = QLabel(label)
        self._key.setFont(QFont("Courier New", 7, QFont.Bold))
        self._key.setStyleSheet(
            f"color:{C['text_lo']}; letter-spacing:2px; background:transparent;")
        self._key.setFixedHeight(12)

        self._val = QLabel("—")
        self._val.setFont(QFont("Courier New", 17, QFont.Bold))
        self._val.setStyleSheet(f"color:{C['accent']}; background:transparent;")
        self._val.setFixedHeight(22)

        self._unit = QLabel(unit)
        self._unit.setFont(QFont("Courier New", 7))
        self._unit.setStyleSheet(
            f"color:{C['text_mid']}; background:transparent;")
        self._unit.setFixedHeight(11)

        lay.addWidget(self._key); lay.addWidget(self._val); lay.addWidget(self._unit)

    def set_value(self, val: str, color: str = None):
        self._val.setText(val)
        self._val.setStyleSheet(
            f"color:{color or C['accent']}; background:transparent;")


# ─────────────────────────────────────────────────────────────────────────────
#  KPI STRIP  — HEADING removed, only 3 cells: DEPTH · ARMED · VIDEO
# ─────────────────────────────────────────────────────────────────────────────
class KpiStrip(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(64)
        self.setStyleSheet(
            f"background:{C['bg_panel']}; border-bottom:1px solid {C['border']};")
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        self._depth = KpiCell("DEPTH",  "metres")
        self._armed = KpiCell("ARMED",  "pixhawk")
        self._video = KpiCell("VIDEO",  "stream")

        # last cell — no right border
        self._video.setStyleSheet(f"background:{C['bg_panel']};")

        for w in (self._depth, self._armed, self._video):
            lay.addWidget(w, 1)

        self._depth.set_value("—")
        self._armed.set_value("DISARMED", C['red'])
        self._video.set_value("OFFLINE",  C['red'])

    def update_depth(self, m: float):
        col = C['green'] if m < 10 else (C['accent'] if m < 50 else C['red'])
        self._depth.set_value(f"{m:.2f}", col)

    def update_armed(self, armed: bool, connected: bool):
        if connected:
            self._armed.set_value(
                "ARMED" if armed else "DISARMED",
                C['green'] if armed else C['red'])
        else:
            self._armed.set_value("—")

    def update_video(self, ok: bool):
        self._video.set_value(
            "H.264" if ok else "OFFLINE",
            C['green'] if ok else C['red'])


# ─────────────────────────────────────────────────────────────────────────────
#  THRUSTER ROW
# ─────────────────────────────────────────────────────────────────────────────
class ThrusterRow(QWidget):
    _H     = 22
    _LBL_W = 76
    _VAL_W = 38
    _DIR_W = 14

    def __init__(self, index: int, parent=None):
        super().__init__(parent)
        self.setFixedHeight(self._H)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(6)

        self._lbl = QLabel(THRUSTER_LABELS[index])
        self._lbl.setFixedWidth(self._LBL_W); self._lbl.setFixedHeight(self._H)
        self._lbl.setFont(QFont("Courier New", 8))
        self._lbl.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self._lbl.setStyleSheet(f"color:{C['text_lo']}; background:transparent;")

        self._bar = QProgressBar()
        self._bar.setMinimum(0); self._bar.setMaximum(PWM_MAX - PWM_MIN)
        self._bar.setValue(PWM_NEUTRAL - PWM_MIN)
        self._bar.setFormat(""); self._bar.setFixedHeight(6)
        self._bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self._val = QLabel(str(PWM_NEUTRAL))
        self._val.setFixedWidth(self._VAL_W); self._val.setFixedHeight(self._H)
        self._val.setFont(QFont("Courier New", 8, QFont.Bold))
        self._val.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self._val.setStyleSheet(f"color:{C['accent']}; background:transparent;")

        self._dir = QLabel("●")
        self._dir.setFixedWidth(self._DIR_W); self._dir.setFixedHeight(self._H)
        self._dir.setFont(QFont("Courier New", 9))
        self._dir.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self._dir.setStyleSheet(f"color:{C['text_lo']}; background:transparent;")

        lay.addWidget(self._lbl); lay.addWidget(self._bar)
        lay.addWidget(self._val); lay.addWidget(self._dir)

    def update_pwm(self, pwm: int):
        pwm = max(PWM_MIN, min(PWM_MAX, pwm))
        self._bar.setValue(pwm - PWM_MIN)
        self._val.setText(str(pwm))
        delta = pwm - PWM_NEUTRAL
        if abs(delta) < 30:
            self._dir.setStyleSheet(f"color:{C['text_lo']}; background:transparent;")
            self._dir.setText("●")
        elif delta > 0:
            self._dir.setStyleSheet(f"color:{C['green']}; background:transparent;")
            self._dir.setText("▲")
        else:
            self._dir.setStyleSheet(f"color:{C['yellow']}; background:transparent;")
            self._dir.setText("▼")


# ─────────────────────────────────────────────────────────────────────────────
#  VIDEO PANEL
# ─────────────────────────────────────────────────────────────────────────────
class ZedPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._connected = False

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0); root.setSpacing(0)

        self._container = QWidget()
        self._container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._container.setStyleSheet(f"background:{C['bg_dark']};")
        con_lay = QVBoxLayout(self._container)
        con_lay.setContentsMargins(0, 0, 0, 0)

        self._feed = QLabel()
        self._feed.setMinimumSize(320, 200)
        self._feed.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._feed.setAlignment(Qt.AlignCenter)
        self._feed.setStyleSheet(
            f"background:{C['bg_dark']}; border:1px solid {C['border']}; border-radius:4px;")
        con_lay.addWidget(self._feed)
        self._draw_offline()

        _bs = (f"color:{C['text_mid']}; background:rgba(10,4,18,210);"
               f"border:1px solid {C['border']}; border-radius:3px; padding:2px 6px;")
        self._badge_l = QLabel(f"  ZED 2i  ·  H.264  ·  UDP :{GST_UDP_PORT}  ")
        self._badge_l.setFont(QFont("Courier New", 8))
        self._badge_l.setStyleSheet(_bs)
        self._badge_l.setParent(self._container)

        self._badge_r = QLabel("  [C] capture frame  ")
        self._badge_r.setFont(QFont("Courier New", 8))
        self._badge_r.setStyleSheet(
            f"color:{C['text_lo']}; background:rgba(10,4,18,210);"
            f"border:1px solid {C['border']}; border-radius:3px; padding:2px 6px;")
        self._badge_r.setParent(self._container)

        sw = QWidget(); sw.setFixedHeight(26)
        sw.setStyleSheet(
            f"background:{C['bg_panel']}; border-top:1px solid {C['border']};")
        sr = QHBoxLayout(sw); sr.setContentsMargins(8, 0, 8, 0); sr.setSpacing(0)
        self._dot = StatusDot("Video Stream")
        self._backend_lbl = QLabel("GStreamer")
        self._backend_lbl.setFont(QFont("Courier New", 8))
        self._backend_lbl.setStyleSheet(f"color:{C['text_lo']};")
        self._backend_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        sr.addWidget(self._dot, 0, Qt.AlignVCenter)
        sr.addStretch()
        sr.addWidget(self._backend_lbl, 0, Qt.AlignVCenter)

        root.addWidget(self._container, 1)
        root.addWidget(sw, 0)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        cw, ch, m = self._container.width(), self._container.height(), 10
        self._badge_l.adjustSize(); self._badge_r.adjustSize()
        self._badge_l.move(m, ch - self._badge_l.height() - m)
        self._badge_r.move(cw - self._badge_r.width() - m,
                           ch - self._badge_r.height() - m)

    def _draw_offline(self):
        sz  = self._feed.size() if self._feed.width() > 1 else QSize(320, 200)
        pix = QPixmap(sz); pix.fill(QColor(C['bg_dark']))
        p   = QPainter(pix); p.setRenderHint(QPainter.Antialiasing)
        p.setPen(QPen(QColor(C['border']), 1, Qt.DotLine))
        for x in range(0, pix.width(),  40): p.drawLine(x, 0, x, pix.height())
        for y in range(0, pix.height(), 40): p.drawLine(0, y, pix.width(), y)
        cx, cy = pix.width() // 2, pix.height() // 2
        p.setPen(QPen(QColor(C['border_hi']), 1))
        p.drawLine(cx - 24, cy, cx + 24, cy)
        p.drawLine(cx, cy - 24, cx, cy + 24)
        p.drawEllipse(cx - 16, cy - 16, 32, 32)
        p.setPen(QColor(C['text_lo']))
        p.setFont(QFont("Courier New", 12, QFont.Bold))
        p.drawText(pix.rect(), Qt.AlignCenter,
                   f"NO SIGNAL\n\nWaiting for H.264 stream\nUDP :{GST_UDP_PORT}")
        p.end(); self._feed.setPixmap(pix)

    @pyqtSlot(bool)
    def set_connected(self, ok: bool):
        self._connected = ok
        self._dot.set_state("connected" if ok else "disconnected")
        if not ok: self._draw_offline()

    @pyqtSlot(QImage)
    def update_frame(self, qi: QImage):
        pix = QPixmap.fromImage(qi).scaled(
            self._feed.width(), self._feed.height(),
            Qt.KeepAspectRatio, Qt.FastTransformation)
        self._feed.setPixmap(pix)


# ─────────────────────────────────────────────────────────────────────────────
#  FC CHIP
# ─────────────────────────────────────────────────────────────────────────────
class FcChip(QWidget):
    def __init__(self, label: str, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(48)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet(
            f"background:{C['bg_card']}; border:1px solid {C['border']}; border-radius:6px;")
        lay = QVBoxLayout(self)
        lay.setContentsMargins(10, 6, 10, 6); lay.setSpacing(4)
        lay.setAlignment(Qt.AlignVCenter)

        self._key = QLabel(label)
        self._key.setFont(QFont("Courier New", 7, QFont.Bold))
        self._key.setFixedHeight(11)
        self._key.setStyleSheet(
            f"color:{C['text_lo']}; letter-spacing:1px; background:transparent;")

        self._val = QLabel("—")
        self._val.setFont(QFont("Courier New", 11, QFont.Bold))
        self._val.setFixedHeight(16)
        self._val.setStyleSheet(f"color:{C['accent']}; background:transparent;")

        lay.addWidget(self._key); lay.addWidget(self._val)

    def set_value(self, txt: str, color: str = None):
        self._val.setText(txt)
        self._val.setStyleSheet(
            f"color:{color or C['accent']}; background:transparent;")


# ─────────────────────────────────────────────────────────────────────────────
#  PIXHAWK PANEL
# ─────────────────────────────────────────────────────────────────────────────
class PixhawkPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(8, 6, 8, 6); lay.setSpacing(8)

        chip_row = QHBoxLayout()
        chip_row.setSpacing(6); chip_row.setContentsMargins(0, 0, 0, 0)
        self._chip_mode   = FcChip("MODE")
        self._chip_armed  = FcChip("ARMED")
        self._chip_mavros = FcChip("MAVROS")
        for c in (self._chip_mode, self._chip_armed, self._chip_mavros):
            chip_row.addWidget(c)

        thr_box = QGroupBox("THRUSTER PWM  (µs)")
        thr_lay = QVBoxLayout(thr_box)
        thr_lay.setContentsMargins(8, 18, 8, 6); thr_lay.setSpacing(2)

        self._rows: list = []
        for i in range(THRUSTER_COUNT):
            r = ThrusterRow(i); self._rows.append(r); thr_lay.addWidget(r)

        legend = QHBoxLayout()
        legend.setContentsMargins(0, 3, 0, 0); legend.setSpacing(6)
        sp = QLabel(); sp.setFixedWidth(ThrusterRow._LBL_W); legend.addWidget(sp)
        for txt, align in [("1100", Qt.AlignLeft | Qt.AlignVCenter),
                            ("NEUTRAL  1500", Qt.AlignCenter),
                            ("1900", Qt.AlignRight | Qt.AlignVCenter)]:
            l = QLabel(txt); l.setFont(QFont("Courier New", 7))
            l.setAlignment(align)
            l.setStyleSheet(f"color:{C['text_lo']}; background:transparent;")
            legend.addWidget(l, 1)
        sp2 = QLabel()
        sp2.setFixedWidth(ThrusterRow._VAL_W + 6 + ThrusterRow._DIR_W)
        legend.addWidget(sp2)
        thr_lay.addLayout(legend)

        lay.addLayout(chip_row); lay.addWidget(thr_box, 1)

    def update_state(self, connected, armed, guided, mode, **_):
        self._chip_mavros.set_value(
            "● CONNECTED" if connected else "● OFFLINE",
            C['green'] if connected else C['red'])
        self._chip_mode.set_value(mode or "UNKNOWN")
        self._chip_armed.set_value(
            ("● ARMED" if armed else "○ DISARMED") if connected else "—",
            (C['green'] if armed else C['red']) if connected else C['text_lo'])

    def update_pwm(self, channels: list):
        for i, pwm in enumerate(channels[:THRUSTER_COUNT]):
            self._rows[i].update_pwm(pwm)


# ─────────────────────────────────────────────────────────────────────────────
#  PRESSURE / DEPTH PANEL
# ─────────────────────────────────────────────────────────────────────────────
class PressurePanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(8, 6, 8, 6); lay.setSpacing(6)

        self._dot = StatusDot("Depth Sensor")

        depth_row = QHBoxLayout()
        depth_row.setSpacing(8); depth_row.setAlignment(Qt.AlignVCenter)

        icon = QLabel("▼")
        icon.setFont(QFont("Courier New", 20, QFont.Bold))
        icon.setFixedWidth(24); icon.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        icon.setStyleSheet(f"color:{C['accent2']}; background:transparent;")

        vb = QVBoxLayout(); vb.setSpacing(0); vb.setAlignment(Qt.AlignVCenter)
        self._lbl_val = QLabel("—")
        self._lbl_val.setFont(QFont("Courier New", 30, QFont.Bold))
        self._lbl_val.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self._lbl_val.setStyleSheet(f"color:{C['accent']}; background:transparent;")
        self._lbl_unit = QLabel("metres depth")
        self._lbl_unit.setFont(QFont("Courier New", 8))
        self._lbl_unit.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self._lbl_unit.setStyleSheet(f"color:{C['text_lo']}; background:transparent;")
        vb.addWidget(self._lbl_val); vb.addWidget(self._lbl_unit)

        depth_row.addWidget(icon); depth_row.addLayout(vb); depth_row.addStretch()

        self._bar = QProgressBar()
        self._bar.setRange(0, 100); self._bar.setValue(0)
        self._bar.setFormat(""); self._bar.setFixedHeight(7)
        self._bar.setStyleSheet(
            f"QProgressBar {{ background:{C['bg_dark']}; border:1px solid {C['border']}; border-radius:3px; }}"
            f"QProgressBar::chunk {{ background:qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"stop:0 {C['thruster_lo']},stop:1 {C['accent']}); border-radius:3px; }}"
        )

        scale = QHBoxLayout(); scale.setContentsMargins(0, 0, 0, 0)
        for txt, align in [("0 m", Qt.AlignLeft),
                            ("50 m", Qt.AlignCenter),
                            ("100 m", Qt.AlignRight)]:
            l = QLabel(txt); l.setAlignment(align)
            l.setFont(QFont("Courier New", 7))
            l.setStyleSheet(f"color:{C['text_lo']}; background:transparent;")
            scale.addWidget(l, 1)

        raw_box = QGroupBox("RAW READINGS")
        raw_lay = QGridLayout(raw_box)
        raw_lay.setContentsMargins(8, 18, 8, 8)
        raw_lay.setHorizontalSpacing(12); raw_lay.setVerticalSpacing(5)

        def kv(label, row):
            k = QLabel(label); k.setFont(QFont("Courier New", 8))
            k.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
            k.setStyleSheet(f"color:{C['text_lo']}; background:transparent;")
            v = QLabel("—"); v.setFont(QFont("Courier New", 9, QFont.Bold))
            v.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
            v.setStyleSheet(f"color:{C['accent']}; background:transparent;")
            raw_lay.addWidget(k, row, 0); raw_lay.addWidget(v, row, 1)
            return v

        self._lbl_cm    = kv("DEPTH (cm) :", 0)
        self._lbl_m     = kv("DEPTH (m)  :", 1)
        self._lbl_topic = kv("TOPIC      :", 2)
        self._lbl_topic.setText(DEPTH_TOPIC)
        self._lbl_topic.setStyleSheet(
            f"color:{C['text_lo']}; font-size:8px; background:transparent;")
        raw_lay.setColumnStretch(1, 1)

        lay.addWidget(self._dot)
        lay.addLayout(depth_row)
        lay.addWidget(self._bar)
        lay.addLayout(scale)
        lay.addWidget(raw_box)
        lay.addStretch()

    def update_depth(self, depth_cm: float):
        self._dot.set_state("connected")
        m = depth_cm / 100.0
        self._lbl_val.setText(f"{m:.2f}")
        self._bar.setValue(int(min(100, m)))
        self._lbl_cm.setText(f"{depth_cm:.1f}")
        self._lbl_m.setText(f"{m:.4f}")
        col = C['green'] if m < 10 else (C['accent'] if m < 50 else C['red'])
        self._lbl_val.setStyleSheet(f"color:{col}; background:transparent;")

    def set_disconnected(self):
        self._dot.set_state("disconnected")
        for l in (self._lbl_val, self._lbl_cm, self._lbl_m): l.setText("—")
        self._bar.setValue(0)


# ─────────────────────────────────────────────────────────────────────────────
#  RECORDING MANAGER
# ─────────────────────────────────────────────────────────────────────────────
class RecordingManager:
    def __init__(self, status_callback=None):
        self._proc = None
        self._cb   = status_callback or (lambda m: None)
        self._file = ""

    def is_recording(self):
        return self._proc is not None and self._proc.poll() is None

    def start(self):
        if self.is_recording(): return
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._file = os.path.expanduser(f"~/rov_recording_{ts}.mp4")
        cmd = self._build_cmd(self._file)
        if not cmd: self._cb("[REC] ffmpeg not found."); return
        try:
            self._proc = subprocess.Popen(
                cmd, stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self._cb(f"[REC] Recording → {self._file}")
        except Exception as e:
            self._cb(f"[REC] Failed: {e}"); self._proc = None

    def stop(self):
        if not self.is_recording(): return
        try:
            self._proc.stdin.write(b"q\n"); self._proc.stdin.flush()
            self._proc.wait(timeout=5)
        except Exception:
            self._proc.kill()
        self._cb(f"[REC] Saved → {self._file}"); self._proc = None

    def _build_cmd(self, outfile):
        if subprocess.run(["which", "ffmpeg"], capture_output=True).returncode != 0:
            return None
        return ["ffmpeg", "-y",
                "-f", "x11grab", "-r", "30", "-i", os.environ.get("DISPLAY", ":0.0"),
                "-f", "pulse", "-i", "default",
                "-c:v", "libx264", "-preset", "ultrafast",
                "-c:a", "aac", "-b:a", "128k", outfile]


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
        self._running = False; self._node = None; self._executor = None

    def run(self):
        self._running = True
        self.log_signal.emit("[ROS2] Worker thread started.")
        if not ROS2_AVAILABLE:
            self.log_signal.emit("[ROS2] rclpy unavailable – demo mode.")
            self._demo_loop(); return
        try: rclpy.init()
        except Exception as e:
            self.log_signal.emit(f"[ROS2] Init failed: {e}")
            self._demo_loop(); return
        while self._running:
            try:
                self._create_node()
                self.log_signal.emit("[ROS2] Node created, spinning…")
                self._executor.spin()
            except Exception as e:
                self.log_signal.emit(
                    f"[ROS2] Error: {e} — retrying in {RECONNECT_DELAY}s")
                self._cleanup_node(); self._emit_disconnected()
                time.sleep(RECONNECT_DELAY)
        self._cleanup_node()
        try: rclpy.shutdown()
        except: pass

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
            if self._executor: self._executor.shutdown(timeout_sec=1)
            if self._node:     self._node.destroy_node()
        except: pass
        self._node = self._executor = None

    def _emit_disconnected(self):
        self.pixhawk_state_signal.emit(False, False, False, "—")
        self.depth_signal.emit(-1.0)

    def _on_state(self, msg):
        try: self.pixhawk_state_signal.emit(
            msg.connected, msg.armed, msg.guided, msg.mode)
        except Exception as e: self.log_signal.emit(f"[PIX] State error: {e}")

    def _on_rcout(self, msg):
        try:
            ch = list(msg.channels[:THRUSTER_COUNT])
            while len(ch) < THRUSTER_COUNT: ch.append(PWM_NEUTRAL)
            self.pixhawk_pwm_signal.emit(ch)
        except Exception as e: self.log_signal.emit(f"[PIX] RCOut error: {e}")

    def _on_depth_cm(self, msg):
        try: self.depth_signal.emit(float(msg.data))
        except Exception as e: self.log_signal.emit(f"[DEPTH] error: {e}")

    def _demo_loop(self):
        import math; t = 0.0
        while self._running:
            t += 0.1
            pwms = [int(PWM_NEUTRAL + 150 * math.sin(t + i * 0.8))
                    for i in range(THRUSTER_COUNT)]
            self.pixhawk_state_signal.emit(True, False, True, "STABILIZE")
            self.pixhawk_pwm_signal.emit(pwms)
            self.depth_signal.emit(500.0 * (0.5 + 0.5 * math.sin(t * 0.3)))
            time.sleep(0.1)

    def stop(self):
        self._running = False
        if self._executor:
            try: self._executor.shutdown(timeout_sec=1)
            except: pass
        self.quit(); self.wait(3000)


# ─────────────────────────────────────────────────────────────────────────────
#  HEADER
#  • Mission timer has a small ↺ RESET button beneath the digits
#  • No HEADING section anywhere
# ─────────────────────────────────────────────────────────────────────────────
class HeaderWidget(QWidget):
    record_start = pyqtSignal()
    record_stop  = pyqtSignal()
    _H = 70

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(self._H)
        self.setStyleSheet(
            f"background:qlineargradient(x1:0,y1:0,x2:1,y2:0,"
            f"stop:0 {C['bg_panel']},stop:0.45 {C['bg_card']},stop:1 {C['bg_panel']});"
            f"border-bottom:1px solid {C['border']};"
        )
        lay = QHBoxLayout(self)
        lay.setContentsMargins(14, 0, 14, 0)
        lay.setSpacing(0)

        # ── logo ──────────────────────────────────────────────────────────
        lay.addWidget(LogoWidget(54), 0, Qt.AlignVCenter)
        lay.addSpacing(10)

        # ── team name ─────────────────────────────────────────────────────
        nw = QWidget(); nw.setStyleSheet("background:transparent;")
        nl = QVBoxLayout(nw)
        nl.setContentsMargins(0, 0, 0, 0); nl.setSpacing(3)
        nl.setAlignment(Qt.AlignVCenter)
        t = QLabel(TEAM_NAME)
        t.setFont(QFont("Courier New", 13, QFont.Bold))
        t.setStyleSheet(f"color:{C['accent']}; letter-spacing:3px;")
        s = QLabel(SUBTITLE)
        s.setFont(QFont("Courier New", 8))
        s.setStyleSheet(f"color:{C['text_mid']}; letter-spacing:2px;")
        nl.addWidget(t); nl.addWidget(s)
        lay.addWidget(nw, 0, Qt.AlignVCenter)
        lay.addStretch(1)

        # ── tether signal bars ────────────────────────────────────────────
        sw = QWidget(); sw.setStyleSheet("background:transparent;")
        sl = QVBoxLayout(sw)
        sl.setContentsMargins(0, 0, 0, 0); sl.setSpacing(3)
        sl.setAlignment(Qt.AlignCenter)
        self._signal_bars = SignalBarsWidget(5)
        sig_lbl = QLabel("TETHER")
        sig_lbl.setFont(QFont("Courier New", 7))
        sig_lbl.setAlignment(Qt.AlignCenter)
        sig_lbl.setStyleSheet(f"color:{C['text_lo']}; letter-spacing:1px;")
        sl.addWidget(self._signal_bars, 0, Qt.AlignCenter)
        sl.addWidget(sig_lbl, 0, Qt.AlignCenter)
        lay.addWidget(sw, 0, Qt.AlignVCenter)

        lay.addSpacing(12)
        lay.addWidget(_vsep(40), 0, Qt.AlignVCenter)
        lay.addSpacing(12)

        # ── mission elapsed timer  +  ↺ RESET button ─────────────────────
        mw = QWidget(); mw.setStyleSheet("background:transparent;")
        ml = QVBoxLayout(mw)
        ml.setContentsMargins(0, 0, 0, 0); ml.setSpacing(1)
        ml.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        # top label
        ml_lbl = QLabel("MISSION ELAPSED")
        ml_lbl.setFont(QFont("Courier New", 7, QFont.Bold))
        ml_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        ml_lbl.setStyleSheet(f"color:{C['text_lo']}; letter-spacing:2px;")
        ml_lbl.setFixedHeight(11)

        # timer digits
        self._lbl_mission = QLabel("00:00:00")
        self._lbl_mission.setFont(QFont("Courier New", 20, QFont.Bold))
        self._lbl_mission.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._lbl_mission.setStyleSheet(
            f"color:{C['accent']}; letter-spacing:2px;")
        self._lbl_mission.setFixedHeight(26)

        # reset button — sits right-aligned below the digits
        self._btn_reset = QPushButton("↺  RESET")
        self._btn_reset.setObjectName("btn_reset_timer")
        self._btn_reset.setFixedHeight(16)
        self._btn_reset.setFixedWidth(80)
        self._btn_reset.setCursor(Qt.PointingHandCursor)
        self._btn_reset.clicked.connect(self._reset_timer)

        ml.addWidget(ml_lbl)
        ml.addWidget(self._lbl_mission)
        ml.addWidget(self._btn_reset, 0, Qt.AlignRight)
        lay.addWidget(mw, 0, Qt.AlignVCenter)

        lay.addSpacing(12)
        lay.addWidget(_vsep(40), 0, Qt.AlignVCenter)
        lay.addSpacing(12)

        # ── wall clock ────────────────────────────────────────────────────
        cw = QWidget(); cw.setStyleSheet("background:transparent;")
        cl = QVBoxLayout(cw)
        cl.setContentsMargins(0, 0, 0, 0); cl.setSpacing(2)
        cl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self._lbl_date = QLabel()
        self._lbl_date.setFont(QFont("Courier New", 7))
        self._lbl_date.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._lbl_date.setStyleSheet(f"color:{C['text_mid']};")
        self._lbl_time = QLabel()
        self._lbl_time.setFont(QFont("Courier New", 15, QFont.Bold))
        self._lbl_time.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._lbl_time.setStyleSheet(f"color:{C['text_hi']}; letter-spacing:1px;")
        cl.addWidget(self._lbl_date); cl.addWidget(self._lbl_time)
        lay.addWidget(cw, 0, Qt.AlignVCenter)

        lay.addSpacing(12)
        lay.addWidget(_vsep(40), 0, Qt.AlignVCenter)
        lay.addSpacing(12)

        # ── REC / STOP ────────────────────────────────────────────────────
        rw = QWidget(); rw.setStyleSheet("background:transparent;")
        rl = QVBoxLayout(rw)
        rl.setContentsMargins(0, 0, 0, 0); rl.setSpacing(4)
        rl.setAlignment(Qt.AlignVCenter)
        self._btn_rec = QPushButton("⏺  REC")
        self._btn_rec.setObjectName("btn_record")
        self._btn_rec.setFixedWidth(96); self._btn_rec.setFixedHeight(24)
        self._btn_stop = QPushButton("⏹  STOP")
        self._btn_stop.setObjectName("btn_stop")
        self._btn_stop.setFixedWidth(96); self._btn_stop.setFixedHeight(24)
        self._btn_stop.setEnabled(False)
        self._lbl_rec = QLabel("● IDLE")
        self._lbl_rec.setFont(QFont("Courier New", 8))
        self._lbl_rec.setAlignment(Qt.AlignCenter)
        self._lbl_rec.setFixedHeight(12)
        self._lbl_rec.setStyleSheet(f"color:{C['text_lo']};")
        self._btn_rec.clicked.connect(self._on_rec)
        self._btn_stop.clicked.connect(self._on_stop)
        rl.addWidget(self._btn_rec,  0, Qt.AlignCenter)
        rl.addWidget(self._btn_stop, 0, Qt.AlignCenter)
        rl.addWidget(self._lbl_rec,  0, Qt.AlignCenter)
        lay.addWidget(rw, 0, Qt.AlignVCenter)

        # ── timers ────────────────────────────────────────────────────────
        self._clock = QTimer(self); self._clock.timeout.connect(self._tick)
        self._clock.start(500); self._tick()

        self._mission_secs  = 0
        self._mission_timer = QTimer(self)
        self._mission_timer.timeout.connect(self._mission_tick)
        self._mission_timer.start(1000)

        self._blink       = False
        self._blink_timer = QTimer(self)
        self._blink_timer.timeout.connect(self._blink_tick)

    # ── clock ─────────────────────────────────────────────────────────────────
    def _tick(self):
        now = datetime.now()
        self._lbl_date.setText(now.strftime("%A, %d %B %Y"))
        self._lbl_time.setText(now.strftime("%H:%M:%S"))

    def _mission_tick(self):
        self._mission_secs += 1
        self._refresh_mission_display()

    def _refresh_mission_display(self):
        h = self._mission_secs // 3600
        m = (self._mission_secs % 3600) // 60
        s = self._mission_secs % 60
        self._lbl_mission.setText(f"{h:02d}:{m:02d}:{s:02d}")

    def _reset_timer(self):
        """Reset mission elapsed timer back to 00:00:00."""
        self._mission_secs = 0
        self._refresh_mission_display()
        # brief visual flash to confirm reset
        self._lbl_mission.setStyleSheet(
            f"color:{C['green']}; letter-spacing:2px;")
        QTimer.singleShot(300, lambda: self._lbl_mission.setStyleSheet(
            f"color:{C['accent']}; letter-spacing:2px;"))

    def set_signal_level(self, level: int):
        self._signal_bars.set_level(level)

    # ── REC handlers ──────────────────────────────────────────────────────────
    def _on_rec(self):
        self._btn_rec.setEnabled(False); self._btn_stop.setEnabled(True)
        self._lbl_rec.setStyleSheet(f"color:{C['red']};")
        self._lbl_rec.setText("● REC")
        self._blink_timer.start(800); self.record_start.emit()

    def _on_stop(self):
        self._btn_rec.setEnabled(True); self._btn_stop.setEnabled(False)
        self._lbl_rec.setStyleSheet(f"color:{C['text_lo']};")
        self._lbl_rec.setText("● IDLE")
        self._blink_timer.stop(); self.record_stop.emit()

    def _blink_tick(self):
        self._blink = not self._blink
        self._lbl_rec.setStyleSheet(
            f"color:{C['red'] if self._blink else C['text_lo']};")
        self._lbl_rec.setText("● REC" if self._blink else "○ REC")


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN WINDOW
# ─────────────────────────────────────────────────────────────────────────────
class ROVMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.setMinimumSize(1200, 720)
        self.setStyleSheet(STYLESHEET)

        self._header   = HeaderWidget()
        self._kpi      = KpiStrip()
        self._zed      = ZedPanel()
        self._pixhawk  = PixhawkPanel()
        self._pressure = PressurePanel()
        self._recorder = RecordingManager(status_callback=self._log)
        self._last_frame = None

        central = QWidget(); self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0); root.setSpacing(0)
        root.addWidget(self._header)
        root.addWidget(self._kpi)

        h_split = QSplitter(Qt.Horizontal); h_split.setHandleWidth(1)

        zg = QGroupBox("H.264 UDP STREAM  —  GStreamer  ·  ZED 2i")
        zl = QVBoxLayout(zg); zl.setContentsMargins(4, 18, 4, 4)
        zl.addWidget(self._zed)
        h_split.addWidget(zg)

        v_split = QSplitter(Qt.Vertical); v_split.setHandleWidth(1)

        pg = QGroupBox("PIXHAWK 2.4.8  —  MAVROS")
        pl = QVBoxLayout(pg); pl.setContentsMargins(4, 18, 4, 4)
        pl.addWidget(self._pixhawk)
        v_split.addWidget(pg)

        dg = QGroupBox("PRESSURE SENSOR  —  DEPTH")
        dl = QVBoxLayout(dg); dl.setContentsMargins(4, 18, 4, 4)
        dl.addWidget(self._pressure)
        v_split.addWidget(dg)

        v_split.setStretchFactor(0, 4); v_split.setStretchFactor(1, 3)
        h_split.addWidget(v_split)
        h_split.setStretchFactor(0, 3); h_split.setStretchFactor(1, 2)

        body = QWidget()
        bl = QVBoxLayout(body); bl.setContentsMargins(8, 8, 8, 0); bl.setSpacing(0)
        bl.addWidget(h_split)
        root.addWidget(body, 1)

        self._status_bar = self.statusBar()
        self._ros_lbl = QLabel("  ROS2: initialising…")
        self._ros_lbl.setFont(QFont("Courier New", 9))
        self._ros_lbl.setStyleSheet(f"color:{C['text_mid']};")
        self._shortcut_lbl = QLabel("  [C] capture  ·  [R] record  ·  [S] stop  ")
        self._shortcut_lbl.setFont(QFont("Courier New", 9))
        self._shortcut_lbl.setStyleSheet(f"color:{C['text_lo']};")
        self._status_bar.addPermanentWidget(self._ros_lbl)
        self._status_bar.addPermanentWidget(self._shortcut_lbl)
        self._log("GUI initialised — MARINE XPERTS EXP 07.")

        self._header.record_start.connect(self._recorder.start)
        self._header.record_stop.connect(self._recorder.stop)

        self._gst = GStreamerWorker(port=GST_UDP_PORT)
        self._gst.frame_signal.connect(self._zed.update_frame)
        self._gst.frame_raw_signal.connect(self._on_raw_frame)
        self._gst.connected_signal.connect(self._on_video_connected)
        self._gst.log_signal.connect(self._log)
        self._gst.start()

        self._ros = RosWorker()
        self._ros.pixhawk_state_signal.connect(self._on_pixhawk_state)
        self._ros.pixhawk_pwm_signal.connect(self._on_pixhawk_pwm)
        self._ros.depth_signal.connect(self._on_depth)
        self._ros.log_signal.connect(self._log)
        self._ros.start()

    @pyqtSlot(bool)
    def _on_video_connected(self, ok):
        self._zed.set_connected(ok); self._kpi.update_video(ok)

    @pyqtSlot(bool, bool, bool, str)
    def _on_pixhawk_state(self, connected, armed, guided, mode):
        self._pixhawk.update_state(connected, armed, guided, mode)
        self._kpi.update_armed(armed, connected)

    @pyqtSlot(list)
    def _on_pixhawk_pwm(self, channels):
        self._pixhawk.update_pwm(channels)

    @pyqtSlot(float)
    def _on_depth(self, depth_cm):
        if depth_cm < 0: self._pressure.set_disconnected()
        else:
            self._pressure.update_depth(depth_cm)
            self._kpi.update_depth(depth_cm / 100.0)

    @pyqtSlot(object)
    def _on_raw_frame(self, frame): self._last_frame = frame

    def keyPressEvent(self, event):
        k = event.key()
        if k == Qt.Key_C and self._last_frame is not None: self._capture_frame()
        elif k == Qt.Key_R and not self._recorder.is_recording(): self._recorder.start()
        elif k == Qt.Key_S and self._recorder.is_recording():     self._recorder.stop()
        super().keyPressEvent(event)

    def _capture_frame(self):
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        path = f"/media/adham/ESD-ISO/rov_capture_{ts}.png"
        try:
            import cv2
            bgr = cv2.cvtColor(self._last_frame, cv2.COLOR_RGB2BGR)
            self._log(f"[CAPTURE] Saved → {path}" if cv2.imwrite(path, bgr)
                      else f"[CAPTURE] Failed to write {path}")
        except ImportError:
            self._log("[CAPTURE] pip install opencv-python")
        except Exception as e:
            self._log(f"[CAPTURE] Error: {e}")

    def _log(self, msg):
        full = f"[{datetime.now().strftime('%H:%M:%S')}]  {msg}"
        print(full)
        self._status_bar.showMessage(full, 8000)
        if "ROS2" in msg or "ros2" in msg.lower():
            self._ros_lbl.setText(f"  {msg[:60]}")

    def closeEvent(self, event):
        self._log("Shutting down…")
        if self._recorder.is_recording(): self._recorder.stop()
        self._gst.stop(); self._ros.stop()
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

