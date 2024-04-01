import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class SiroNodePublicador(Node):

    def __init__(self):
        super().__init__('siro_node_publicador')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer_ = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = '¡Hola desde siro_node_publicador!'
        self.get_logger().info('Publicando: "%s"' % msg.data)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SiroNodePublicador()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
