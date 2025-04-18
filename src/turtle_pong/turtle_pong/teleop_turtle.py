import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import signal
import sys
import tty
import termios

# Ascii codes for small keyboard characters
KEYCODE_RIGHT = 0x43
KEYCODE_LEFT = 0x44
KEYCODE_UP = 0x41
KEYCODE_DOWN = 0x42
KEYCODE_W = 0x77
KEYCODE_S = 0x73
KEYCODE_Q = 0x71

class KeyboardReader:
    def __init__(self):
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin.fileno())

    def read_one(self):
        ch = sys.stdin.read(1)
        if ch:
            return ord(ch)
        return None

    def shutdown(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)


class TeleopTurtle(Node):
    def __init__(self):
        super().__init__('teleop_turtle')

        self.linear = 0.0
        self.angular = 0.0
        self.l_scale = 2.0
        self.a_scale = 2.0

        self.declare_parameter('scale_linear', self.l_scale)
        self.declare_parameter('scale_angular', self.a_scale)

        self.l_scale = self.get_parameter('scale_linear').get_parameter_value().double_value
        self.a_scale = self.get_parameter('scale_angular').get_parameter_value().double_value

        self.twist_left_pub = self.create_publisher(Twist, 'turtle_left/cmd_vel', 1)
        self.twist_right_pub = self.create_publisher(Twist, 'turtle_right/cmd_vel', 1)
        self.twist_ball_pub = self.create_publisher(Twist, 'ball/cmd_vel', 1)

        self.keyboard_reader = KeyboardReader()
        signal.signal(signal.SIGINT, self.quit)

    def quit(self, signum, frame):
        self.keyboard_reader.shutdown()
        rclpy.shutdown()
        sys.exit(0)

    def get_key_press(self):
        return self.keyboard_reader.read_one()

    def key_loop(self):
        print("Reading from keyboard")
        print("---------------------------")
        print("Use W/S to move the left turtle up/down.")
        print("Use UP/DOWN to move the right turtle up/down.")
        print("Use LEFT/RIGHT to move the ball left/right.")
        print("'q' to quit.")

        while True:
            c = self.get_key_press()
            if c is not None:
                self.linear = self.angular = 0.0

                # Control para la tortuga izquierda
                if c == KEYCODE_W:
                    self.linear = 1.0  # Mover hacia adelante
                elif c == KEYCODE_S:
                    self.linear = -1.0  # Mover hacia atrás

                # Control para la tortuga derecha
                elif c == KEYCODE_UP:
                    self.linear = 1.0  # Mover hacia adelante
                elif c == KEYCODE_DOWN:
                    self.linear = -1.0  # Mover hacia atrás

                # Control para el balón
                elif c == KEYCODE_LEFT:
                    self.angular = -1.0  # Mover el balón a la izquierda
                elif c == KEYCODE_RIGHT:
                    self.angular = 1.0  # Mover el balón a la derecha

                elif c == KEYCODE_Q:
                    self.quit(0, None)

                twist_left = Twist()
                twist_right = Twist()
                twist_ball = Twist()

                # Publicar velocidades en función de la tortuga
                if c in (KEYCODE_W, KEYCODE_S):
                    twist_left.linear.x = self.l_scale * self.linear
                    self.twist_left_pub.publish(twist_left)

                if c in (KEYCODE_UP, KEYCODE_DOWN):
                    twist_right.linear.x = self.l_scale * self.linear
                    self.twist_right_pub.publish(twist_right)

                if c in (KEYCODE_LEFT, KEYCODE_RIGHT):
                    twist_ball.angular.z = self.a_scale * self.angular
                    self.twist_ball_pub.publish(twist_ball)


def main(args=None):
    rclpy.init(args=args)
    teleop_turtle = TeleopTurtle()

    try:
        teleop_turtle.key_loop()
    except Exception as e:
        teleop_turtle.get_logger().error(f"Error in key loop: {str(e)}")
    finally:
        teleop_turtle.quit(0, None)

if __name__ == '__main__':
    main()
