import rclpy
from rclpy.node import Node
from pkg00_interfaces.msg import Student

class Sub(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().error("接收端已经启动")
        self.listener_ = self.create_subscription(Student,"topic_stu",self.sub_callback,10)
        
    def sub_callback(self,stu):
        self.get_logger().error(f'收到学生信息: name = {stu.name}, age = {stu.age}, height = {stu.height}')

def main():
    rclpy.init()
    listener = Sub("sub")
    rclpy.spin(listener)
    rclpy.shutdown()