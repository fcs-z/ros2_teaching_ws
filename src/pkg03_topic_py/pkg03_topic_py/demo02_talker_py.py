import rclpy
from rclpy.node import Node
from pkg00_interfaces.msg import Student

class Pub(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info("发送端已经启动")
        self.talker_ = self.create_publisher(Student,"topic_stu",10)
        self.timer_ = self.create_timer(0.5,self.timer_callback)
        self.count_ = 0

    def timer_callback(self):
        stu = Student()
        stu.name = "asd"
        stu.age = 1
        stu.height = 1.7
        stu.age = self.count_
        self.count_ += 1
        self.get_logger().info(f'发送学生信息： name = {stu.name}, age = {stu.age}, height = {stu.height}')
        self.talker_.publish(stu)

def main():
    rclpy.init()
    talker = Pub("pub")
    rclpy.spin(talker)
    rclpy.shutdown()