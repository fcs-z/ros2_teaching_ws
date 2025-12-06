import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Pub(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info("发送端已经启动")
        self.talker_ = self.create_publisher(String,"topic",10)
        self.timer_ = self.create_timer(0.5,self.timer_callback)
        self.count_ = 0

    def timer_callback(self):
        msg = String()
        msg.data = "hi"+f':{self.count_}'
        self.get_logger().info(f'发送消息：{msg.data}')
        self.count_ += 1
        self.talker_.publish(msg)

def main():
    rclpy.init()
    talker = Pub("pub")
    rclpy.spin(talker)
    rclpy.shutdown()