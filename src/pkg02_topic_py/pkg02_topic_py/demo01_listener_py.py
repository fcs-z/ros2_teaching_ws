import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sub(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().error("接收端已经启动")
        self.listener_ = self.create_subscription(String,"topic",self.sub_callback,10)
        
    def sub_callback(self,msg):
        self.get_logger().error(f'收到消息:{msg.data}')
        # self.get_logger().warning(f'收到消息:{msg.data}')

def main():
    rclpy.init()
    listener = Sub("sub")
    rclpy.spin(listener)
    rclpy.shutdown()