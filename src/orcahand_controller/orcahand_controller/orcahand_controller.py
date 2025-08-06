#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import os
from orca_core import Orcahand
from sensor_msgs.msg import JointState

class OrcahandController(Node):
    def __init__(self):
        super().__init__('orcahand_controller_node')
        self.joint_satate_publisher_ = self.create_publisher(JointState,'joint_states',10)
        self.timer = self.create_timer(0.1,self.pubish_joint_states)
        self.get_logger().info('orcahand_controller is ready!')

    def pubish_joint_states(self):
        """定时器调用的函数，发布JointState消息."""
        joint_state_msg = JointState() # 初始化JointState消息对象
        joint_state_msg.header.stamp = self.get_clock().now().to_msg() # 设置时间戳
