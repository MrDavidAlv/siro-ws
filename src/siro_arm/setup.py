from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'siro_arm'

setup(
    name=package_name,
    version='0.0.1',  # Cambiado a 0.0.1 para representar la primera versión
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Incluir archivos URDF
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        # Incluir archivos STL (meshes) dentro de urdf/meshes
        (os.path.join('share', package_name, 'models', 'meshes', 'visual'), glob('models/meshes/visual/*.stl')),
        # Incluir archivos STL (meshes) dentro de urdf/meshes
        (os.path.join('share', package_name, 'models', 'meshes', 'v_bot'), glob('models/meshes/v_bot/*.stl')),
        # Incluir archivos DAE (meshes) dentro de urdf/meshes
        (os.path.join('share', package_name, 'models', 'meshes', 'c_bot'), glob('models/meshes/c_bot/*.dae')),
        # Incluir archivos de lanzamiento
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # Incluir la configuración de RViz
        (os.path.join('share', package_name, 'config'), glob('config/*.rviz')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='axioma',
    maintainer_email='davidalvarez33@hotmail.com',
    description='Paquete para controlar el brazo robótico siro_arm',
    license='Apache License 2.0',  # Asegúrate de declarar la licencia que estás utilizando
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Aquí puedes añadir scripts ejecutables si es necesario
        ],
    },
)
