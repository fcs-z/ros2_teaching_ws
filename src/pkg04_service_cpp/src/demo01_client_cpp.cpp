#include <rclcpp/rclcpp.hpp>
#include <pkg00_interfaces/srv/add_ints.hpp>
using pkg00_interfaces::srv::AddInts;
using namespace std::chrono_literals;

class Cli:public rclcpp::Node{
public:
    Cli(const std::string &node_name):Node(node_name){
        RCLCPP_INFO(this->get_logger(),"客户端已启动");
        client_ = this->create_client<AddInts>("service_add_nums");
    }

    bool isConnect(){
        while (!client_->wait_for_service(1s))
        {
            if(!rclcpp::ok()){
                RCLCPP_INFO(rclcpp::get_logger("rclcpp"),"强制退出");
                return false;
            }
            RCLCPP_INFO(this->get_logger(),"服务连接中，请稍侯...");
        }
        return true;    
    }

    rclcpp::Client<AddInts>::FutureAndRequestId send_request(int32_t num1, int32_t num2){
        auto request = std::make_shared<AddInts::Request>();
        request->num1 = num1;
        request->num2 = num2;
        return client_->async_send_request(request);
    }
     
private:
    rclcpp::Client<AddInts>::SharedPtr client_;

};

int main(int argc, char* argv[]){
    if(argc !=3 ){
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"),"请提交两个整数");
        return 1;
    }

    rclcpp::init(argc,argv);
    auto client = std::make_shared<Cli>("Cli");

    bool flag = client->isConnect();
    if(!flag){
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"),"服务连接失败");
        return 0;
    }
    auto response = client->send_request(atoi(argv[1]),atoi(argv[2]));

    if(rclcpp::spin_until_future_complete(client,response) == rclcpp::FutureReturnCode::SUCCESS){
        RCLCPP_INFO(client->get_logger(),"请求正常处理");
        RCLCPP_INFO(client->get_logger(),"响应结果: %d",response.get()->sum);
    }else{
        RCLCPP_INFO(client->get_logger(),"请求异常");
    }
    
    rclcpp::shutdown();
    return 0;
}
