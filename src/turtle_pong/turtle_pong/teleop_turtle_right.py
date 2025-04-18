import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import select
import tty
import termios


class TeleopTurtleRight(Node):
    def __init__(self):
        super().__init__('teleop_turtle_right')
        self.publisher_ = self.create_publisher(Twist, 'turtle_right/cmd_vel', 1)
        self.get_logger().info('Controlling turtle_right using keyboard. Press "w" to move forward, "s" to move backward, "q" to quit.')
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.speed = Twist()

    def timer_callback(self):
        if self.speed:
            self.publisher_.publish(self.speed)

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
            if rlist:
                key = sys.stdin.read(1)
                return key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None

    def run(self):
        while rclpy.ok():
            key = self.get_key()
            if key is not None:
                if key == 'w':
                    self.speed.linear.x = 1.0  # Mover hacia adelante
                    self.get_logger().debug('Moving forward')
                elif key == 's':
                    self.speed.linear.x = -1.0  # Mover hacia atrás
                    self.get_logger().debug('Moving backward')
                elif key == 'q':
                    self.get_logger().info('Quitting')
                    break
                else:
                    self.speed.linear.x = 0.0  # Detener
            else:
                self.speed.linear.x = 0.0  # Detener

        self.speed.linear.x = 0.0  # Detener al final
        self.publisher_.publish(self.speed)
        self.destroy_node()


def main(args=None):
    rclpy.init(args=args)
    teleop_turtle_right = TeleopTurtleRight()
    teleop_turtle_right.run()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
