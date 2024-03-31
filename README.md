# PROYECTO ROS2 HUMBLE


ROS 2 (Robot Operating System 2) es una plataforma de código abierto diseñada para facilitar el desarrollo, operación y mantenimiento de sistemas robóticos y de automatización industrial. Ofrece una arquitectura modular y flexible que permite la comunicación entre componentes distribuidos, soportando una variedad de sistemas operativos y arquitecturas de hardware. ROS 2 se destaca por su capacidad de escalabilidad, seguridad y robustez, lo que lo convierte en una herramienta crucial para la creación de sistemas robóticos avanzados en diversos entornos industriales y de investigación.


## Preparación del espacio de trabajo


### Creación del proyecto Ros2


1. Creación del workspace.


    ### `mkdir -p siro_ws/src`


2. Ingresamos a `siro_ws`


    ### `cd siro_ws`


3. Compilación del proyecto


    ### `colcon build`













    Se crearon las carpetas de compilación de este proyecto.


    ```
    /build
    /install
    /log
    ```


4. Ingresar al directorio `src`


    ### `cd src`


5. Creación de paquete con ament_cmake `cpp_siro`


    ### `ros2 pkg create --build-type ament_cmake cpp_siro`


    Se crea la carpeta del paquete `cpp_siro`
   Que es la que contiene los archivos de compilación del paquete y archivos de dependecias e información.


    ```
    /cpp_siro
    ```


6. Ingresamos a la carpeta del paquete.


    ### `cd cpp_siro`


   Aquí encontramos varios documentos y directorios.


    ```
    /include
    /cpp_siro
    CMakeList.txt
    package.xml
    ```


    En el directorio `incluede` se guardan archivos necesarios para la compilacion.


    En el directorio `cpp_siro` se Gurdan los nodos.


    El archivo `CMakeList.txt` guarda la configuración para la del paquete como dependencias, registro de nodos, directorios, versión de C++,...


    El archivo `packeage.xml` contiene información del paquete como la descripción, el autor, el contacto, dependencias y herramientas.



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
```