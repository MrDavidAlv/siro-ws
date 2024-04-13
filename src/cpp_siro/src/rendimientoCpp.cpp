#include <chrono>
#include <iostream>
#include <rclcpp/rclcpp.hpp>

using namespace std::chrono;
using namespace rclcpp;

class RendimientoCppNode : public Node {
public:
    RendimientoCppNode() : Node("rendimiento_cpp") {
        // Número de Fibonacci a calcular (puedes cambiar este valor para probar diferentes números)
        int n = 30;

        // Medir el tiempo de inicio
        auto start_time = high_resolution_clock::now();

        // Calcular Fibonacci
        int resultado = calcular_fibonacci(n);

        // Medir el tiempo de finalización
        auto end_time = high_resolution_clock::now();

        // Calcular la duración en milisegundos
        auto duration = duration_cast<milliseconds>(end_time - start_time).count();

        // Imprimir el resultado y el tiempo de ejecución
        std::cout << "C++: Fibonacci(" << n << ") = " << resultado << std::endl;
        std::cout << "C++: Tiempo de ejecución = " << duration << " ms" << std::endl;
    }

private:
    // Función para calcular Fibonacci de forma recursiva
    int calcular_fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2);
    }
};

int main(int argc, char** argv) {
    // Inicializar ROS 2
    rclcpp::init(argc, argv);

    // Crear el nodo de rendimiento en C++
    auto node = std::make_shared<RendimientoCppNode>();

    // Ejecutar el nodo
    rclcpp::spin(node);

    // Finalizar ROS 2
    rclcpp::shutdown();
    return 0;
}
