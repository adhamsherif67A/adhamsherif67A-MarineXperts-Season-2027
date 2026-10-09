# ROV Image Capture Implementation Plan
## Status: ✅ COMPLETE

## Steps Completed:
## Step 1: ✅ Create TODO.md
## Step 2: ✅ Verify OpenCV (available)
## Step 3: ✅ Edit src/real_joy/src/rov_gui_gst.py
   - Added cv2 import + OPENCV_AVAILABLE check
   - Added frame_raw_signal (np.ndarray) to GStreamerWorker  
   - Emit raw RGB frame from _on_new_sample (frame_rgb.copy())
   - Store self._last_frame in ROVMainWindow._on_raw_frame()
   - Added keyPressEvent: 'c' → cv2.imwrite("/media/boda/ESD-ISO/rov_capture_{timestamp}.png")

## Step 4: READY FOR TESTING
**Instructions:**
1. Ensure flash drive mounted at `/media/boda/ESD-ISO`
2. Run: `python3 src/real_joy/src/rov_gui_gst.py`
3. Start H.264 UDP stream (port 5000)
4. **Press 'c'** → check PNG saved to flash drive

## Step 5: If ROS integration needed
```
colcon build --packages-select real_joy
source install/setup.bash
ros2 run real_joy rov_gui_gst
```


