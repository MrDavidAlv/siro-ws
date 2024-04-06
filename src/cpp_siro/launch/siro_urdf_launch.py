import launch
import launch_ros.actions
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Ruta al directorio donde se encuentra el paquete cpp_siro
    package_dir = '/home/axioma/siro-ws/src/cpp_siro'

    # Ruta al archivo URDF
    urdf_file = os.path.join(package_dir, 'urdf', 'siro_urdf.xml')

    # Argumentos para el nodo joint_state_publisher
    joint_state_publisher_node = launch_ros.actions.Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    # Argumentos para el nodo rviz2
    rviz2_node = launch_ros.actions.Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", os.path.join(package_dir, 'rviz', 'siro_rviz_config.rviz')],
    )

    # Argumentos para el nodo que carga el URDF
    urdf_spawner_node = launch_ros.actions.Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": open(urdf_file).read()}],
    )

    return launch.LaunchDescription([
        urdf_spawner_node,
        joint_state_publisher_node,
        rviz2_node,
    ])
