import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame
import sys

class TurtleJoyControl(Node):
    def __init__(self):
        super().__init__('TurtleJoyControl')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() < 1:
            self.get_logger().error("No se encontró ningún control.")
            sys.exit()

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                rclpy.shutdown()
                return

        left_x = -round(self.joystick.get_axis(0), 3)
        left_y = -round(self.joystick.get_axis(1), 3)

        msg = Twist()
        msg.linear.x, msg.angular.z = left_y, left_x
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    turtle_joy_control = TurtleJoyControl()
    try:
        rclpy.spin(turtle_joy_control)
    finally:
        turtle_joy_control.destroy_node()
        rclpy.shutdown()
        pygame.quit()

if __name__ == '__main__':
    main()
