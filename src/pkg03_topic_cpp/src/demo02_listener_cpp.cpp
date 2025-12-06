#include <rclcpp/rclcpp.hpp>
#include <pkg00_interfaces/msg/student.hpp>
using namespace std::chrono_literals;
using pkg00_interfaces::msg::Student;

class Sub: public rclcpp::Node{
public:
    Sub(const std::string &node_name):Node(node_name){
        RCLCPP_INFO(this->get_logger(),"接收端已经启动");
        listener_ = this->create_subscription<Student>("topic_stu",10,
            std::bind(&Sub::sub_callback,this,std::placeholders::_1));
    }

private:
    void sub_callback(const Student &stu){
        RCLCPP_INFO(this->get_logger(),"收到学生信息: name = %s, age = %d, height = %.2f", stu.name.c_str(), stu.age, stu.height);
    }
    rclcpp::Subscription<Student>::SharedPtr listener_;
};

int main(int argc, char const *argv[])
{
    rclcpp::init(argc, argv);
    auto listener = std::make_shared<Sub>("sub");
    rclcpp::spin(listener);
    rclcpp::shutdown();
    return 0;
}