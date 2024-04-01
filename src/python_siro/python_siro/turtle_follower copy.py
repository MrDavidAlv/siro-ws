import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import os


class TurtleFollower(Node):

    def __init__(self):
        super().__init__('turtle_follower')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.file_path = os.path.join(os.path.dirname(__file__), 'coordinates', 'coordinates.txt')

        if os.path.exists(self.file_path):
            self.follow_coordinates()
        else:
            self.get_logger().error("El archivo de coordenadas no existe.")

    def follow_coordinates(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                x, y = map(float, line.split())
                self.move_turtle_to(x, y)

    def move_turtle_to(self, x, y):
        msg = Twist()
        msg.linear.x = x
        msg.linear.y = y
        self.publisher_.publish(msg)
        self.get_logger().info(f"Moviendo la tortuga a ({x}, {y})")


def main(args=None):
    rclpy.init(args=args)
    node = TurtleFollower()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
