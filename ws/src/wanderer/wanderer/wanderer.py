import rclpy
from rclpy.node import Node
import rclpy
from geometry_msgs.msg import Twist

from irobot_create_msgs.msg import HazardDetectionVector, HazardDetection
from geometry_msgs.msg import Twist
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

        self.publisher = self.create_publisher(Twist, 'zelda/cmd_vel', 10)

    def hazard_callback(self, haz: HazardDetectionVector):
        self.get_logger().info('hazard!: "%i"' % len(haz.detections))
        # self.get_logger().info(f"hazards found: {haz.detections}")

        for det in haz.detections:
            if det.type == HazardDetection.BUMP:
                self.get_logger().info(f"bumped")
                
                twist = Twist()
                #twist.linear.x = 0.2  # Move forward at 0.2 m/s
                twist.angular.z = 0.5

                for i in range(50):
                    self.publisher.publish(twist)
                    self.get_logger().info('Moving robot...')
                    rclpy.spin_once(self, timeout_sec=0.1)

        

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


