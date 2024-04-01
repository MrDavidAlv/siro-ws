# TurtleSim
TurtleSim es una aplicación de simulación en ROS2 que te permite controlar una tortuga virtual en un entorno 2D. Es una herramienta útil para aprender los conceptos básicos de ROS2 y realizar pruebas de concepto en un entorno de simulación.

<div id="header" align="center">
    <img src="/images/turtlesim_node.png" alt="Descripción de la imagen" width="60%" max-width="800px">
</div>

### Instalación
Para instalar TurtleSim en ROS2, puedes usar:

### `sudo apt install ros-humble-turtlesim`

Esto instalará TurtleSim junto con otras dependencias necesarias en tu sistema.

## Nodos en TurtleSim
Descripción
TurtleSim en ROS2 consta de varios nodos que interactúan para controlar el movimiento de la tortuga y visualizar su posición en la pantalla.

### Comandos
Para ver los nodos en ejecución en TurtleSim en ROS2, utiliza:

### `ros2 node list`

Esto mostrará una lista de todos los nodos en ejecución en el sistema ROS2. Puedes esperar ver nodos como turtlesim, teleop_turtle, etc.

Para obtener más información sobre un nodo específico, puedes usar:

### `ros2 node info /nombre_del_nodo`

Reemplaza `/nombre_del_nodo` con el nombre del nodo que desees inspeccionar.

## Tópicos en TurtleSim

### Descripción
Los tópicos en TurtleSim se utilizan para enviar y recibir comandos de movimiento de la tortuga, así como para recibir actualizaciones sobre su posición.

### Comandos
Para ver todos los tópicos disponibles en TurtleSim en ROS2, puedes usar:

### `ros2 topic list`
Esto mostrará una lista de todos los tópicos activos en el sistema ROS2. Busca tópicos como `/turtle1/cmd_vel`, `/turtle1/pose`, etc.

Para obtener más información sobre un tópico específico, puedes utilizar:

### `ros2 topic info /nombre_del_tópico`
Reemplaza `/nombre_del_tópico` con el nombre del tópico que desees inspeccionar.

Para ver los mensajes que se publican en un tópico en tiempo real, puedes usar:

### `ros2 topic echo /nombre_del_tópico`
Esto mostrará los mensajes publicados en el tópico especificado.

## Servicios en TurtleSim

### Descripción
TurtleSim en ROS2 proporciona servicios que permiten realizar acciones como cambiar la forma de la tortuga o reiniciar su posición.

### Comandos
Para ver todos los servicios disponibles en TurtleSim en ROS2, puedes usar:

### `ros2 service list`
Esto mostrará una lista de todos los servicios activos en el sistema ROS2. Busca servicios como `/clear`, `/spawn`, etc.

Para obtener más información sobre un servicio específico, puedes utilizar:

### `ros2 service info /nombre_del_servicio`
Reemplaza `/nombre_del_servicio` con el nombre del servicio que desees inspeccionar.

Para llamar a un servicio y ejecutar una acción, puedes utilizar:

### `ros2 service call /nombre_del_servicio argumentos`
Reemplaza `/nombre_del_servicio` con el nombre del servicio que desees llamar y proporciona los argumentos necesarios según lo requiera el servicio.

## Acciones en TurtleSim

### Descripción
TurtleSim en ROS2 también proporciona acciones que permiten realizar tareas complejas de manera asincrónica, como mover la tortuga hacia una ubicación específica.

### Comandos
Para ver todos los servidores de acción disponibles en TurtleSim en ROS2, puedes usar:

### `ros2 action list`
Esto mostrará una lista de todos los servidores de acción activos en el sistema ROS2. Busca servidores de acción como `/turtle1/rotate_absolute`, `/turtle1/teleport_absolute`, etc.

Para obtener más información sobre un servidor de acción específico, puedes utilizar:

### `ros2 action info /nombre_del_servidor_de_acción`
Reemplaza `/nombre_del_servidor_de_acción` con el nombre del servidor de acción que desees inspeccionar.

Para enviar una solicitud de acción a un servidor de acción, puedes utilizar:

### `ros2 action send_goal /nombre_del_servidor_de_acción argumentos `
Reemplaza `/nombre_del_servidor_de_acción` con el nombre del servidor de acción que desees llamar y proporciona los argumentos necesarios según lo requiera el servicio.

Conclusión
TurtleSim en ROS2 es una herramienta valiosa para aprender y experimentar con ROS2. Con esta guía, deberías tener una comprensión más profunda de los nodos, tópicos, servicios y acciones en TurtleSim, así como los comandos para interactuar con ellos. ¡Disfruta explorando y controlando la tortuga virtual en ROS2!