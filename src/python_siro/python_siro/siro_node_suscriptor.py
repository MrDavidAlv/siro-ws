import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SiroNodeSuscriptor(Node):

    def __init__(self):
        super().__init__('siro_node_suscriptor')
        self.subscription_ = self.create_subscription(
            String, 'chatter', self.subscriber_callback, 10)
        self.timer_ = self.create_timer(1, self.timer_callback)

    def subscriber_callback(self, msg):
        self.get_logger().info("Mensaje recibido: '%s'" % msg.data)

    def timer_callback(self):
        self.get_logger().info("Esperando mensajes...")

def main(args=None):
    rclpy.init(args=args)
    node = SiroNodeSuscriptor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
