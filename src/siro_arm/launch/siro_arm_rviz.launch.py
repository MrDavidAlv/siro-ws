from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    #xacro_file = os.path.join(get_package_share_directory('siro_arm'), 'urdf', 'arm2.xacro')
    urdf_file = os.path.join(get_package_share_directory('siro_arm'), 'urdf', 'arm1.urdf')

    return LaunchDescription([
        # Node(
        #     package='xacro',
        #     executable='xacro',
        #     name='xacro',
        #     output='screen',
        #     arguments=[xacro_file, '-o', urdf_file]
        # ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory('siro_arm'), 'config', 'siro_arm.rviz')],
        )
    ])
