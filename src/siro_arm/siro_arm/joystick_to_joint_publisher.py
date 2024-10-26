import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import pygame
import sys

class JoystickToJointPublisher(Node):

    def __init__(self):
        super().__init__('joystick_to_joint_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        # Inicializa pygame
        pygame.init()
        pygame.joystick.init()

        # Verifica si hay joystick conectado
        if pygame.joystick.get_count() < 1:
            self.get_logger().error("No se encontró ningún control.")
            sys.exit()

        # Crea el objeto joystick
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.get_logger().info(f"Control conectado: {self.joystick.get_name()}")

        # Inicializa los estados de las articulaciones
        self.joint_state = JointState()
        self.joint_state.name = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5']
        self.joint_state.position = [0.0] * 5

    def timer_callback(self):
        # Maneja los eventos del joystick
        pygame.event.pump()

        # Obtiene los valores del joystick para controlar las articulaciones
        left_x = self.joystick.get_axis(0)
        left_y = self.joystick.get_axis(1)
        right_x = self.joystick.get_axis(2)
        right_y = self.joystick.get_axis(3)
        
        # Control de la articulación 5 con botones L2 (botón 6) y R2 (botón 7)
        l2_pressed = self.joystick.get_button(6)  # L2 button
        r2_pressed = self.joystick.get_button(7)  # R2 button

        # Mapea los valores del joystick a los movimientos de las articulaciones
        self.joint_state.position[0] += left_x * 0.05  # joint_1
        self.joint_state.position[1] += left_y * 0.05  # joint_2
        self.joint_state.position[2] += right_x * 0.05  # joint_3
        self.joint_state.position[3] += right_y * 0.05  # joint_4

        # Mueve la articulación 5 con los botones L2 y R2
        if l2_pressed:  # L2 presionado
            self.joint_state.position[4] -= 0.05  # Rotar la articulación 5 hacia una dirección
        elif r2_pressed:  # R2 presionado
            self.joint_state.position[4] += 0.05  # Rotar la articulación 5 hacia la otra dirección

        # Asegúrate de que los valores estén dentro de los límites de las articulaciones
        self.joint_state.position = [
            max(min(pos, 1.57), -1.57) for pos in self.joint_state.position
        ]

        # Publica los nuevos estados de las articulaciones
        self.joint_state.header.stamp = self.get_clock().now().to_msg()
        self.publisher_.publish(self.joint_state)

def main(args=None):
    rclpy.init(args=args)
    node = JoystickToJointPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
