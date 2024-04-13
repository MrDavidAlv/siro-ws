# 🎯PROYECTO ROS2 HUMBLE 🤖🚀🕹️


<!--div id="header" align="center" style="text-align: center; white-space: nowrap">
    <img src="/images/ros2.gif" title="ros2" alt="ros2" width="300px"/>
    <img src="/images/humble.png" title="humble" alt="humble" width="150px"/>
</div-->

<div id="header" align="center">
    <img src="/images/ros-image2.png" alt="ros humble" width="60%" max-width="100%">
</div>


`ROS2` (Robot Operating System 2) es una plataforma de código abierto diseñada para facilitar el desarrollo, operación y mantenimiento de sistemas robóticos y de automatización industrial. Ofrece una arquitectura modular y flexible que permite la comunicación entre componentes distribuidos, soportando una variedad de sistemas operativos y arquitecturas de hardware. ROS 2 se destaca por su capacidad de escalabilidad, seguridad y robustez, lo que lo convierte en una herramienta crucial para la creación de sistemas robóticos avanzados en diversos entornos industriales y de investigación.

### Historia

**ROS** en su primera versión, **ROS1**, se desarrolló en los Laboratorios de Inteligencia Artificial de Stanford (SAIL) por estudiantes de doctorado **Eric Berger** y **Keenan Wyrobek**. Se publicó bajo una **licencia BSD** de software libre en 2007, que permite libertad para uso comercial e investigador. Desde 2008, el instituto **Willow Garage** se ha encargado principalmente del desarrollo y soporte.

La idea de crear un sistema operativo era estandarizar tareas como la *abstracción de hardware*, *control de dispositivos* de bajo nivel (drivers), implementación de *procesos comunes*, manejo de *comunicación*, *soporte* de paquetes y otras ventajas.

**ROS2** es la evolución natural del exitoso marco de trabajo **ROS1**. Desarrollado para abordar las limitaciones de su predecesor, ROS2 ofrece una *arquitectura modular* y *distribuida*, mejor *rendimiento* y *escalabilidad*, así como soporte *multiplataforma*. Lanzado oficialmente en 2015, ROS2 mantiene la *flexibilidad* y *robustez* de ROS1, al tiempo que introduce mejoras significativas en herramientas de desarrollo y comunicación. Su diseño modular permite una fácil integración con otros sistemas y una adaptación más rápida a diferentes entornos de desarrollo. Con características como compatibilidad con múltiples lenguajes de programación y una creciente comunidad de desarrolladores, ROS2 es la elección preferida para proyectos de robótica modernos y ambiciosos.

#### Filosofía
*"ROS, nacido del corazón del código abierto, ofrece libertad y flexibilidad para que los usuarios moldeen su propia realidad robótica, trazando un camino lleno de posibilidades infinitas en el vasto horizonte de la tecnología"*.


#### DIFERENCIAS 

| Característica               | ROS 1                                                          | ROS 2                                                              |
|------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------|
| **Arquitectura**             | Basada en un sistema de nodos con comunicación XML-RPC y TCP/IP | Arquitectura modular y distribuida, comunicación basada en DDS    |
| **Lenguajes de Programación**| Soporte para C++, Python, Lisp, entre otros                   | Soporte para varios lenguajes, incluyendo C++, Python, y más      |
| **Rendimiento**              | Limitaciones en rendimiento, seguridad y escalabilidad         | Mejoras significativas en rendimiento, seguridad y escalabilidad  |
| **Multiplataforma**          | Principalmente enfocado en Linux                               | Soporte multiplataforma incluyendo Linux, Windows, y macOS        |
| **Herramientas**             | Herramientas de desarrollo y depuración limitadas              | Mejoras en herramientas de depuración, simulación, y gestión de paquetes |
| **Compatibilidad**           | No es directamente compatible con ROS 2                        | Introduce puentes y herramientas de migración para la compatibilidad con ROS 1 |
| **Ecosistema**               | Ecosistema consolidado con una amplia comunidad                 | Ecosistema en constante crecimiento con una creciente comunidad de desarrolladores |


## Arquitectura ROS2
La arquitectura de ROS2 se ha diseñado para abordar las limitaciones de ROS1 y proporcionar una plataforma más flexible, escalable y robusta para el desarrollo de aplicaciones robóticas. A continuación, se proporciona una explicación paso a paso de la arquitectura de ROS2:

