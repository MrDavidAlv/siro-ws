import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import turtlesim.srv
from rclpy.qos import QoSProfile

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')

        # Servicio para eliminar todas las tortugas
        self.client = self.create_client(turtlesim.srv.Kill, 'kill')

        # Esperar a que el servicio esté disponible
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando el servicio "kill"...')

        # Eliminar todas las tortugas
        self.kill_all_turtles()

        # Crear la tortuga izquierda, orientada hacia arriba
        self.spawn_turtle(1.0, 5.0, 'turtle_left')

        # Crear la tortuga derecha, orientada hacia arriba
        self.spawn_turtle(9.0, 5.0, 'turtle_right')

        # Suscribirse a los tópicos /left/cmd_vel y /right/cmd_vel
        self.create_subscription(Twist, 'left/cmd_vel', self.cmd_vel_left_callback, 10)
        self.create_subscription(Twist, 'right/cmd_vel', self.cmd_vel_right_callback, 10)

        # Publicadores para las tortugas
        self.publisher_left = self.create_publisher(Twist, 'turtle_left/cmd_vel', 10)
        self.publisher_right = self.create_publisher(Twist, 'turtle_right/cmd_vel', 10)

    def kill_all_turtles(self):
        """Elimina todas las tortugas en turtlesim."""
        request = turtlesim.srv.Kill.Request()
        for i in range(1, 11):  # Elimina hasta 10 tortugas (ajusta si es necesario)
            request.name = f'turtle{i}'
            self.client.call_async(request)

    def spawn_turtle(self, x, y, name):
        """Crea una nueva tortuga en la posición dada."""
        self.get_logger().info(f'Spawning {name} at ({x}, {y})')
        spawn_client = self.create_client(turtlesim.srv.Spawn, 'spawn')
        while not spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando el servicio "spawn"...')
        request = turtlesim.srv.Spawn.Request()
        request.x = x
        request.y = y
        request.theta = 1.5708  # Orientación hacia arriba (90 grados en radianes)
        request.name = name  # Nombre de la nueva tortuga
        spawn_client.call_async(request)

    def cmd_vel_left_callback(self, msg):
        """Callback que se llama cuando se recibe un mensaje en /left/cmd_vel."""
        self.publisher_left.publish(msg)  # Publica el mensaje en el tópico de la tortuga izquierda

    def cmd_vel_right_callback(self, msg):
        """Callback que se llama cuando se recibe un mensaje en /right/cmd_vel."""
        self.publisher_right.publish(msg)  # Publica el mensaje en el tópico de la tortuga derecha

def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
