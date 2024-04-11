# Instalación 🛠️
Para instalar ROS 2 en tu sistema utilizando paquetes Debian o binarios, sigue las instrucciones que se describen a continuación. Estas instrucciones asumen que estás utilizando una distribución de Linux compatible (como Ubuntu) y que tienes privilegios de superusuario para instalar paquetes.

- **Paquetes Debian**: Son paquetes preconstruidos específicos para Debian y sus derivados (como Ubuntu), se instalan usando el gestor de paquetes apt.

- **Binarios**: Son archivos ejecutables preconstruidos, se instalan directamente sin usar un gestor de paquetes.

## Instalación para paquetes Debian

> **Advertencia**: Instalar en Ubuntu 22.04 LST.

#### Configuración de fuentes

1. Configuración regional compatible con UTF-8
```
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```
 
 2. Configurar el repositorio de Ubuntu Universe esté habilitado.
```
sudo apt install software-properties-common
sudo add-apt-repository universe
```

 3. Agregue la clave GPG ROS2.
```
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

 4. Agregar el repositorio a la lista de fuentes.
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

#### Instalar paquetes de ROS2
5. Actualizar cache.
```
sudo apt update
```

6. Actualizar el sistema.
```
sudo apt upgrade
```

7. Intalación de ROS2.

> **Version Desktop**: Instalara todos los paquetes de ROS2, RVIZ2, ejemplos y tutoriales.
```
sudo apt install ros-humble-desktop
```
> **Version base**: Bibliotecas de comunicación, paquetes de mensajes, herramientas de línea de comandos.
```
sudo apt install ros-humble-ros-base
```

8. Herramientas de desarrollo.
```
sudo apt install ros-dev-tools
```

---

### Probar instalación 
1. Actualizamos cache.
```
sudo apt update
```

2. Actualizamos el sistema operativo.
```
sudo apt upgrade
```

3. Ahora en una terminal ejecute el nodo publicador de prueba. 

```
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```

4. Ahora en una terminal ejecute el nodo suscriptor de prueba. 

```
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp listener
```
<br>

### [`↩️ atras`](./README.md) 