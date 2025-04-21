# launch/obstacle_avoidance.launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='obstacle_avoidance',
            executable='bot_controller',
            name='obstacle_avoider',
            output='screen'
        )
    ])

