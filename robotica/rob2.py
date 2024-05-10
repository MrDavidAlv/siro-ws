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

# Definir una clase para una Transform (transformación con traslación y rotación)
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

# Configurar los límites de los ejes para todas las gráficas
limites = [-2, 5]

# Crear una sola figura con múltiples subplots (2 filas, 3 columnas)
fig, axs = plt.subplots(2, 3, subplot_kw={'projection': '3d'}, figsize=(18, 12))
fig.suptitle('Comparación de conceptos de ROS')

# 1. Gráfico para `geometry_msgs/Point`
ax1 = axs[0, 0]
point = Vector3(3, 2, 4)
ax1.scatter(point.x, point.y, point.z, c='r', marker='o', label=f'Point ({point.x}, {point.y}, {point.z})')
ax1.set_xlim(limites)
ax1.set_ylim(limites)
ax1.set_zlim(limites)
ax1.set_xlabel('Eje X')
ax1.set_ylabel('Eje Y')
ax1.set_zlabel('Eje Z')
ax1.legend()
ax1.set_title('geometry_msgs/Point')

# 2. Gráfico para `geometry_msgs/Quaternion`
ax2 = axs[0, 1]
quaternion = Quaternion(0, 0.707, 0, 0.707)
roll, pitch, yaw = quaternion_to_euler(quaternion)
ax2.quiver(0, 0, 0, np.cos(yaw), np.sin(pitch), np.cos(roll), length=1, color='k', label=f'Quaternion\n(roll: {roll:.2f}, pitch: {pitch:.2f}, yaw: {yaw:.2f})')
ax2.set_xlim(limites)
ax2.set_ylim(limites)
ax2.set_zlim(limites)
ax2.set_xlabel('Eje X')
ax2.set_ylabel('Eje Y')
ax2.set_zlabel('Eje Z')
ax2.legend()
ax2.set_title('geometry_msgs/Quaternion')

# 3. Gráfico para `geometry_msgs/Pose`
ax3 = axs[0, 2]
pose = Pose(point, quaternion)
ax3.scatter(pose.position.x, pose.position.y, pose.position.z, c='b', marker='o', label=f'Pose Position ({pose.position.x}, {pose.position.y}, {pose.position.z})')
ax3.quiver(pose.position.x, pose.position.y, pose.position.z, np.cos(yaw), np.sin(pitch), np.cos(roll), length=1, color='b', label='Pose Orientation (Quaternion)')
ax3.set_xlim(limites)
ax3.set_ylim(limites)
ax3.set_zlim(limites)
ax3.set_xlabel('Eje X')
ax3.set_ylabel('Eje Y')
ax3.set_zlabel('Eje Z')
ax3.legend()
ax3.set_title('geometry_msgs/Pose')

# 4. Gráfico para `geometry_msgs/Twist`
ax4 = axs[1, 0]
twist_linear = Vector3(1, 0.5, 0)
twist_angular = Vector3(0.5, 0.2, 0.1)
twist = Twist(twist_linear, twist_angular)
ax4.quiver(0, 0, 0, twist.linear.x, twist.linear.y, twist.linear.z, color='g', label=f'Twist Linear ({twist.linear.x}, {twist.linear.y}, {twist.linear.z})')
ax4.quiver(0, 0, 0, twist.angular.x, twist.angular.y, twist.angular.z, color='y', label=f'Twist Angular ({twist.angular.x}, {twist.angular.y}, {twist.angular.z})')
ax4.set_xlim(limites)
ax4.set_ylim(limites)
ax4.set_zlim(limites)
ax4.set_xlabel('Eje X')
ax4.set_ylabel('Eje Y')
ax4.set_zlabel('Eje Z')
ax4.legend()
ax4.set_title('geometry_msgs/Twist')

# 5. Gráfico para `geometry_msgs/Transform`
ax5 = axs[1, 1]
transform_translation = Vector3(3, 2, 4)
transform_rotation = quaternion
transform = Transform(transform_translation, transform_rotation)
ax5.quiver(transform.translation.x, transform.translation.y, transform.translation.z, np.cos(yaw), np.sin(pitch), np.cos(roll), length=1, color='m', label='Transform Rotation')
ax5.quiver(0, 0, 0, transform.translation.x, transform.translation.y, transform.translation.z, color='m', label='Transform Translation')
ax5.set_xlim(limites)
ax5.set_ylim(limites)
ax5.set_zlim(limites)
ax5.set_xlabel('Eje X')
ax5.set_ylabel('Eje Y')
ax5.set_zlabel('Eje Z')
ax5.legend()
ax5.set_title('geometry_msgs/Transform')

# 6. Gráfico para `geometry_msgs/Wrench`
ax6 = axs[1, 2]
force = Vector3(1, -0.5, 0.5)
torque = Vector3(0.3, 0.1, -0.2)
wrench = Wrench(force, torque)
ax6.quiver(0, 0, 0, wrench.force.x, wrench.force.y, wrench.force.z, color='orange', label=f'Wrench Force ({wrench.force.x}, {wrench.force.y}, {wrench.force.z})')
ax6.quiver(0, 0, 0, wrench.torque.x, wrench.torque.y, wrench.torque.z, color='cyan', label=f'Wrench Torque ({wrench.torque.x}, {wrench.torque.y}, {wrench.torque.z})')
ax6.set_xlim(limites)
ax6.set_ylim(limites)
ax6.set_zlim(limites)
ax6.set_xlabel('Eje X')
ax6.set_ylabel('Eje Y')
ax6.set_zlabel('Eje Z')
ax6.legend()
ax6.set_title('geometry_msgs/Wrench')

# Mostrar todas las gráficas en una sola ventana
plt.show()
