# Lanzaderas en ROS 2

Los lanzamientos en ROS 2 son archivos de configuración que permiten iniciar y coordinar múltiples nodos y acciones de manera simultánea. Son esenciales para configurar sistemas robóticos complejos de manera eficiente y automatizada.

## ¿Qué es un lanzamiento?

Un lanzamiento es un archivo de configuración en ROS 2 que describe cómo iniciar y coordinar nodos y acciones relacionadas. Puedes pensar en un lanzamiento como un script que automatiza la configuración y ejecución de un sistema robótico.

## Componentes de un archivo de lanzamiento

Un archivo de lanzamiento generalmente consta de las siguientes partes:

1. **Importaciones de módulos**: Al principio del archivo, se importan los módulos necesarios de ROS 2 para crear y configurar los lanzamientos.

2. **Definición de la función `generate_launch_description`**: Esta función es el punto de entrada del archivo de lanzamiento y devuelve una descripción del lanzamiento. Aquí es donde se configuran todos los nodos y acciones que se iniciarán.

3. **Configuración de nodos y acciones**: Dentro de la función `generate_launch_description`, se configuran todos los nodos y acciones que se desean iniciar durante el lanzamiento. Esto puede incluir nodos ROS, ejecutables de ROS 2, servicios, acciones, etc.

4. **Retorno de la descripción del lanzamiento**: Finalmente, se retorna la descripción del lanzamiento al final de la función `generate_launch_description`.

## Ejemplo: `siro_urdf_launch.py`

A continuación, se muestra un ejemplo de un archivo de lanzamiento que inicia un URDF en Gazebo y otros nodos relacionados:

---

### Importaciones de módulos

```python
import launch
import launch_ros.actions
import os
```

En este fragmento de código, importamos los módulos necesarios de ROS 2 y del sistema operativo para trabajar con lanzamientos y manipular archivos.

### Definición de la función generate_launch_description

```python
def generate_launch_description():
    # Contenido de la función

```
Aquí definimos la función generate_launch_description, que es el punto de entrada del archivo de lanzamiento y donde configuraremos nuestros nodos y acciones.

### Configuración de nodos y acciones

```python
# Ruta al paquete y archivo URDF
package_dir = '/home/jj/siro_ws/src/cpp_siro'
urdf_file = os.path.join(package_dir, 'urdf', 'siro_urdf.xml')

```
En esta parte, especificamos la ruta al paquete y al archivo URDF que queremos cargar en Gazebo.

```python
# Creación de nodos
joint_state_publisher_node = launch_ros.actions.Node(
    package="joint_state_publisher_gui",
    executable="joint_state_publisher_gui",
)

rviz2_node = launch_ros.actions.Node(
    package="rviz2",
    executable="rviz2",
    arguments=["-d", os.path.join(package_dir, 'rviz', 'default.rviz')],
)

```
Aquí creamos nodos para el publicador de estados conjuntos y RViz.

### Retorno de la descripción del lanzamiento

```python
return launch.LaunchDescription([
    joint_state_publisher_node,
    rviz2_node,
])
```
Finalmente, retornamos la descripción del lanzamiento que contiene todos los nodos y acciones configurados.

### [`atras`](./../)        [`siro_ws`](./../../../)

