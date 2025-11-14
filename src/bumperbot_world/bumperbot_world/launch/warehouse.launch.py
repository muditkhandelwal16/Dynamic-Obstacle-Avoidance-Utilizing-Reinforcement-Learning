from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    world_path = '/home/mudit/bumperbot_ws/src/bumperbot_world/worlds/warehouse_world.sdf'

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gzserver', '--verbose', world_path],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['gzclient'],
            output='screen'
        )
    ])
