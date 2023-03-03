import rclpy
from rclpy.node import Node
import rclpy
from geometry_msgs.msg import Twist

from irobot_create_msgs.msg import IrIntensityVector
from geometry_msgs.msg import Twist
from rclpy import qos

from math import radians
from random import uniform

class Reactor(Node):

    def __init__(self):
        super().__init__('reactor')
        self.hazard_subscription = self.create_subscription(
            IrIntensityVector,
            'zelda/ir_intensity',
            self.ir_callback,
            qos.qos_profile_sensor_data)

        self.publisher = self.create_publisher(Twist, 'zelda/cmd_vel', 10)

        self.move_timer = self.create_timer(
            TIMER_INTERVAL,
            self.move_timer_callback
        )
    #def hazard_callback(self, haz: IrIntensityVector):

        #for det in haz.:



def main(args=None):
    rclpy.init(args=args)

    reactor = Reactor()

    rclpy.spin(reactor)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    reactor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()