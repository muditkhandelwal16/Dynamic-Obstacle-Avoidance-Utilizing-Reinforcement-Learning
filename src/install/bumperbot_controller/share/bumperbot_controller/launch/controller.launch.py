from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import UnlessCondition, IfCondition


def generate_launch_description():

    use_python_arg = DeclareLaunchArgument(
        "use_python",
        default_value = "True"
    )

    wheel_radius_arg = DeclareLaunchArgument(
        "wheel_radius",
        default_value="0.033"
    )

    wheel_separation_arg = DeclareLaunchArgument(
        "wheel_separation",
        default_value="0.17"
    )

    # use_sim_time = LaunchConfiguration("use_sim_time")
    # use_simple_controller = LaunchConfiguration("use_simple_controller")
    use_python = LaunchConfiguration("use_python")
    wheel_radius = LaunchConfiguration("wheel_radius")
    wheel_separation = LaunchConfiguration("wheel_separation")

    controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[{"controller_manager.ros__parameters": {"update_rate": 100, "use_sim_time": True}}],
        output="screen"
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
    )

    simple_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["simple_velocity_controller",
                "--controller-manager",
                "/controller_manager"
        ]
    )

    simple_controller_py = Node(
        package = "bumperbot_controller",
        executable = "simple_controller.py",
        parameters = [{"wheel_radius": wheel_radius,
                       "wheel_separation": wheel_separation}],
        condition = IfCondition(use_python)
    )


    return LaunchDescription(
        [
            use_python_arg,
            wheel_radius_arg,
            wheel_separation_arg,
            controller_manager,
            joint_state_broadcaster_spawner,
            simple_controller,
            simple_controller_py
        ]
    )