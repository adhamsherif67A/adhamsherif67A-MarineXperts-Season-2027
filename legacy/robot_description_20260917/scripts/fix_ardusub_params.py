#!/usr/bin/env python3
"""
Fix ArduSub SITL parameters so thrusters stop cleanly after motion and on disarm.

Run with MAVROS active:
    python3 /home/boda/mako_ws/src/robot_description/scripts/fix_ardusub_params.py
"""

import subprocess
import time
import sys

# Parameters to set for clean thruster stop on neutral stick / disarm:
PARAMS = {
    # ── EKF3 STATE ESTIMATION ───────────────────────────────────────────────
    # Gazebo's air-pressure sensor is atmospheric, not hydrostatic, and its
    # value is invalid for an underwater vehicle.  The launch file relays
    # Gazebo odometry to /mavros/odometry/in; source 6 makes EKF3 use that
    # MAVLink ExternalNav stream for a consistent XYZ pose, velocity, and yaw.
    "EK3_SRC1_POSXY":  6.0,
    "EK3_SRC1_POSZ":   6.0,
    "EK3_SRC1_VELXY":  6.0,
    "EK3_SRC1_VELZ":   6.0,
    "EK3_SRC1_YAW":    6.0,

    # ── THRUSTER SPIN-ARM (KEY FIX) ──────────────────────────────────────────
    # T200 thrusters are bidirectional – no minimum spin needed when armed.
    # Without this, ArduSub commands ~10% thrust (PWM ~1580) on ALL motors
    # when armed at neutral stick, which shakes the model.
    "MOT_SPIN_ARM":     0.0,   # was 0.1 → thrusters now spin only when commanded

    # ── MINIMUM SPIN FLOOR ────────────────────────────────────────────────────
    # Also zero for the same reason (T200 works from 0 thrust bidirectionally).
    "MOT_SPIN_MIN":     0.0,   # was 0.15 → no forced minimum spin

    # ── DISARM BEHAVIOR ───────────────────────────────────────────────────────
    # 0 = on disarm, ArduSub outputs 1500 µs (neutral = 0 N with our deadband)
    # 1 = on disarm, outputs MOT_PWM_MIN (1100 µs) which is max reverse thrust!
    "MOT_SAFE_DISARM":  0.0,   # keep 0 (already correct in mav.parm)

    # ── SPOOL TIME ────────────────────────────────────────────────────────────
    # T200 electronic speed controllers have no spin-up spool time.
    # Keeping 0.5s spool means thrusters ramp up slowly, giving the impression
    # of momentum after a command – looks like they keep spinning.
    "MOT_SPOOL_TIME":   0.0,   # was 0.5s → instant response like real T200

    # ── GCS FAILSAFE ──────────────────────────────────────────────────────────
    # In simulation, MAVROS connection can lag. With FS_GCS_ENABLE=2, ArduSub
    # activates "hold position" failsafe after 5s of no heartbeat, which issues
    # non-zero thrust commands to maintain depth. This looks like motors spinning.
    "FS_GCS_ENABLE":    0.0,   # was 2 → disable in simulation

    # ── PILOT FAILSAFE TIMEOUT ────────────────────────────────────────────────
    "FS_PILOT_TIMEOUT": 10.0,  # was 3s → increase for simulation

    # ── THROTTLE DEADZONE ─────────────────────────────────────────────────────
    # Keep at 100: this 100-µs deadzone around 1500 µs matches the Gazebo
    # thruster deadband of 0.5 N. At neutral stick, PWM stays in [1400,1600].
    "THR_DZ":          100.0,  # keep as-is
}


def set_param(name, value):
    svc_cmd = [
        "ros2", "service", "call",
        "/mavros/param/set",
        "mavros_msgs/srv/ParamSetV2",
        f"{{param_id: '{name}', value: {{double_value: {value}}}}}"
    ]
    try:
        result = subprocess.run(svc_cmd, capture_output=True, text=True, timeout=15)
        if result.returncode == 0 and "success=True" in result.stdout:
            print(f"  OK   {name:30s} = {value}")
            return True
        else:
            print(f"  FAIL {name:30s} = {value}")
            if result.stderr:
                print(f"       {result.stderr.strip()[:80]}")
            return False
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT {name}")
        return False


def main():
    print("=" * 60)
    print("  ArduSub SITL Parameter Fix - Clean Thruster Stop")
    print("=" * 60)
    print()
    print("Prerequisites:")
    print("  1. Gazebo + SITL running: ros2 launch robot_description gazebo.launch.py")
    print("  2. MAVROS running: ros2 launch mavros apm.launch fcu_url:=udp://127.0.0.1:14551@")
    print()
    print("Press ENTER to apply parameters (Ctrl-C to abort)...")
    try:
        input()
    except KeyboardInterrupt:
        print("Aborted.")
        sys.exit(0)

    print()
    ok = fail = 0
    for name, value in PARAMS.items():
        if set_param(name, value):
            ok += 1
        else:
            fail += 1
        time.sleep(0.3)

    print()
    print(f"Done: {ok} OK, {fail} failed.")
    print()
    if fail > 0:
        print("For failed params, set manually via MAVProxy:")
        print("  param set MOT_SPIN_ARM 0")
        print("  param set MOT_SPIN_MIN 0")
        print("  param set MOT_SPOOL_TIME 0")
        print("  param set FS_GCS_ENABLE 0")
        print("  param set EK3_SRC1_POSXY 6")
        print("  param set EK3_SRC1_POSZ 6")
        print()
    print("Reboot ArduSub SITL to apply (in MAVProxy: reboot)")


if __name__ == "__main__":
    main()
