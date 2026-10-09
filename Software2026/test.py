import socket
import struct
import numpy as np
import cv2

PORT = 5001

def recv_all(conn, size):
    data = b''
    while len(data) < size:
        packet = conn.recv(size - len(data))
        if not packet:
            return None
        data += packet
    return data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", PORT))
sock.listen(1)

while True:  # outer loop: accept new connections
    print("Waiting for connection...")
    conn, addr = sock.accept()
    print("Connected:", addr)

    while True:  # inner loop: receive frames
        try:
            # Header: payload_size (4B) + height (4B) + width (4B)
            header = recv_all(conn, 12)
            if not header:
                print("Disconnected")
                break

            size, h, w = struct.unpack("III", header)
            expected = h * w * 4
            if size != expected:
                print(f"Header mismatch: {size} vs {expected}")
                break

            buffer = recv_all(conn, size)
            if buffer is None:
                print("Frame lost")
                break

            depth = np.frombuffer(buffer, dtype=np.float32).reshape((h, w))

            depth_vis = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
            depth_vis = depth_vis.astype(np.uint8)
            depth_vis = cv2.applyColorMap(depth_vis, cv2.COLORMAP_JET)  # optional but looks better
            cv2.imshow("Depth", depth_vis)

            if cv2.waitKey(1) == ord('q'):
                conn.close()
                sock.close()
                cv2.destroyAllWindows()
                exit(0)

        except Exception as e:
            print("Receiver error:", e)
            break

    conn.close()