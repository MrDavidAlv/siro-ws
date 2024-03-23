#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class SiroNodePublicador : public rclcpp::Node
{
public:
    SiroNodePublicador() : Node("siro_node_publicador")
    {
        // Publica mensajes en el tópico 'chatter' cada segundo
        publisher_ = this->create_publisher<std_msgs::msg::String>("chatter", 10);
        timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                         [this]() {
                                             auto msg = std_msgs::msg::String();
                                             msg.data = "¡Hola desde siro_node_publicador!";
                                             RCLCPP_INFO(this->get_logger(), "Publicando: '%s'", msg.data.c_str());
                                             publisher_->publish(msg);
                                         });
    }

private:
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SiroNodePublicador>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
