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


En el directorio `incluede` se guardan archivos necesarios para la compilacion.


En el directorio `cpp_siro` se Gurdan los nodos.


El archivo `CMakeList.txt` guarda la configuración para la del paquete como dependencias, registro de nodos, directorios, versión de C++,...


El archivo `packeage.xml` contiene información del paquete como la descripción, el autor, el contacto, dependencias y herramientas.