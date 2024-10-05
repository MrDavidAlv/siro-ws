import rclpy  # Importar la biblioteca de cliente de ROS 2 para Python
from rclpy.node import Node  # Importar la clase Node, que es la base para los nodos de ROS 2
from std_msgs.msg import String  # Importar el tipo de mensaje String de los mensajes estándar de ROS

# Crear la clase Publicador, que hereda de Node
class Publicador(Node):
    def __init__(self):
        # Constructor de la clase Publicador
        super().__init__("Publicador")  # Llamar al constructor de la clase base Node con el nombre del nodo
        # Crear un publicador para mensajes de tipo String en el tema 'topic'
        self.publisher = self.create_publisher(String, 'mi_topico', 10)  # Usar un solo atributo para el publicador
        
        # Establecer un cronómetro con un periodo de 1 segundo
        periodo = 1.0  # Definir el periodo del cronómetro en 1 segundo
        self.timer = self.create_timer(periodo, self.cronometro)  # Crear un temporizador que llame a cronometro cada segundo
        self.i = 0  # Inicializar el contador

    def cronometro(self):
        # Esta función se llama cada vez que se activa el temporizador
        msg = String()  # Crear un nuevo mensaje de tipo String
        msg.data = f'Hola mundo: {self.i}'  # Formatear el mensaje con el contador actual
        self.publisher.publish(msg)  # Publicar el mensaje en el tema

        # Registrar el mensaje publicado en la consola
        self.get_logger().info(f'Publicando los datos "{msg.data}"')  # Mostrar el mensaje en el registro
        self.i += 1  # Incrementar el contador para la próxima publicación

def main(args=None):
    rclpy.init(args=args)  # Inicializar la biblioteca de cliente de ROS 2
    publicador = Publicador()  # Crear una instancia de la clase Publicador

    rclpy.spin(publicador)  # Mantener el nodo en ejecución para recibir eventos

    # Realizar limpieza después de que el nodo haya dejado de funcionar
    publicador.destroy_node()  # Destruir el nodo
    rclpy.shutdown()  # Cerrar la biblioteca de cliente de ROS 2

# Comprobar si el script se está ejecutando directamente
if __name__ == '__main__':
    main()  # Llamar a la función main para ejecutar el nodo
