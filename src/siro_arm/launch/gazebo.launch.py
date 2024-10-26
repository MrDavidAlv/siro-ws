from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
import os

def generate_launch_description():
    # Definir rutas de los archivos y paquetes
    package_name = 'siro_arm'
    xacro_file = os.path.join(get_package_share_directory(package_name), 'urdf', 'siro_arm.xacro')
    sdf_file = os.path.join(get_package_share_directory(package_name), 'models', 'siro_arm.sdf')
    rviz_config_file = os.path.join(get_package_share_directory(package_name), 'config', 'siro_arm.rviz')

    # Comando para procesar el archivo Xacro
    robot_description = Command(['xacro ', xacro_file])

    # Nodo para Rviz
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file]
    )

    # Nodo para el robot_state_publisher (procesa el Xacro en ROS2)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # Nodo de Gazebo para cargar el SDF
    gazebo_launch = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    launch_arguments={'world': os.path.join(get_package_share_directory('siro_arm'), 'worlds', 'siro_world.sdf')}.items()
)

    # Nodo de control del brazo (reemplaza 'control_node' por el nombre de tu ejecutable de control)
    control_node = Node(
        package=package_name,
        executable='joystick_to_joint_publisher',  # Reemplaza este nombre si tu ejecutable es diferente
        name='joystick_to_joint_publisher',
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        rviz_node,
        gazebo_launch,
        control_node
    ])
