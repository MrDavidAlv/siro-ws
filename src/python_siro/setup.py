from setuptools import find_packages, setup

package_name = 'python_siro'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'geometry_msgs'],
    zip_safe=True,
    maintainer='axioma',
    maintainer_email='davidalvarez33@hotmail.com',
    description='TODO: Package description',
    license='Licencia Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'siro_node_suscriptor = python_siro.siro_node_suscriptor:main',
            'siro_node_publicador = python_siro.siro_node_publicador:main',
            'star_turtle_controller = python_siro.star_turtle_controller:main',
            'turtle_follower = python_siro.turtle_follower:main',
            'rendimientoPython = python_siro.rendimientoPython:main',
        ],
    },
)
