## Creación de nodos


1. Para crear un nodo, nos ubicamos en el direcorio `src` del paquete.


    ### `cd siro_ws/src/cpp_siro/src`


2. creamos un nodo de publicación `siro_node_publicador.cpp` que va a estar publicando en el tópico `chatter`


    Escribimos el código del nodo.


3. Creamos un nodo de publicación `siro_node_suscriptor.cpp` que va a estar suscrito al tópico `chatter`


    Escribimos el código del nodo.


4. Configurar el archivo `CMakeList.txt`


    Configurar la versión y el nombre del paquete.
    ```
    cmake_minimum_required(VERSION 3.5)
    project(cpp_siro)
    ```


    Especificar la versión de C++
    ```
    # Default to C++14
    if(NOT CMAKE_CXX_STANDARD)
        set(CMAKE_CXX_STANDARD 14)
    endif()
    ```


    Especificar dependencias del paquete `ament_cmake`, `rclcpp` y `std_msgs`


    Cramos los nodos como ejecutables.
    ```
    # Agrega el ejecutable del nodo.
    add_executable(siro_node_suscriptor src/siro_node_suscriptor.cpp)
    add_executable(siro_node_publicador src/siro_node_publicador.cpp)
    ```


    Instalar las dependencias de los nodos.
    ```
    # Especifica las dependencias para el ejecutable.
    ament_target_dependencies(siro_node_suscriptor rclcpp std_msgs)
    ament_target_dependencies(siro_node_publicador rclcpp std_msgs)


    ```


    Instalar los nodos.
    ```
    # Instala el ejecutable.
    install(TARGETS
        siro_node_suscriptor
        siro_node_publicador
        DESTINATION lib/${PROJECT_NAME}
    )
    ```


   Creación de un directorio `/launch` para crear lanzaderas y compilacion.


    ```
    # Instala los scripts y los recursos.
    install(DIRECTORY
        launch
        DESTINATION share/${PROJECT_NAME}
    )


    ament_package()
    ```



5. Compilar el proyecto.


Ir a la raíz del proyecto


### `cd /siro_ws`


Compilar


### `colcon build`


```
Starting >>> cpp_siro
Finished <<< cpp_siro [0.21s]


Summary: 1 package finished [0.52s]


```


6. Compilar fuentes del proyecto.


### `source install/setup.bash`


7. Correr nodos.


Nodo publicador.


### `ros2 run cpp_siro siro_node_publicador`


```
[INFO] [1711217642.774303167] [siro_node_publicador]: Publicando: '¡Hola desde siro_node_publicador!'
[INFO] [1711217643.774279461] [siro_node_publicador]: Publicando: '¡Hola desde siro_node_publicador!'
[INFO] [1711217644.774280965] [siro_node_publicador]: Publicando: '¡Hola desde siro_node_publicador!'
[INFO] [1711217645.774667996] [siro_node_publicador]: Publicando: '¡Hola desde siro_node_publicador!'
.
.
.
...
```


Nodo suscriptor.


### `ros2 run cpp_siro siro_node_suscriptor`
```
[INFO] [1711217789.714065951] [siro_node_suscriptor]: Mensaje recibido: '¡Hola desde siro_node_publicador!'
[INFO] [1711217790.127715513] [siro_node_suscriptor]: Esperando mensajes...
[INFO] [1711217790.713996754] [siro_node_suscriptor]: Mensaje recibido: '¡Hola desde siro_node_publicador!'
[INFO] [1711217791.127714843] [siro_node_suscriptor]: Esperando mensajes...
[INFO] [1711217791.714009715] [siro_node_suscriptor]: Mensaje recibido: '¡Hola desde siro_node_publicador!'
.
.
.
...
```'