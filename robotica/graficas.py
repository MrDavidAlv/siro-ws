import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Definir una clase para un vector 3D (Vector3)
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Definir una clase para un cuaternio (Quaternion)
class Quaternion:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

# Definir una clase para representar una pose (Pose) con posición y orientación
class Pose:
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation

# Definir una clase para un Twist (movimiento lineal y angular)
class Twist:
    def __init__(self, linear, angular):
        self.linear = linear
        self.angular = angular

# Definir una clase para una PoseStamped
class PoseStamped:
    def __init__(self, pose, timestamp, frame_id):
        self.pose = pose
        self.timestamp = timestamp
        self.frame_id = frame_id

# Definir una clase para una Transform
class Transform:
    def __init__(self, translation, rotation):
        self.translation = translation
        self.rotation = rotation

# Definir una clase para un Wrench (fuerza y torque)
class Wrench:
    def __init__(self, force, torque):
        self.force = force
        self.torque = torque

# Función para convertir un cuaternio a ángulos de Euler (roll, pitch, yaw)
def quaternion_to_euler(quaternion):
    qx, qy, qz, qw = quaternion.x, quaternion.y, quaternion.z, quaternion.w
    roll = np.arctan2(2 * (qw * qx + qy * qz), 1 - 2 * (qx * qx + qy * qy))
    pitch = np.arcsin(2 * (qw * qy - qz * qx))
    yaw = np.arctan2(2 * (qw * qz + qx * qy), 1 - 2 * (qy * qy + qz * qz))
    return roll, pitch, yaw

# Crear una figura y un conjunto de ejes 3D para graficar
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

# Gráfico para `geometry_msgs/Point`
point = Vector3(3, 2, 4)
ax.scatter(point.x, point.y, point.z, c='r', marker='o', label=f'Point ({point.x}, {point.y}, {point.z})')

# Gráfico para `geometry_msgs/Quaternion`
quaternion = Quaternion(0, 0.707, 0, 0.707)
roll, pitch, yaw = quaternion_to_euler(quaternion)
ax.quiver(0, 0, 0, np.cos(yaw), np.sin(pitch), np.cos(roll), length=1, color='k', label=f'Quaternion\n(roll: {roll:.2f}, pitch: {pitch:.2f}, yaw: {yaw:.2f})')

# Gráfico para `geometry_msgs/Pose`
pose = Pose(point, quaternion)
ax.scatter(pose.position.x, pose.position.y, pose.position.z, c='b', marker='o', label='Pose (Point)')
ax.quiver(pose.position.x, pose.position.y, pose.position.z, np.cos(yaw), np.sin(pitch), np.cos(roll), length=1, color='b', label='Pose (Quaternion)')

# Gráfico para `geometry_msgs/Twist`
twist_linear = Vector3(1, 0.5, 0)
twist_angular = Vector3(0.5, 0.2, 0.1)
twist = Twist(twist_linear, twist_angular)
ax.quiver(0, 0, 0, twist.linear.x, twist.linear.y, twist.linear.z, color='g', label=f'Twist Linear ({twist.linear.x}, {twist.linear.y}, {twist.linear.z})')
ax.quiver(0, 0, 0, twist.angular.x, twist.angular.y, twist.angular.z, color='y', label=f'Twist Angular ({twist.angular.x}, {twist.angular.y}, {twist.angular.z})')

# Gráfico para `geometry_msgs/PoseStamped`
pose_stamped = PoseStamped(pose, timestamp='123456789', frame_id='base_link')
# Pose ya está graficada, así que no es necesario graficarla nuevamente.

# Gráfico para `geometry_msgs/Transform`
translation = Vector3(3, 2, 4)
rotation = quaternion
transform = Transform(translation, rotation)
ax.quiver(transform.translation.x, transform.translation.y, transform.translation.z, np.cos(yaw), np.sin(pitch), np.cos(roll), length=1, color='m', label='Transform\n(rotation)')

# Gráfico para `geometry_msgs/Wrench`
force = Vector3(1, -0.5, 0.5)
torque = Vector3(0.3, 0.1, -0.2)
wrench = Wrench(force, torque)
ax.quiver(0, 0, 0, wrench.force.x, wrench.force.y, wrench.force.z, color='orange', label=f'Wrench Force ({wrench.force.x}, {wrench.force.y}, {wrench.force.z})')
ax.quiver(0, 0, 0, wrench.torque.x, wrench.torque.y, wrench.torque.z, color='cyan', label=f'Wrench Torque ({wrench.torque.x}, {wrench.torque.y}, {wrench.torque.z})')

# Configurar los límites de los ejes
ax.set_xlim([-2, 6])
ax.set_ylim([-2, 6])
ax.set_zlim([-2, 6])

# Configurar etiquetas de los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Añadir una leyenda
ax.legend()

# Ocultar las cuadrículas
ax.grid(False)

# Mostrar el gráfico
plt.show()
