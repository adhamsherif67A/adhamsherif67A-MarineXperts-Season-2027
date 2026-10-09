import cv2

cap = cv2.VideoCapture("udpsrc port=5000 caps=application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! appsink", cv2.CAP_GSTREAMER)

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # احفظ كل فريمين (left/right) أو حسب ترتيب الكاميرا
    cv2.imwrite(f"images/image_left_{count}.png", frame)
    # لو عندك frame تاني للكرترا اليمين
    # cv2.imwrite(f"images/image_right_{count}.png", frame_right)
    count += 1
    if count >= 50:  # مثلا 50 صورة كفاية
        break

cap.release()