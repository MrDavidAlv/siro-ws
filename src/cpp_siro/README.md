## PAQUETES CON ament_cmake(C++)

Creación de paquete con ament_cmake `cpp_siro`

### `ros2 pkg create --build-type ament_cmake cpp_siro`

Se crea la carpeta del paquete `cpp_siro`
Que es la que contiene los archivos de compilación del paquete y archivos de dependecias e información.

```
    /cpp_siro
```

Ingresamos a la carpeta del paquete.

### `cd cpp_siro`

Aquí encontramos varios documentos y directorios.

```
    /include
    /cpp_siro
    CMakeList.txt
    package.xml
```


1. `package.xml`: Este archivo es esencial en cualquier paquete de ROS. Contiene información sobre el paquete, como su nombre, versión, descripción y dependencias. También especifica la licencia bajo la cual se distribuye el paquete, entre otras cosas. Aquí es donde se enumeran las dependencias de otros paquetes de ROS 2 que este paquete necesita para funcionar correctamente.


2. `CMakeLists.txt`: Este archivo es parte de la configuración de CMake y se utiliza para especificar cómo se debe compilar el paquete. En este archivo se definen las dependencias, se configuran las opciones de compilación y se establecen los objetivos de construcción para el paquete. `ament_cmake` proporciona macros específicas de ROS 2 para facilitar este proceso.

Configurar la versión y el nombre del paquete.

```cmake
    cmake_minimum_required(VERSION 3.5)
    project(cpp_siro)
```

Especificar la versión de C++

```cmake
        # Default to C++14
        if(NOT CMAKE_CXX_STANDARD)
            set(CMAKE_CXX_STANDARD 14)
        endif()
```


Especificar dependencias del paquete `ament_cmake`, `rclcpp` y `std_msgs`

Cramos los nodos como ejecutables.

```cmake
        # Agrega el ejecutable del nodo.
        add_executable(siro_node_suscriptor src/siro_node_suscriptor.cpp)
        add_executable(siro_node_publicador src/siro_node_publicador.cpp)
```

Instalar las dependencias de los nodos.

```cmake
        # Especifica las dependencias para el ejecutable.
        ament_target_dependencies(siro_node_suscriptor rclcpp std_msgs)
        ament_target_dependencies(siro_node_publicador rclcpp std_msgs)
```

Instalar los nodos.

```cmake
        # Instala el ejecutable.
        install(TARGETS
            siro_node_suscriptor
            siro_node_publicador
            DESTINATION lib/${PROJECT_NAME}
        )
```


Creación de un directorio `/launch` para crear lanzaderas y compilacion.

```cmake
        # Instala los scripts y los recursos.
        install(DIRECTORY
            launch
            DESTINATION share/${PROJECT_NAME}
        )


        ament_package()
```


3. `src/`: Este directorio suele contener los archivos fuente (tanto de C++ como de Python) necesarios para el funcionamiento del paquete. Aquí es donde se escriben las implementaciones de los nodos, bibliotecas y otros componentes del paquete.


4. `include/`: A veces, este directorio se utiliza para almacenar archivos de encabezado (headers) de C++ que son necesarios para compilar el paquete. Esto es común cuando se están construyendo bibliotecas que serán utilizadas por otros paquetes.


5. `launch/`: Este directorio se utiliza para almacenar archivos de lanzamiento (`launch files`). Los archivos de lanzamiento son archivos XML que describen cómo se deben iniciar los nodos y configuraciones relacionadas cuando se lanza el paquete. Estos archivos son útiles para configurar y ejecutar nodos de manera conveniente, especialmente cuando se trabaja con múltiples nodos y parámetros.


6. `config/`: A veces, este directorio se utiliza para almacenar archivos de configuración, como archivos YAML, que contienen parámetros u otras configuraciones necesarias para el funcionamiento del paquete. Estos archivos pueden ser utilizados por nodos dentro del paquete para cargar configuraciones específicas durante la ejecución.


7. `test/`: Opcionalmente, este directorio se puede utilizar para almacenar archivos de prueba, como scripts de prueba o casos de prueba automatizados, que ayudan a garantizar el correcto funcionamiento del paquete.


Estos son los archivos y directorios comunes que se encuentran en un paquete creado con `ament_cmake` en ROS 2. Cada uno de ellos cumple un propósito específico en el proceso de desarrollo, compilación y ejecución del paquete dentro del entorno de ROS 2.



### [`atras`](./../)        [`siro_ws`](./../../)