| Paso  | Descripción  |
|-------|----------------|
| 1. Arquitectura Modular y Distribuida | ROS 2 se basa en una arquitectura modular y distribuida, donde los nodos son componentes independientes que pueden ejecutarse de manera separada.          |
| 2. Comunicación Basada en DDS | Utiliza DDS para la comunicación entre nodos, ofreciendo un rendimiento superior, mayor seguridad y mejor escalabilidad que el sistema de ROS 1.            |
| 3. Nodos                     | Cada nodo en ROS 2 es un proceso independiente que realiza una tarea específica y se comunica con otros nodos intercambiando mensajes a través de DDS.     |
| 4. Middleware (DDS)          | DDS actúa como el middleware que facilita la comunicación entre nodos, proporcionando mecanismos eficientes para la publicación y suscripción de mensajes. |
| 5. Interfaces de Mensajería (IDL) | Utiliza interfaces de definición de lenguaje (IDL) para describir la estructura de los mensajes que se intercambian entre nodos.                        |
| 6. Gestión de Recursos       | Incluye una capa de gestión de recursos para asignar y administrar eficientemente los recursos del sistema, como memoria y procesamiento.                   |
| 7. Soporte Multiplataforma   | Diseñado para ser ejecutado en una variedad de sistemas operativos, incluyendo Linux, Windows y macOS, lo que proporciona mayor flexibilidad y portabilidad.  |


En resumen, la arquitectura de ROS2 se caracteriza por su modularidad, su sistema de comunicación basado en DDS, su soporte multiplataforma y su capacidad para gestionar eficientemente los recursos del sistema. Estas características hacen de ROS2 una plataforma poderosa y versátil para el desarrollo de aplicaciones robóticas modernas.


<div id="header" align="center">
    <img src="/images/arquitectura.png" alt="Arquitectura de ros" width="50%" max-width="100%">
</div>

<br>

#### NODOS
Los nodos son bloques de código (clases) que se encargan de partes específicas de las actividades del robot. Estos se van a enlazar mediante tópicos, servicios o acciones. Básicamente nos ayudan a crear un sistema modular que se pueda modificar fácilmente y comunicar.

##### Comandos básicos
Usaremos el paquete turtlesim que puedes instalar [`aquí`](./turtlesim/README.md).

1. Ejecutar un nodo.
```bash
ros2 run turtlesim turtlesim_node
```
En este caso lanzamos el nodo que mediante rqt lanza una interfaz gráfica con una tortuga en unas coordenadas especificas.

<div id="header" align="center">
    <img src="/images/turtlesim_node.png" alt="turtlesim_node" width="50%" max-width="100%">
</div>

En una nueva consola ejecutamos un segundo nodo.
```bash
ros2 run turtlesim turtle_teleop_key
```
2. Para visualizar los nodos en ejecución:
```bash
ros2 node list
```
Lo cual nos mostrara que hay dos nodos en ejecución

```
/teleop_turtle
/turtlesim
```

3. Podemos cambiar los parámetros y argumentos en los nodos. Por ejemplo, cambiar el nombre del nodo `turtlesim` a `myturtle`, para ello vamos a abrir una nueva consola y ejecutar
```bash
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=myturtle
```
Visualizamos nuevamente los nodos en ejecucón
```bash
ros2 node list
```
En este caso nos aparecen tres nodos en ejecución
```
/myturtle
/teleop_turtle
/turtlesim
```
4. **Información de un nodo**:  A veces se hace necesario conocer la información de un nodo para ver las suscripciones, qué está publicando, los servicios clientes, los servicios servidores y las acciones. Podemos ver la información de esta manera.
```bash
ros2 node info /turtlesim
```
En este caso vemos la información del nodo `/turtlesim`
```
/turtlesim
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
    /turtlesim/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /turtlesim/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /turtlesim/get_parameters: rcl_interfaces/srv/GetParameters
    /turtlesim/list_parameters: rcl_interfaces/srv/ListParameters
    /turtlesim/set_parameters: rcl_interfaces/srv/SetParameters
    /turtlesim/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```

<br>

#### TOPICOS
Son canales en los cuales unos nodos publican información y otros se suscriben para recibirla. La relación para la comunicación puede ser de  *muchos a uno*(one to many), *muchos a uno*(many to one) y *muchos a muchos*(many to many).

