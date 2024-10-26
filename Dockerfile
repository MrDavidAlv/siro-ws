# Usar una imagen base de Ubuntu con ROS 2 Humble
FROM ros:humble

# Instalar dependencias del sistema y paquetes ROS primero
RUN apt-get update && apt-get install -y \
    ros-humble-desktop \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-rviz2 \
    ros-humble-joint-state-publisher \
    ros-humble-joint-state-publisher-gui \
    python3-pygame \
    git \
    libgl1-mesa-glx \
    libxkbcommon-x11-0 \
    && rm -rf /var/lib/apt/lists/*

# Configurar la variable de entorno ROS
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Crear un espacio de trabajo
WORKDIR /ros2_ws

# Copiar el código fuente al final, después de las instalaciones
COPY . /ros2_ws




# docker build -t ros2_siro_ws .
# docker run -it --rm   --name ros2_siro_ws_container   --net=host   --env="DISPLAY=:0"   --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"   ros2_siro_ws
