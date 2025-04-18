import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import turtlesim.srv
from rclpy.qos import QoSProfile

class BallController(Node):
    def __init__(self):
        super().__init__('ball_controller')

        # Servicio para eliminar todas las tortugas
        self.client = self.create_client(turtlesim.srv.Kill, 'kill')

        # Esperar a que el servicio esté disponible
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando el servicio "kill"...')

        # Eliminar todas las tortugas
        self.kill_all_turtles()

        # Crear el balón en una posición inicial
        self.spawn_ball(5.0, 5.0, 'ball')

        # Suscribirse al tópico para recibir comandos de movimiento del balón
        self.create_subscription(Twist, 'ball/cmd_vel', self.cmd_vel_ball_callback, 10)

        # Publicador para el balón
        self.publisher_ball = self.create_publisher(Twist, 'ball/cmd_vel', 10)

    def kill_all_turtles(self):
        """Elimina todas las tortugas en turtlesim."""
        request = turtlesim.srv.Kill.Request()
        for i in range(1, 11):  # Elimina hasta 10 tortugas (ajusta si es necesario)
            request.name = f'turtle{i}'
            self.client.call_async(request)

    def spawn_ball(self, x, y, name):
        """Crea una nueva tortuga en la posición dada, simulando un balón."""
        self.get_logger().info(f'Spawning {name} at ({x}, {y})')
        spawn_client = self.create_client(turtlesim.srv.Spawn, 'spawn')
        while not spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando el servicio "spawn"...')
        request = turtlesim.srv.Spawn.Request()
        request.x = x
        request.y = y
        request.theta = 0.0  # Orientación inicial (hacia la derecha)
        request.name = name  # Nombre del balón
        spawn_client.call_async(request)

    def cmd_vel_ball_callback(self, msg):
        """Callback que se llama cuando se recibe un mensaje en /ball/cmd_vel."""
        # Publica el mensaje en el tópico de movimiento del balón
        self.publisher_ball.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    ball_controller = BallController()
    rclpy.spin(ball_controller)
    ball_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
