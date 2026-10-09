import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from image_transport import ImageTransport

import cv2


def main():
    rclpy.init()

    node = Node("theora_viewer")
    bridge = CvBridge()

    def callback(msg):
        frame = bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow("Theora Frame", frame)
        cv2.waitKey(1)

    # 👇 ده السحر كله
    it = ImageTransport(node)
    sub = it.subscribe(
        '/zed/zed_node/left/image_rect_color',
        callback,
        transport='theora'
    )

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()