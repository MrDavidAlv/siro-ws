import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Definir una clase para un cuaternio (Quaternion)
class Quaternion:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

# Función para convertir un cuaternio a ángulos de Euler (roll, pitch, yaw)
def quaternion_to_euler(quaternion):
    qx, qy, qz, qw = quaternion.x, quaternion.y, quaternion.z, quaternion.w
    roll = np.arctan2(2 * (qw * qx + qy * qz), 1 - 2 * (qx * qx + qy * qy))
    pitch = np.arcsin(2 * (qw * qy - qz * qx))
    yaw = np.arctan2(2 * (qw * qz + qx * qy), 1 - 2 * (qy * qy + qz * qz))
    return roll, pitch, yaw

# Crear gráfica para `geometry_msgs/Quaternion`
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definir el cuaternio con valores que representen rotaciones más notables
# Utilizaremos un cuaternio que representa rotaciones alrededor de los tres ejes
# Vamos a elegir una combinación de rotaciones significativas alrededor de roll, pitch y yaw
quaternion = Quaternion(0.707, 0, 0, 0.707)  # Rotación de 90 grados alrededor de X

# Convertir el cuaternio a ángulos de Euler (roll, pitch, yaw)
roll, pitch, yaw = quaternion_to_euler(quaternion)

# Graficar los ejes de rotación: roll, pitch, yaw
# Para hacer más visibles las rotaciones, aumentaremos la longitud de los vectores
length = 2  # Longitud de los vectores para hacerlos más visibles
ax.quiver(0, 0, 0, length * np.cos(yaw), length * np.sin(yaw), 0, length=1, color='k', label='Yaw')
ax.quiver(0, 0, 0, 0, length * np.sin(pitch), length * np.cos(pitch), length=1, color='r', label='Pitch')
ax.quiver(0, 0, 0, length * np.cos(roll), 0, length * np.sin(roll), length=1, color='b', label='Roll')

# Configurar los límites de los ejes
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

# Configurar nombres de los ejes
ax.set_xlabel('Yaw')
ax.set_ylabel('Pitch')
ax.set_zlabel('Roll')

# Configurar el fondo transparente y eliminar cuadrículas
ax.set_facecolor((1, 1, 1, 0))  # RGBA (transparencia)
ax.grid(False)

# Añadir la leyenda
ax.legend()

# Configurar título
ax.set_title('geometry_msgs/Quaternion')

# Mostrar la gráfica
plt.show()
