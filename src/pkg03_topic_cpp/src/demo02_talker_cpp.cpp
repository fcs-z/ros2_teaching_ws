#include <rclcpp/rclcpp.hpp>
#include <pkg00_interfaces/msg/student.hpp>
using namespace std::chrono_literals;
using pkg00_interfaces::msg::Student;

class Pub: public rclcpp::Node{
public:
    Pub(const std::string &node_name):Node(node_name){
        RCLCPP_INFO(this->get_logger(),"发送端已经启动");
        talker_ = this->create_publisher<Student>("topic_stu",10);
        timer_ = this->create_wall_timer(500ms,std::bind(&Pub::timer_callback,this));
    }

private:
    void timer_callback(){
        auto stu = Student();
        stu.name = "asd";
        stu.age = 100;
        stu.height = 1.70;
        RCLCPP_INFO(this->get_logger(),"发送学生信息: name = %s, age = %d, height = %.2f", stu.name.c_str(), stu.age, stu.height);
        talker_->publish(stu);
    }
    rclcpp::Publisher<Student>::SharedPtr talker_;
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