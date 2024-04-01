import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cpp_siro',
            executable='siro_node_publicador',
            name='siro_node_publicador'
        ),
        Node(
            package='cpp_siro',
            executable='siro_node_suscriptor',
            name='siro_node_suscriptor'
        )
    ])
