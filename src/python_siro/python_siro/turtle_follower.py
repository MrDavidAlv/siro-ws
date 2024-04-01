import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class TurtleGCodeFollower(Node):

    def __init__(self):
        super().__init__('turtle_gcode_follower')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.move_turtle_to(0.0, 0.0)  # Mover la tortuga a la esquina inferior izquierda
        self.follow_gcode()

    def follow_gcode(self):
        scale_factor = 0.001  # Factor de escala (ajusta según sea necesario)
        gcode = [
            "G01 X-50.0 Y-50.0",
            "G01 X41.55",
            "G01 X41.55",
            "G01 X41.55 Y65.17",
            "G01 X41.55 Y65.17",
            "G01 X41.39 Y65.53",
            "G01 X41.07 Y66.21",
            "G01 X40.65 Y67.15",
            "G01 X40.13 Y68.29",
            "G01 X39.55 Y69.55",
            "G01 X39.3 Y70.1",
            "G01 X38.89 Y70.99",
            "G01 X38.46 Y71.95",
            "G01 X38 Y72.94",
            "G01 X37.55 Y73.94",
            "G01 X37.1 Y74.92",
            "G01 X36.67 Y75.85",
            "G01 X36.28 Y76.71",
            "G01 X35.93 Y77.47",
            "G01 X35.81 Y77.75",
            "G01 X35.18 Y79.13",
            "G01 X34.68 Y80.24",
            "G01 X34.37 Y80.95",
            "G01 X34.3 Y81.12",
            "G01 X34.85 Y81.17",
            "G01 X36.18 Y81.2",
            "G01 X38.47 Y81.2",
            "G01 X39.1 Y79.75",
            "G01 X39.73 Y78.3",
            "G01 X42.01 Y78.3",
            "G01 X44.28 Y78.3",
            "G01 X44.88 Y79.72",
            "G01 X45.48 Y81.15",
            "G01 X47.84 Y81.18",
            "G01 X47.84 Y81.18",
            "G01 X49.28 Y81.18",
            "G01 X50.11 Y81.15",
            "G01 X50.2 Y81.13",
            "G01 X50.14 Y80.98",
            "G01 X49.97 Y80.59",
            "G01 X49.7 Y79.98",
            "G01 X49.33 Y79.18",
            "G01 X48.89 Y78.19",
            "G01 X48.37 Y77.06",
            "G01 X47.8 Y75.8",
            "G01 X47.18 Y74.43",
            "G01 X46.52 Y72.98",
            "G01 X42.71 Y64.65",
            "G01 X42.27 Y64.62",
            "G01 X41.82 Y64.59",
            "G01 X41.55 Y65.17",
            "G01 Y0",
            "G01 X0"
        ]

        for command in gcode:
            parts = command.split()
            if len(parts) < 2:
                continue
            x, y = 0.0, 0.0
            for part in parts[1:]:
                if part.startswith('X'):
                    x = float(part[1:]) * scale_factor
                elif part.startswith('Y'):
                    y = float(part[1:]) * scale_factor
            self.move_turtle_to(x, y)

    def move_turtle_to(self, x, y):
        msg = Twist()
        msg.linear.x = x
        msg.linear.y = y
        self.publisher_.publish(msg)
        self.get_logger().info(f"Moviendo la tortuga a ({x}, {y})")
        # Esperar un breve tiempo antes de moverse al siguiente punto
        time.sleep(1)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleGCodeFollower()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
