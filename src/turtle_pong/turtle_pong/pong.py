import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill, SetPen
from std_srvs.srv import Empty
from turtlesim.msg import Color
import math


class PongGame(Node):

    def __init__(self):
        super().__init__('pong')

        self.get_logger().info('Resetting and removing default turtle1 from the game')
        self.reset_game()
        
        # Spawn turtles
        self.spawn_player_turtle("turtle_left", 1.0, 5.0, math.pi / 2)
        self.spawn_player_turtle("turtle_right", 10.0, 5.0, math.pi / 2)

        # Subscriber to color sensor topic
        self.create_subscription(Color, '/ball/color_sensor', self.color_sensor_callback, 10)

        # Rate for the loop
        self.rate = self.create_rate(100)

    def reset_game(self):
        # Reset the turtlesim environment
        empty_service = self.create_client(Empty, '/reset')
        while not empty_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /reset service...')
        empty_request = Empty.Request()
        empty_service.call_async(empty_request)

        # Kill turtle1
        kill_service = self.create_client(Kill, '/kill')
        while not kill_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /kill service...')
        kill_request = Kill.Request()
        kill_request.name = "turtle1"
        kill_service.call_async(kill_request)

    def spawn_player_turtle(self, name, x, y, theta):
        self.get_logger().info(f'Spawning {name}')
        
        spawn_service = self.create_client(Spawn, '/spawn')
        while not spawn_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service...')
        spawn_request = Spawn.Request()
        spawn_request.name = name
        spawn_request.x = x
        spawn_request.y = y
        spawn_request.theta = theta
        spawn_service.call_async(spawn_request)

        set_pen_service = self.create_client(SetPen, f'/{name}/set_pen')
        while not set_pen_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f'Waiting for service {name}/set_pen...')
        set_pen_request = SetPen.Request()
        set_pen_request.off = True
        set_pen_service.call_async(set_pen_request)

    def color_sensor_callback(self, color):
        # Log received color
        self.get_logger().info(f'Color received (r,g,b) = ({color.r}, {color.g}, {color.b})')


def main(args=None):
    rclpy.init(args=args)
    pong_game = PongGame()

    try:
        while rclpy.ok():
            rclpy.spin_once(pong_game)
            pong_game.rate.sleep()
    except KeyboardInterrupt:
        pong_game.get_logger().info('Shutting down...')
    finally:
        pong_game.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
