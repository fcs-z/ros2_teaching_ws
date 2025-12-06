import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info("helloworld")
        self.get_logger().error("helloworld")
        
def main():
    rclpy.init()
    node = MyNode("py_node")
    rclpy.spin(node)
    rclpy.shutdown()
    
