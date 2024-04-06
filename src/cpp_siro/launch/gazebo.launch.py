import launch
import launch.actions
import launch_ros.actions
import os

def generate_launch_description():
    # Ruta al directorio donde se encuentra el paquete cpp_siro
    package_dir = '/home/jj/siro_ws/src/cpp_siro'

    # Ruta al archivo URDF
    urdf_file = os.path.join(package_dir, 'urdf', 'siro_urdf.xml')

    # Configurar el nodo de Gazebo
    gazebo_node = launch.actions.ExecuteProcess(
        cmd=['gazebo'],
        output='screen'
    )

    # Argumentos para el nodo que carga el URDF en Gazebo
    spawn_entity_node = launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'siro_robot', '-file', urdf_file],
        output='screen'
    )

    return launch.LaunchDescription([
        gazebo_node,
        spawn_entity_node
    ])
