import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.subscription = self.create_subscription(Float32, 'sensor_x_readings', self.listener_callback, 10)

    def listener_callback(self, msg):
        if msg.data > 0.5:
            self.get_logger().info(f'ALERT: High Reading {msg.data}')
        else:
            self.get_logger().info(f'Reading OK: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

