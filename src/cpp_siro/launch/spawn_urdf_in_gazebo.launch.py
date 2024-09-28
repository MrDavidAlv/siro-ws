import launch
import launch_ros.actions
import os

def generate_launch_description():
    # Ruta al directorio donde se encuentra el paquete cpp_siro
    package_dir = '/home/jj/siro_ws/src/cpp_siro'

    # Ruta al archivo URDF
    urdf_file = os.path.join(package_dir, 'urdf', 'siro_urdf.xml')

    # Argumentos para el nodo rviz2
    rviz2_node = launch_ros.actions.Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", os.path.join(package_dir, 'rviz', 'default.rviz')],
    )

    # Argumentos para el nodo que carga el URDF en Gazebo
    gazebo_launch_description = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(package_dir, 'launch', 'spawn_urdf_in_gazebo.launch.py')
        ),
        launch_arguments={'urdf_file': urdf_file}.items(),
    )

    return launch.LaunchDescription([
        gazebo_launch_description,
        rviz2_node,
    ])
