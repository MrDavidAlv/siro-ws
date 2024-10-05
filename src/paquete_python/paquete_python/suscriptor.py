import rclpy  # Importar la biblioteca de cliente de ROS 2 para Python
from rclpy.node import Node  # Importar la clase Node, que es la base para los nodos de ROS 2
from std_msgs.msg import String  # Importar el tipo de mensaje String de los mensajes estándar de ROS

# Crear la clase Suscriptor, que hereda de Node
class Suscriptor(Node):
    def __init__(self):
        # Constructor de la clase Suscriptor
        super().__init__("Suscriptor")  # Llamar al constructor de la clase base Node con el nombre del nodo
        # Crear un suscriptor para el tema 'topic' que recibe mensajes de tipo String
        self.subscription = self.create_subscription(
            String,  # Tipo de mensaje que se va a recibir
            'mi_topico',  # Nombre del tema al que se suscribe
            self.callback,  # Función de callback que se llama cuando se recibe un mensaje
            10  # Tamaño de la cola del suscriptor
        )
        self.subscription  # Evitar que la variable de suscripción sea eliminada por el recolector de basura

    def callback(self, msg):
        # Esta función se llama cada vez que se recibe un mensaje
        self.get_logger().info(f'Recibido en Python: "{msg}"')  # Mostrar el contenido del mensaje recibido en el registro

def main(args=None):
    rclpy.init(args=args)  # Inicializar la biblioteca de cliente de ROS 2
    suscriptor = Suscriptor()  # Crear una instancia de la clase Suscriptor

    rclpy.spin(suscriptor)  # Mantener el nodo en ejecución para recibir eventos

    # Realizar limpieza después de que el nodo haya dejado de funcionar
    suscriptor.destroy_node()  # Destruir el nodo
    rclpy.shutdown()  # Cerrar la biblioteca de cliente de ROS 2

# Comprobar si el script se está ejecutando directamente
if __name__ == '__main__':
    main()  # Llamar a la función main para ejecutar el nodo
