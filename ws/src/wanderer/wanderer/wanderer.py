import rclpy
from rclpy.node import Node

from irobot_create_msgs.msg import HazardDetectionVector
from rclpy import qos

class Wanderer(Node):

    def __init__(self):
        super().__init__('wanderer')
        
        self.hazard_subscription = self.create_subscription(
            HazardDetectionVector,
            'zelda/hazard_detection',
            self.hazard_callback,
            qos.qos_profile_sensor_data)
        self.hazard_subscription  # prevent unused variable warning


    def hazard_callback(self, haz):
        self.get_logger().info('hazard!: "%i"' % len(haz.detections))


def main(args=None):
    rclpy.init(args=args)

    wanderer = Wanderer()

    rclpy.spin(wanderer)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    wanderer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


