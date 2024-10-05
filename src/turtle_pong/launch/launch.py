import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Nodo 'pong' del paquete 'turtle_pong'
        Node(
            package='turtle_pong',
            executable='pong',
            name='pong',
            output='screen'
        ),
        # Nodo 'turtle_pong_ball' del paquete 'turtle_pong'
        Node(
            package='turtle_pong',
            executable='turtle_pong_ball',
            name='ball',
            output='screen'
        ),
        # Nodo 'teleop_turtle' del paquete 'turtle_pong'
        Node(
            package='turtle_pong',
            executable='teleop_turtle',
            name='key',
            output='screen'
        )
    ])
