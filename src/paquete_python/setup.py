from setuptools import find_packages, setup

package_name = 'paquete_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'primer_nodo = paquete_python.primer_nodo:main',
            'talker      = paquete_python.publicador:main',
            'listener      = paquete_python.suscriptor:main',
        ],
    },
)
