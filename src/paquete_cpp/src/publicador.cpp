#include <rclcpp/rclcpp.hpp>  // Incluir la biblioteca de ROS 2
#include <std_msgs/msg/string.hpp>  // Incluir el mensaje de tipo String

using std::placeholders::_1;  // Para usar _1 como un marcador de posición en los callbacks

class Publicador : public rclcpp::Node {
public:
    Publicador() : Node("publicador") {
        // Crear un publicador para mensajes de tipo String en el tema 'topic'
        publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);

        // Crear un temporizador que llama a la función de cronómetro cada segundo
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1),  // Intervalo de 1 segundo
            std::bind(&Publicador::cronometro, this)  // Enlazar la función cronómetro
        );

        contador_ = 0;  // Inicializar el contador
    }

private:
    void cronometro() {
        auto mensaje = std_msgs::msg::String();  // Crear un nuevo mensaje String
        mensaje.data = "Estoy contando: " + std::to_string(contador_);  // Formatear el mensaje
        publisher_->publish(mensaje);  // Publicar el mensaje

        // Mostrar el mensaje publicado en el registro
        RCLCPP_INFO(this->get_logger(), "Publicando los datos desde C++: '%s'", mensaje.data.c_str());
        contador_++;  // Incrementar el contador
    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;  // Atributo para el publicador
    rclcpp::TimerBase::SharedPtr timer_;  // Atributo para el temporizador
    int contador_;  // Contador
};

// Función principal
int main(int argc, char **argv) {
    rclcpp::init(argc, argv);  // Inicializar la biblioteca de cliente de ROS 2
    rclcpp::spin(std::make_shared<Publicador>());  // Crear e iniciar el nodo
    rclcpp::shutdown();  // Cerrar la biblioteca de cliente de ROS 2
    return 0;  // Salir del programa
}
