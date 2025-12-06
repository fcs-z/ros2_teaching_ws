#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
using namespace std::chrono_literals;

class Pub: public rclcpp::Node{
public:
    Pub(const std::string &node_name):Node(node_name){
        RCLCPP_INFO(this->get_logger(),"发送端已经启动");
        talker_ = this->create_publisher<std_msgs::msg::String>("topic",10);
        timer_ = this->create_wall_timer(500ms,std::bind(&Pub::timer_callback,this));
    }

private:
    void timer_callback(){
        auto msg = std_msgs::msg::String();
        msg.data = "hello";
        RCLCPP_INFO(this->get_logger(),"发送消息: %s", msg.data.c_str());
        talker_->publish(msg);
    }
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr talker_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char const *argv[])
{
    rclcpp::init(argc, argv);
    auto talker = std::make_shared<Pub>("pub");
    rclcpp::spin(talker);
    rclcpp::shutdown();
    return 0;
}
