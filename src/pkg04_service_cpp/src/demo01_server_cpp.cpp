#include <rclcpp/rclcpp.hpp>
#include <pkg00_interfaces/srv/add_ints.hpp>
using pkg00_interfaces::srv::AddInts;

class Ser:public rclcpp::Node{
public:
    Ser(const std::string &node_name):Node(node_name){
        RCLCPP_INFO(this->get_logger(),"服务端已启动,等待请求...");
        server_ = this->create_service<AddInts>("service_add_nums",
            std::bind(&Ser::add_callback,this,std::placeholders::_1,std::placeholders::_2));
    }
    
    void add_callback(const AddInts::Request::SharedPtr req,const AddInts::Response::SharedPtr res){
        res->sum = req->num1 + req->num2;
        RCLCPP_INFO(this->get_logger(),"计算过程: %d + %d = %d",req->num1,req->num2,res->sum);
    }
private:
    rclcpp::Service<AddInts>::SharedPtr server_;

};

int main(int argc, char* argv[]){
    rclcpp::init(argc,argv);
    auto server = std::make_shared<Ser>("Ser");
    rclcpp::spin(server);
    rclcpp::shutdown();
}
