#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <functional>  // Asegúrate de incluir esto
#include <memory>

class Suscriptor : public rclcpp::Node
{
public:
    Suscriptor()
    : Node("suscriptor")
    {
        // Crear el suscriptor y enlazar el callback
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "topic", 10,
            std::bind(&Suscriptor::callback, this, std::placeholders::_1)  // Usa std::placeholders::_1
        );
    }

private:
    void callback(const std_msgs::msg::String::SharedPtr msg) const
    {
        RCLCPP_INFO(this->get_logger(), "Recibido: '%s'", msg->data.c_str());
    }

    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;  // Declarar el puntero del suscriptor
};

int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Suscriptor>());
    rclcpp::shutdown();
    return 0;
}