##### Caraterísticas de los tópicos
- **Definición de Tópicos**:
Canales de comunicación identificados por un nombre único.
- **Tipos de Mensajes**:
Los mensajes transmitidos a través de los tópicos pueden ser de tipos estándar (std_msgs) o personalizados.
- **Publicación y Suscripción**:
Los nodos pueden publicar o suscribirse a un tópico para enviar o recibir mensajes.
- **Comunicación Desacoplada**:
La comunicación se realiza de forma asíncrona y desacoplada entre nodos.
- **Calidad de Servicio (QoS)**:
Configuraciones de QoS permiten ajustar la durabilidad, fiabilidad, latencia, entre otros aspectos de la comunicación.
- **Jerarquía de Nombres de los Tópicos**:
Los nombres de los tópicos pueden ser jerárquicos para organizar la información.
- **Tópicos Privados**:
Los nodos pueden usar tópicos privados para encapsular la comunicación dentro de un nodo o grupo de nodos.
- **Herramientas para Trabajar con Tópicos**:
Herramientas como `ros2 topic list` y `ros2 topic echo` permiten gestionar y monitorear los tópicos.

En cuanto a los tipos de tópicos, no hay una clasificación específica de los tópicos en sí; más bien, los tópicos se definen por el tipo de mensajes que manejan y el propósito de los nodos que los utilizan.


##### Comandos básicos
1. Para ver los topicos de los nodos `turtlesim` y `teleop_key` que previamente deben estar ejecución usamos la siguiente instrucción

```bash
ros2 topic list
```

Esto nos indica que deben estar ejecutándose estos tópicos.
```
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

> **Nota**: Los tópicos `/parameter_events` y `/rosout` son de la ejecución de ROS2 y no pertenecen a los paquetes y nodos en ejecución, por lo tanto, siempre van a estar presentes.

2. Otra herramienta útil para el desarrollo de los tópicos con ROS2 es saber el tipo de los tópicos.
```bash
ros2 topic list -t
```
Y nos muestra la siguiente información.
```
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/rosout [rcl_interfaces/msg/Log]
/turtle1/cmd_vel [geometry_msgs/msg/Twist]
/turtle1/color_sensor [turtlesim/msg/Color]
/turtle1/pose [turtlesim/msg/Pose]
```

3. Durante la instalación, se descargó una herramienta útil para visualizar la conexión de los nodos, tópicos, servicios y acciones de nuestro proyecto. Para visualizar la arquitectura del proyecto, podemos usar el comando.
```bash
rqt_graph
```
Y nos habilita la ventana para ver el **rqt_graph**.
<div id="header" align="center">
    <img src="/images/rqt_graph.PNG" alt="rqt_graph" width="50%" max-width="100%">
</div>

4. Para visualizar el flujo de información de un tópico `cmd_vel` usamos el siguiente comando.
```bash
ros2 topic echo  /turtle1/cmd_vel
```
Esto nos habilitará información enviada a travás del tópico `/turtle/cmd_vel`.

```
linear:
  x: 2.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
---
```

5. Tambien podemos ver la información del tópico pose `pose`.
```bash
ros2 topic echo  /turtle1/pose
```
Nos imprimira la posición y ángulo de la tortuga.
```
x: 5.544444561004639
y: 5.544444561004639
theta: 0.0
linear_velocity: 0.0
angular_velocity: 0.0
---
```

6. En el caso de querer ver la información de un tópico usamos:
```bash
ros2 topic info /turtle1/cmd_vel
```

Lo cual nos retorna el tipo de nodo, número de nodos suscritos y número de nodos publicando.
```
Type: geometry_msgs/msg/Twist
Publisher count: 1
Subscription count: 1
```

<br>

#### SERVICIOS

<br>

#### ACCIONES



Nodes

Discovery

Interfaces

Topics

Services

Actions

Parameters

Introspection with command line tools

Launch

Client libraries


## [`👉 Instalación 🛠️`](./INSTALL.md)

<br>
<br>
<br>

## [`👉 Simulador Turtlesim`](./turtlesim/)


## Preparación del espacio de trabajo


### Creación del proyecto Ros2


1. Creación del workspace.

### `mkdir -p siro_ws/src`

2. Ingresamos a `siro_ws`

### `cd siro_ws`

3. Compilación del proyecto

### `colcon build`


Al compilar se crean 3 direcorios nuevos
```
    \build
    \install
    \log
```

4. Actualizar las fuentes compiladas 

### `source install/setup.bash`


Realizar el paso 3 y 4 cada vez que se realice un cambio

## [`👉 Crea paquetes en ROS2`](./src/)

--






