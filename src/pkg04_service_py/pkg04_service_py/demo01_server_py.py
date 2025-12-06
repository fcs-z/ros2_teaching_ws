import rclpy
from rclpy.node import Node
from pkg00_interfaces.srv import AddInts
import sys

class Ser(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info("服务端已启动,等待请求...")
        self.server_ = self.create_service(AddInts, "service_add_nums", self.add_callback)
    
    def add_callback(self, req, res):
        res.sum = req.num1 + req.num2
        self.get_logger().info(f"计算过程: {req.num1} + {req.num2} = {res.sum}")
        return res

def main(args=None):
    rclpy.init(args=args)
    server = Ser("Ser")
    rclpy.spin(server)
    rclpy.shutdown()
