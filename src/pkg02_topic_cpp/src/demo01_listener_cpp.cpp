#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
using namespace std::chrono_literals;

class Sub: public rclcpp::Node{
public:
    Sub(const std::string &node_name):Node(node_name){
        RCLCPP_INFO(this->get_logger(),"接收端已经启动");
        listener_ = this->create_subscription<std_msgs::msg::String>("topic",10,
            std::bind(&Sub::sub_callback,this,std::placeholders::_1));
    }

private:
    void sub_callback(const std_msgs::msg::String &msg){
        RCLCPP_INFO(this->get_logger(),"收到消息: %s",msg.data.c_str());
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr listener_;
};

int main(int argc, char const *argv[])
{
    rclcpp::init(argc, argv);
    auto listener = std::make_shared<Sub>("sub");
    rclcpp::spin(listener);
    rclcpp::shutdown();
    return 0;
}
