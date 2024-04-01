import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Lanzar el nodo turtlesim
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node'
        ),

        # Lanzar rqt_robot_steering
        ExecuteProcess(
            cmd=['rqt_robot_steering'],
            output='screen'
        )
    ])
