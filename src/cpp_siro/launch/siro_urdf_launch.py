import launch
import launch_ros.actions
import os

def generate_launch_description():
    # Ruta al directorio donde se encuentra el paquete cpp_siro
    package_dir = '/home/jj/siro-ws/src/cpp_siro'

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
        arguments=["-d", os.path.join(package_dir, 'rviz', 'default.rviz')],
    )

    return launch.LaunchDescription([
        #gazebo_node,
        joint_state_publisher_node,
        rviz2_node,
    ])
