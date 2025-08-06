from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    # 获取默认的urdf、rviz路径
    urdf_package_path = get_package_share_directory('orcahand_description')
    urdf_path = os.path.join(urdf_package_path,'urdf','orcahand_right.urdf')
    rviz_config_path = os.path.join(urdf_package_path,'config','display_orcahand.rviz')
    # get_package_share_directory 查找包的路径
    # os.path.join()拼接路径成完整路径

    # 读取urdf文件内容
    with open(urdf_path, 'r') as infp:
        urdf_content = infp.read()
   
    # 发布机器人状态的节点
    action_robot_state_publisher = Node(
        package = 'robot_state_publisher', # 包的名字
        executable = 'robot_state_publisher', # 可执行文件
        name = 'robot_state_publisher', # 节点名字
        parameters = [{'robot_description':urdf_content}] # 传递ROS参数
    )

    # 发布rviz节点
    action_rviz_node = Node(
        package = 'rviz2',
        executable = 'rviz2',
        arguments = ['-d',rviz_config_path] if os.path.exists(rviz_config_path) else [] # 传递命令行参数，打开rviz文件
    )
    
    # 发布关节状态
    action_joint_state_publisher = Node(
        package = 'joint_state_publisher_gui',
        executable = 'joint_state_publisher_gui',
    )

    # 打包返回
    return LaunchDescription([
        action_robot_state_publisher,
        action_rviz_node,
        action_joint_state_publisher
    ])