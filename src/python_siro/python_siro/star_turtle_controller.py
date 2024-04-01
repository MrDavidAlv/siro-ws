import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time


class StarTurtleController(Node):

    def __init__(self):
        super().__init__('star_turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.move_turtle()

    def move_turtle(self):
        # Definir las coordenadas de los puntos de la estrella de David
        points = [
            (0.0, 1.0),
            (math.sqrt(3)/2, -0.5),
            (-math.sqrt(3)/2, -0.5),
            (0.0, 1.0),
            (0.0, -1.0),
            (math.sqrt(3)/2, 0.5),
            (-math.sqrt(3)/2, 0.5),
            (0.0, -1.0)
        ]

        # Publicar comandos de movimiento para cada punto
        for point in points:
            msg = Twist()
            msg.linear.x = point[0]
            msg.linear.y = point[1]
            self.publisher_.publish(msg)
            # Esperar un breve tiempo antes de moverse al siguiente punto
            time.sleep(1)


def main(args=None):
    rclpy.init(args=args)
    node = StarTurtleController()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
