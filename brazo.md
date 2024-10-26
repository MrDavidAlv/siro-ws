# SIRO ARM

##   Launch

```python
def generate_launch_description():
    urdf_file = os.path.join(get_package_share_directory('siro_arm'), 'urdf', 'arm1.urdf')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory('siro_arm'), 'config', 'siro_arm.rviz')],
        ),
        Node(
            package='siro_arm',
            executable='tu_nodo_serial_publisher',  # Cambia esto al nombre de tu archivo
            name='serial_publisher',
            output='screen',
        )
    ])

```

## NODE

```python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial

class SerialPublisher(Node):
    def __init__(self):
        super().__init__('serial_publisher')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_states_callback,
            10
        )
        self.serial_connection = serial.Serial('/dev/ttyUSB0', 9600)  # Ajusta el puerto y la velocidad según sea necesario

    def joint_states_callback(self, msg):
        # Extraer la información de los deslizadores
        positions = msg.position
        command = ','.join(map(str, positions)) + '\n'  # Convierte a string y añade un salto de línea
        self.serial_connection.write(command.encode())  # Envía los datos al Arduino

def main(args=None):
    rclpy.init(args=args)
    serial_publisher = SerialPublisher()
    rclpy.spin(serial_publisher)
    serial_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

```




## ARDUINO

```C
#include <Servo.h>

// Define los servos
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

// Variables para almacenar las posiciones de los servos
int pos1, pos2, pos3, pos4, pos5;

void setup() {
    // Inicia la comunicación serial
    Serial.begin(9600);

    // Adjunta los servos a los pines correspondientes
    servo1.attach(9);  // Ajusta según tu conexión
    servo2.attach(10);
    servo3.attach(11);
    servo4.attach(12);
    servo5.attach(13);
}

void loop() {
    // Verifica si hay datos disponibles en el puerto serial
    if (Serial.available() > 0) {
        // Lee los datos de la línea serial
        String data = Serial.readStringUntil('\n');
        
        // Divide los datos en partes
        int commaIndex1 = data.indexOf(',');
        int commaIndex2 = data.indexOf(',', commaIndex1 + 1);
        int commaIndex3 = data.indexOf(',', commaIndex2 + 1);
        int commaIndex4 = data.indexOf(',', commaIndex3 + 1);

        // Extrae las posiciones y convierte a enteros
        pos1 = data.substring(0, commaIndex1).toInt();
        pos2 = data.substring(commaIndex1 + 1, commaIndex2).toInt();
        pos3 = data.substring(commaIndex2 + 1, commaIndex3).toInt();
        pos4 = data.substring(commaIndex3 + 1, commaIndex4).toInt();
        pos5 = data.substring(commaIndex4 + 1).toInt();

        // Mueve los servos a la nueva posición
        servo1.write(pos1);
        servo2.write(pos2);
        servo3.write(pos3);
        servo4.write(pos4);
        servo5.write(pos5);
    }
}
```