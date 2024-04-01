import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='python_siro',
            executable='siro_node_suscriptor.py',
            name='siro_node_suscriptor'
        ),
        Node(
            package='python_siro',
            executable='siro_node_publicador.py',
            name='siro_node_publicador'
        )
    ])
