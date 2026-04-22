import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg = get_package_share_directory('robot_bringup')
    xacro_file = os.path.join(pkg, 'urdf', 'surveillance_robot.urdf.xacro')
    robot_desc = xacro.process_file(xacro_file).toxml()
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': os.path.join(pkg, 'worlds', 'surveillance_world.world')}.items()
    )
    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}],
        output='screen'
    )
    spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'surveillance_robot',
                   '-x', '0.0', '-y', '0.0', '-z', '0.13', '-Y', '0.0'],
        output='screen'
    )
    return LaunchDescription([gazebo, robot_state_pub, spawn])
