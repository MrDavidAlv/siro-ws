## PAQUETES EN ROS2

En ROS 2, los paquetes para C++ se pueden crear utilizando la herramienta `ament_cmake`, que es una extensión de CMake diseñada específicamente para el desarrollo de software en ROS 2. Por otro lado, los paquetes para Python se pueden crear utilizando `ament_python`, que es una extensión de setuptools diseñada para el mismo propósito. Ambas herramientas permiten a los desarrolladores gestionar las dependencias, compilar el código y generar los artefactos necesarios para la ejecución en entornos ROS 2.



### 📦 Paquetes en C++:
Para crear paquetes en C++ en ROS 2, se utiliza la herramienta ament_cmake. Esta herramienta proporciona una estructura de directorios estándar y un conjunto de macros de CMake que facilitan la compilación y la gestión de dependencias. Aquí hay un resumen de los pasos comunes para crear un paquete en C++ en ROS 2:


1. `Creación del paquete`: Puedes crear un nuevo paquete utilizando el comando `ros2 pkg create <package_name> --build-type ament_cmake`. Esto creará una estructura de directorios estándar para tu paquete, incluyendo archivos de compilación y configuración necesarios.

2. `Definición de dependencias`: En el archivo `package.xml`, puedes especificar las dependencias de tu paquete. Esto incluye las dependencias de otras bibliotecas de ROS 2 que tu paquete necesita para compilar y ejecutarse correctamente.

3. `Configuración de CMakeLists.txt`: En el archivo `CMakeLists.txt`, se configuran las opciones de compilación, se incluyen las dependencias y se definen los objetivos de construcción para tu paquete.

4. `Escritura de código`: A continuación, puedes escribir tu código en C++ en los archivos fuente y de encabezado dentro del directorio del paquete.

5. `Compilación del paquete`: Utilizando el comando `colcon build`, puedes compilar tu paquete junto con sus dependencias. Esto generará los ejecutables y bibliotecas necesarios para tu paquete.

6. `Ejecución y prueba` : Finalmente, puedes ejecutar y probar tu paquete utilizando las herramientas de ROS 2, como `ros2 run` o `ros2 launch`, según sea necesario.

### [`👉 Crea paquetes con C++`](./cpp_siro/)



### 📦 Paquetes en Python:
Para crear paquetes en Python en ROS 2, se utiliza la herramienta `ament_python`, que es una extensión de `setuptools` adaptada para el entorno de ROS 2. Aquí hay un resumen de los pasos comunes para crear un paquete en Python en ROS 2:

1. `Creación del paquete`: Al igual que con los paquetes en C++, puedes crear un nuevo paquete utilizando el comando `ros2 pkg create <package_name> --build-type ament_python`.

2. `Definición de dependencias`: Al igual que en los paquetes en C++, puedes especificar las dependencias de tu paquete en el archivo `package.xml`.

3. `Configuración de setup.py`: En el archivo `setup.py`, puedes definir la información del paquete, incluyendo su nombre, versión, autor, descripción, etc.

4. `Escritura de código`: A continuación, puedes escribir tu código en Python dentro del directorio del paquete.

5. `Compilación y distribución`: A diferencia de los paquetes en C++, los paquetes en Python no necesitan ser compilados. Sin embargo, puedes construir distribuciones de tu paquete utilizando `setuptools` para empaquetarlo y distribuirlo fácilmente.

6. `Ejecución y prueba`: Una vez que hayas construido tu paquete, puedes ejecutar y probarlo utilizando las herramientas de ROS 2, como ros2 run o ros2 launch.

En resumen, ROS 2 ofrece herramientas específicas tanto para el desarrollo en C++ como en Python, lo que permite a los desarrolladores crear paquetes de manera eficiente y gestionar sus dependencias de una manera sencilla.

### [`👉 Crea paquetes con Python`](./python_siro/)

--

### [`↩️ atras`](./../)        [`🔄 siro_ws`](./../)