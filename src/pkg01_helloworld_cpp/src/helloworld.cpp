#include <rclcpp/rclcpp.hpp>

class MyNode:public rclcpp::Node{ 
public:
    MyNode(const std::string &node_name):
        Node(node_name){
            RCLCPP_INFO(this->get_logger(),
                "helloworld");
        }
};

int main(int argc, char const *argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MyNode>("cpp_node");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}



