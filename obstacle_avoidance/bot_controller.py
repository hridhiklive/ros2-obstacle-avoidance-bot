# obstacle_avoidance/bot_controller.py

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.laser_callback,
            10)
        self.get_logger().info('Obstacle Avoidance Node Started')

    def laser_callback(self, msg):
        move = Twist()
        min_distance = min(msg.ranges)
        self.get_logger().info(f'Min scan distance: {min_distance:.2f} m')

        if min_distance < 0.5:
            move.linear.x = 0.0
            move.angular.z = 0.5  # Turn
        else:
            move.linear.x = 0.2
            move.angular.z = 0.0  # Go straight

        self.publisher_.publish(move)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

