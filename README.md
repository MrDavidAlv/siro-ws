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

### NODOS
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

### TOPICOS
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


##### Clasificación

En cuanto a los tipos de tópicos, no hay una clasificación específica de los tópicos en sí; más bien, los tópicos se definen por el tipo de mensajes que manejan y el propósito de los nodos que los utilizan.

1. **Tipos de mensajes estándar**:
ROS 2 proporciona una variedad de tipos de mensajes estándar definidos en varios paquetes como `std_msgs`, `geometry_msgs`, `sensor_msgs`, entre otros. Algunos ejemplos de mensajes estándar son:

  - **std_msgs**: Mensajes estándar.
    * **std_msgs/String**: Un mensaje de texto simple.
    * **std_msgs/Int32**: Un entero de 32 bits.
    * **std_msgs/Float32**: Un número de punto flotante de 32 bits.


  - **geometry_msgs**: Mensajes de geometría y movimiento.
    * **geometry_msgs/Point**
      - Representa un punto en un espacio tridimensional.
      - Contiene tres coordenadas: `x`, `y` y `z`.
      - *Ejemplo de uso*: Describir la posición de un objeto en un espacio 3D.
      ```
      geometry_msgs/Point {x: 1.0, y: 2.0, z: 3.0}
      ```
    
    * **geometry_msgs/Quaternion**
      - Representa una orientación en un espacio tridimensional utilizando un cuaternio.
      - Contiene cuatro componentes: `x`, `y`, `z`, y `w`.
      - *Ejemplo de uso*: Describir la orientación de un objeto en un espacio 3D.
      ```
      geometry_msgs/Quaternion {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
      ```

    * **geometry_msgs/Pose**
      - Representa la posición y la orientación de un objeto en un espacio tridimensional.
      - Combina `Point` y `Quaternion`.
      - *Ejemplo de uso*: Describir la pose de un robot o un objeto en un espacio 3D.
      ```
      geometry_msgs/Pose {position: {x: 1.0, y: 2.0, z: 3.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}
      ```

    * **geometry_msgs/Twist**
      - Representa el movimiento lineal y angular de un objeto.
      - *Contiene dos campos*: `linear` (un `Vector3` que describe la velocidad lineal) y `angular` (un `Vector3` que describe la velocidad angular).
      - *Ejemplo de uso*: Describir la velocidad de un robot o un objeto en un espacio 3D.
      ```
      geometry_msgs/Twist {linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}
      ```

    * **geometry_msgs/PoseStamped**
      - Similar a `Pose`, pero incluye un sello de tiempo (`header.stamp`) y un marco de referencia (`header.frame_id`).
      - Combina `Point` y `Quaternion`.
      - Se utiliza para describir la pose de un objeto en un determinado momento y marco de referencia.
      ```
      geometry_msgs/PoseStamped { header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"}, pose: {position: {x: 1.0, y: 2.0, z: 3.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}
      ```
    
    * **geometry_msgs/Transform**
      - Representa una transformación que consiste en una rotación (`rotation`, un `Quaternion`) y una traslación (`translation`, un `Vector3`).
      - *Ejemplo de uso*: Describir cómo se transforma un objeto en relación con otro.
      ```
      geometry_msgs/Transform {translation: {x: 1.0, y: 2.0, z: 3.0}, rotation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}
      ```

    * **geometry_msgs/Wrench**
      - Representa fuerzas lineales y torques angulares que actúan sobre un objeto, con campos `force` y `torque`, ambos de tipo `Vector3`.

  - **sensor_msgs**: Mensajes relacionados con sensores.

    * **sensor_msgs/LaserScan**
      - Representa los datos de un escáner láser (LiDAR).
      - Incluye información sobre el ángulo mínimo y máximo de escaneo, el rango mínimo y máximo de detección, el ángulo entre mediciones consecutivas, y una lista de distancias medidas (rangos).
      - *Ejemplo de uso*: Para recibir datos de un sensor LiDAR en un robot móvil.
      ```
      sensor_msgs/LaserScan {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_laser"},
        angle_min: -1.57,
        angle_max: 1.57,
        angle_increment: 0.01,
        time_increment: 0.0,
        scan_time: 0.0,
        range_min: 0.1,
        range_max: 10.0,
        ranges: [0.5, 0.6, 0.7, ...]
      }
      ```

    * **sensor_msgs/Imu**
      - Representa datos de una unidad de medida inercial (IMU).
      - Incluye datos de orientación (como cuaterniones), aceleración lineal y velocidad angular (tasa de giro).
      - Ejemplo de uso: Para recibir datos de un IMU en un dron o robot móvil.
      ```
      sensor_msgs/Imu {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "imu_link"},
        orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0},
        orientation_covariance: [0.0, 0.0, 0.0, ...],
        angular_velocity: {x: 0.1, y: -0.2, z: 0.3},
        angular_velocity_covariance: [0.0, 0.0, 0.0, ...],
        linear_acceleration: {x: 0.4, y: -0.5, z: 0.6},
        linear_acceleration_covariance: [0.0, 0.0, 0.0, ...]
      }
      ```
    * **sensor_msgs/CameraInfo**
      - Proporciona información sobre la configuración de una cámara, como la matriz de la cámara, el tamaño de la imagen y los coeficientes de distorsión.
      - *Ejemplo de uso*: Para enviar datos sobre la calibración de una cámara.
      ```
      sensor_msgs/CameraInfo {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "camera_frame"},
        height: 720,
        width: 1280,
        distortion_model: "plumb_bob",
        D: [0.1, -0.1, 0.0, 0.0, 0.0],
        K: [1000.0, 0.0, 640.0, ...],
        R: [1.0, 0.0, 0.0, ...],
        P: [1000.0, 0.0, 640.0, ...],
        binning_x: 1,
        binning_y: 1,
        roi: {x_offset: 0, y_offset: 0, height: 720, width: 1280, do_rectify: false}
      }
      ```
    * **sensor_msgs/PointCloud2**
      - Representa un conjunto de puntos tridimensionales (nube de puntos).
      - Se utiliza para representar datos de escaneo de superficies u objetos en 3D, por ejemplo, de un sensor LiDAR o de una cámara de profundidad.
      - *Ejemplo de uso*: Para enviar datos de una nube de puntos capturados por un sensor.
      ```
      sensor_msgs/PointCloud2 {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"},
        height: 1,
        width: 1000,
        fields: [{name: "x", offset: 0, datatype: 7, ...}, ...],
        point_step: 32,
        row_step: 32000,
        data: [...],
        is_bigendian: false,
        is_dense: true
      }
      ```

  - **nav_msgs**: Mensajes relacionados con la navegación robótica.
    * **nav_msgs/Odometry**
      - Representa datos de odometría, que describen la posición y orientación actual de un robot, así como sus velocidades lineales y angulares.
      - Incluye un `header` con un sello de tiempo y un marco de referencia (`frame_id`).
      - Contiene una `PoseWithCovariance` (pose con información de incertidumbre) y una `TwistWithCovariance` (velocidad con información de incertidumbre).
      ```
      nav_msgs/Odometry {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "odom"},
        child_frame_id: "base_link",
        pose: {
            pose: {position: {x: 1.0, y: 2.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}},
            covariance: [0.1, 0.0, 0.0, ...]
        },
        twist: {
            twist: {linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.1}},
            covariance: [0.1, 0.0, 0.0, ...]
        }
      }
      ```

    * **nav_msgs/Path**
      - Representa un camino o trayectoria que un robot puede seguir para navegar a través de un espacio.
      - Consiste en una lista de poses (`PoseStamped`) a lo largo de una trayectoria planificada.
      - *Ejemplo de uso*: Para especificar una ruta de navegación para un robot.
      ```
      nav_msgs/Path {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"},
        poses: [
            {header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"},
            pose: {position: {x: 1.0, y: 1.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}},
            {header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"},
            pose: {position: {x: 2.0, y: 2.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}
            // ...
        ]
      }
      ```

    * **nav_msgs/OccupancyGrid**
      - Representa un mapa de ocupación, que es una representación de un entorno en una cuadrícula bidimensional.
      - Cada celda de la cuadrícula contiene un valor que indica si está libre, ocupada o desconocida.
      - *Ejemplo de uso*: Para compartir un mapa de ocupación de un entorno con otros nodos o para planificar rutas.
      ```
      nav_msgs/OccupancyGrid {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"},
        info: {
            map_load_time: {sec: 0, nanosec: 0},
            resolution: 0.05,
            width: 100,
            height: 100,
            origin: {
                position: {x: -2.5, y: -2.5, z: 0.0},
                orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
            }
        },
        data: [0, 100, -1, ...] // Valores de ocupación para cada celda
      }
      ```

    * **nav_msgs/MapMetaData**
      - Proporciona metadatos sobre un mapa, como la resolución, el tamaño y la posición de la cuadrícula de ocupación.
      - Se usa en conjunto con mensajes como `OccupancyGrid`.
      ```
      nav_msgs/MapMetaData {
        map_load_time: {sec: 0, nanosec: 0},
        resolution: 0.05,
        width: 100,
        height: 100,
        origin: {
            position: {x: -2.5, y: -2.5, z: 0.0},
            orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
        }
    }
      ```
