import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf_transformations import quaternion_from_euler

import random


class TurtlesimPositioningSystem(Node):

    def __init__(self):
        super().__init__('positioning_system')
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.positioning_callback, 10)
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, 'turtle1/sensors/pose', 10)
        self.subscription

        self.declare_parameter("positioning_frequency", 1)
        self.declare_parameter("error_x_systematic", 0.0)
        self.declare_parameter("error_x_random", 0.2)
        self.declare_parameter("error_y_systematic", 0.0)
        self.declare_parameter("error_y_random", 0.2)
        self.declare_parameter("error_yaw_systematic", 0.0)
        self.declare_parameter("error_yaw_random", 0.2)
        
        timer_period = 1 / float(self.get_parameter("positioning_frequency").value)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.msg_out = PoseWithCovarianceStamped()
        
    def positioning_callback(self, msg: Pose) -> None:
        #load parameters
        #fill up msg with pose from turtlesim and add noise
        #fill up msg with covariance matrix
        #publish msg
        mu_x = 0.0
        sigma_x = 0.0
        
        mu_y = 0.0
        sigma_y = 0.0
        
        mu_yaw = 0.0
        sigma_yaw = 0.0
        
    def timer_callback(self):
        self.publisher_.publish(self.msg_out)

def main(args=None):
    rclpy.init(args=args)
    positioning_system = TurtlesimPositioningSystem()
    rclpy.spin(positioning_system)
    positioning_system.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()