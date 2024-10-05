from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtle_pong'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf', 'meshes'), glob('urdf/meshes/*.stl')), 
        # Esta línea instala los archivos de la carpeta launch
        ('share/' + package_name + '/launch', glob('launch/*.py')),  
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='axioma',
    maintainer_email='davidalvarez33@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pong = turtle_pong.pong:main',
            'turtle_pong_ball = turtle_pong.turtle_pong_ball:main',
            'teleop_turtle = turtle_pong.teleop_turtle:main',
            'teleop_turtle_right = turtle_pong.teleop_turtle_right:main',
            'turtle_controller = turtle_pong.turtle_controller:main',
            'ball_controller = turtle_pong.ball_controller:main',
        ],
    },
)
