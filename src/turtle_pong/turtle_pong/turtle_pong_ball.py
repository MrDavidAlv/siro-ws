import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute, SetPen, Spawn
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import random

class cBall(Node):

    def __init__(self):
        super().__init__('turtle_pong_ball')

        self.get_logger().info('Initialize Turtle Ball')

        # Initialize variables
        self.pose_ = None
        self.pose_left_ = None
        self.pose_right_ = None
        self.direction_ = 'STOP'

        # Subscribers
        self.create_subscription(Pose, '/ball/pose', self.pose_callback, 10)
        self.create_subscription(Pose, '/turtle_left/pose', self.pose_left_callback, 10)
        self.create_subscription(Pose, '/turtle_right/pose', self.pose_right_callback, 10)

        # Publisher
        self.cmd_vel_pub_ = self.create_publisher(Twist, '/ball/cmd_vel', 10)

        # Service clients
        self.teleport_abs_client_ = self.create_client(TeleportAbsolute, '/ball/teleport_absolute')
        while not self.teleport_abs_client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service /ball/teleport_absolute...')
        
        # Initial setup
        self.reset()

    def reset(self):
        self.set_pose_abs(3.0, 3.0, 0.0)
        self.pen_off(True)

    def pen_off(self, off):
        set_pen_client = self.create_client(SetPen, '/ball/set_pen')
        while not set_pen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service /ball/set_pen...')
        
        request = SetPen.Request()
        request.off = off
        set_pen_client.call_async(request)

    def set_pose_abs(self, x, y, theta):
        request = TeleportAbsolute.Request()
        request.x = x
        request.y = y
        request.theta = theta
        self.get_logger().info(f'Setting Pose Abs (x, y, theta) = ({x}, {y}, {theta})')
        self.teleport_abs_client_.call_async(request)

    def set_vel(self, linear_x, angular_z):
        twist = Twist()
        twist.linear.x = linear_x
        twist.angular.z = angular_z
        self.cmd_vel_pub_.publish(twist)

    def move(self):
        if not self.pose_ or not self.pose_left_ or not self.pose_right_:
            self.get_logger().info('Pose not yet received')
            self.set_pose_abs(3.0, 3.0, -0.5)
            return

        self.set_vel(2.0, 0.0)

        x, y, theta = self.pose_.x, self.pose_.y, self.pose_.theta
        self.check_player_collision()
        self.update_direction()

        if y > 11.0:
            if self.direction_ in ['UP_LEFT', 'UP_RIGHT']:
                new_theta = 2.0 * math.pi - theta
                self.set_pose_abs(x, y, new_theta)
        if y < 0.001:
            if self.direction_ in ['DOWN_LEFT', 'DOWN_RIGHT']:
                new_theta = -theta
                self.set_pose_abs(x, y, new_theta)
        if x > 11.0:
            if self.direction_ in ['UP_RIGHT', 'DOWN_RIGHT']:
                new_theta = math.pi - theta
                self.set_pose_abs(x, y, new_theta)
        if x < 0.001:
            if self.direction_ in ['UP_LEFT', 'DOWN_LEFT']:
                new_theta = -(math.pi + theta)
                self.set_pose_abs(x, y, new_theta)

    def check_player_collision(self):
        delta_x = 0.2
        delta_y = 0.5
        paddle_size = 2.0 * delta_y
        max_bounce_angle = 5 * math.pi / 12

        if self.pose_left_ and abs(self.pose_left_.x - self.pose_.x) < delta_x:
            if abs(self.pose_left_.y - self.pose_.y) < delta_y:
                rel_intersect_y = (self.pose_left_.y + delta_y) - self.pose_.y
                norm_rel_intersect_y = rel_intersect_y / paddle_size
                bounce_angle = norm_rel_intersect_y * max_bounce_angle
                self.get_logger().info(f'Bounce angle: {bounce_angle}')
                self.set_pose_abs(self.pose_.x, self.pose_.y, bounce_angle)

        if self.pose_right_ and abs(self.pose_right_.x - self.pose_.x) < delta_x:
            if abs(self.pose_right_.y - self.pose_.y) < delta_y:
                rel_intersect_y = (self.pose_right_.y + delta_y) - self.pose_.y
                norm_rel_intersect_y = rel_intersect_y / paddle_size
                bounce_angle = norm_rel_intersect_y * max_bounce_angle
                bounce_angle += math.pi / 2 if bounce_angle > 0 else -math.pi / 2
                self.get_logger().info(f'Bounce angle: {bounce_angle}')
                self.set_pose_abs(self.pose_.x, self.pose_.y, bounce_angle)

    def update_direction(self):
        theta = self.pose_.theta
        if theta == 0.0:
            self.direction_ = 'RIGHT'
        elif 0.0 < theta < math.pi / 2:
            self.direction_ = 'UP_RIGHT'
        elif math.pi / 2 < theta < math.pi:
            self.direction_ = 'UP_LEFT'
        elif theta == math.pi:
            self.direction_ = 'LEFT'
        elif -math.pi < theta < -math.pi / 2:
            self.direction_ = 'DOWN_LEFT'
        elif -math.pi / 2 < theta < 0.0:
            self.direction_ = 'DOWN_RIGHT'

    def pose_callback(self, pose):
        self.pose_ = pose
        self.get_logger().info(f'x: {pose.x}, y: {pose.y}, theta: {pose.theta}, dir: {self.direction_}')

    def pose_left_callback(self, pose):
        self.pose_left_ = pose
        self.get_logger().debug(f'Left paddle x: {pose.x}, y: {pose.y}')

    def pose_right_callback(self, pose):
        self.pose_right_ = pose
        self.get_logger().debug(f'Right paddle x: {pose.x}, y: {pose.y}')


def main(args=None):
    rclpy.init(args=args)
    ball_node = cBall()

    spawn_client = ball_node.create_client(Spawn, '/spawn')
    while not spawn_client.wait_for_service(timeout_sec=1.0):
        ball_node.get_logger().info('Waiting for service /spawn...')
    
    spawn_request = Spawn.Request()
    spawn_request.name = 'ball'
    spawn_request.x = 2.0
    spawn_request.y = 2.0
    spawn_request.theta = 0.0
    ball_node.get_logger().info('Spawning ball turtle')
    spawn_client.call_async(spawn_request)

    try:
        rate = ball_node.create_rate(100)
        while rclpy.ok():
            ball_node.move()
            rclpy.spin_once(ball_node)
            rate.sleep()
    except KeyboardInterrupt:
        ball_node.get_logger().info('Shutting down...')
    finally:
        ball_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