2. **Tipos de mensajes personalizados**: Además de los tipos de mensajes estándar, puedes definir tus propios tipos de mensajes personalizados para adaptarte a las necesidades específicas de tu aplicación. Los mensajes personalizados se crean utilizando el lenguaje de definición de mensajes (IDL) de ROS 2.

3. **Tipos de mensajes de servicios y acciones**: Además de los mensajes de tópicos, ROS 2 también tiene mensajes de servicios (srv) y acciones (action). Los servicios definen un tipo de solicitud y un tipo de respuesta, mientras que las acciones son una combinación de mensajes de objetivos, actualizaciones de estado y resultados.

4. **Mensajes de paquetes de terceros**: Además de los paquetes estándar, existen otros paquetes de ROS 2 desarrollados por la comunidad que proporcionan más tipos de mensajes para diferentes aplicaciones, como robótica, automoción, drones, etc.




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

7. Ver la extructura de mensaje enviada en el tópico.
```bash
ros2 interface show geometry_msgs/msg/Twist
```
Retorna la extructura.
```
# This expresses velocity in free space broken into its linear and angular parts.

Vector3  linear
        float64 x
        float64 y
        float64 z
Vector3  angular 
        float64 x
        float64 y
        float64 z
```
8. Publicar información a través del tópico.
```bash
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -2.0, y: 0.0, z: 0.0},
angular: {x: 0.0, y: 0.0, z: 1.5}}"
```

9. Publicar información a través del tópico con una determinada frecuencia.
```bash
ros2 topic pub --rate /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -2.0, y: 0.0, z: 0.0},
angular: {x: 0.0, y: 0.0, z: 1.5}}"
```
10. Para visualizar la frecuencia con la que un nodo publica.
```bash
ros2 topic hz /turtle1/cmd_vel
```
Retorna la velocidad de publicación.
```
average rate: 0.200
        min: 4.999s max: 5.001s std dev: 0.00058s window: 2
average rate: 0.200
        min: 4.999s max: 5.001s std dev: 0.00070s window: 3
average rate: 0.200
        min: 4.999s max: 5.001s std dev: 0.00090s window: 4
average rate: 0.200
```

<br>

### SERVICIOS

<br>

### PARAMETROS

<br>

#### ACCIONES

---
## REPASO DE MATRICES(Álgebra lineal)
## REPASO ROBÓTICA(Quaterniones, Transformadas, ...)

# Python es lento porque es interpretado


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






