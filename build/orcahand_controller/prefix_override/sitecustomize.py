import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/xingyi/ros2_orcahand/ros2_orcahand_ws/install/orcahand_controller'
