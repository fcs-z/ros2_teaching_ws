import rclpy
from rclpy.node import Node
from pkg00_interfaces.srv import AddInts
import sys

class Cli(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info("客户端已启动")
        self.client_ = self.create_client(AddInts, "service_add_nums")
    
    def is_connect(self):
        while not self.client_.wait_for_service(timeout_sec=1.0):
            if not rclpy.ok():
                self.get_logger().info("强制退出")
                return False
            self.get_logger().info("服务连接中，请稍侯...")
        return True
    
    def send_request(self, num1, num2):
        req = AddInts.Request()
        req.num1 = num1
        req.num2 = num2
        return self.client_.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    
    if len(sys.argv) != 3:
        print("请提交两个整数")
        return 1
        
    client = Cli("Cli")
    
    if not client.is_connect():
        client.get_logger().info("服务连接失败")
        return 0
        
    future = client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    
    while rclpy.ok():
        rclpy.spin_once(client)
        if future.done():
            try:
                response = future.result()
                client.get_logger().info(f"请求正常处理")
                client.get_logger().info(f"响应结果: {response.sum}")
            except Exception as e:
                client.get_logger().error(f"请求异常: {e}")
            break
            
    rclpy.shutdown()
