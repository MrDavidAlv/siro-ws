from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command

def generate_launch_description():
    xacro_file = os.path.join(get_package_share_directory('siro_arm'), 'urdf', 'siro_arm.xacro')

    robot_description = Command(['xacro ', xacro_file])

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
        Node(
            package='siro_arm',
            executable='joystick_to_joint_publisher',
            name='joystick_to_joint_publisher',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory('siro_arm'), 'config', 'siro_arm.rviz')],
        )
    ])
