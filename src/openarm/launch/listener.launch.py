from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description():
    """docstring"""
    return LaunchDescription(
        [
            Node(
                package="demo_nodes_cpp",
                executable="listener",
            )
        ]
    )
