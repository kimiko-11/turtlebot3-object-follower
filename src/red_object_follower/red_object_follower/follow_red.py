import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class RedObjectFollower(Node):
    def __init__(self):
        super().__init__('red_object_follower')

        # Create subscriber for camera feed
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        # Create publisher for velocity commands
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        self.bridge = CvBridge()
        self.get_logger().info("Red Object Follower Node has started.")

    def image_callback(self, msg):
        try:
            # Convert ROS image to OpenCV
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"CV Bridge error: {e}")
            return

        # Image center
        h, w, _ = frame.shape
        image_center_x = w // 2

        # Convert to HSV and create red mask
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red color range
        lower_red1 = np.array([0, 100, 100])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([160, 100, 100])
        upper_red2 = np.array([179, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 | mask2

        # Morphological operations
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=2)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        twist = Twist()

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)

            if area > 500:  # Ignore noise
                M = cv2.moments(largest_contour)
                if M['m00'] > 0:
                    cx = int(M['m10'] / M['m00'])
                    error = image_center_x - cx
                    dead_zone = 30

                    # Move forward if not too close
                    if area < 5000:
                        twist.linear.x = 0.15
                    else:
                        twist.linear.x = 0.0  # Stop if too close

                    # Adjust angle
                    if abs(error) > dead_zone:
                        twist.angular.z = -float(error) / 400.0
                    else:
                        twist.angular.z = 0.0

                    self.get_logger().info(f"Tracking | Area: {area:.1f} | Error: {error}")
        else:
            self.get_logger().info("No red object in view.")
            twist.linear.x = 0.0
            twist.angular.z = 0.2  # Optional: rotate to search

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = RedObjectFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
