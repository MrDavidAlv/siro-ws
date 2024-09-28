import rclpy
from rclpy.node import Node
import time

class RendimientoPythonNode(Node):
    def __init__(self):
        super().__init__('rendimiento_python')

        # Número de Fibonacci a calcular (puedes cambiar este valor para probar diferentes números)
        n = 30

        # Medir el tiempo de inicio
        start_time = time.time()

        # Calcular Fibonacci
        resultado = self.calcular_fibonacci(n)

        # Medir el tiempo de finalización
        end_time = time.time()

        # Calcular la duración en milisegundos
        duration = (end_time - start_time) * 1000

        # Imprimir el resultado y el tiempo de ejecución
        self.get_logger().info(f'Python: Fibonacci({n}) = {resultado}')
        self.get_logger().info(f'Python: Tiempo de ejecución = {duration} ms')

    def calcular_fibonacci(self, n):
        if n <= 1:
            return n
        return self.calcular_fibonacci(n - 1) + self.calcular_fibonacci(n - 2)


def main(args=None):
    # Inicializar ROS 2
    rclpy.init(args=args)

    # Crear el nodo de rendimiento en Python
    node = RendimientoPythonNode()

    # Ejecutar el nodo
    rclpy.spin(node)

    # Finalizar ROS 2
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
