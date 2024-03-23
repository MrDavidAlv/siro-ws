#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class SiroNodeSuscriptor : public rclcpp::Node
{
public:
    SiroNodeSuscriptor() : Node("siro_node_suscriptor")
    {
        // Suscribe al tópico 'chatter' con un callback
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "chatter", 10, [this](const std_msgs::msg::String::SharedPtr msg) {
                RCLCPP_INFO(this->get_logger(), "Mensaje recibido: '%s'", msg->data.c_str());
            });

        // Configura el temporizador para imprimir cada segundo
        timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                         [this]() {
                                             RCLCPP_INFO(this->get_logger(), "Esperando mensajes...");
                                         });
    }

private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SiroNodeSuscriptor>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
