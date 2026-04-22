# ROS2 Remote Surveillance Robot Workspace

This repository contains a ROS 2 workspace for a surveillance robot simulation and a lightweight web dashboard package.

## Workspace Structure

- `src/robot_bringup`: Robot description, launch files, and Gazebo world.
- `src/web_dashboard`: Python package for the dashboard and related tests.

## Prerequisites

- Ubuntu with ROS 2 installed (recommended for Gazebo + ROS 2 workflows)
- `colcon`
- Gazebo (if not already included with your ROS 2 setup)

## Build

```bash
cd <workspace_root>
colcon build
```

## Source Environment

```bash
source install/setup.bash
```

## Run Gazebo Bringup

```bash
ros2 launch robot_bringup gazebo.launch.py
```

## Run Surveillance Launch

```bash
ros2 launch robot_bringup surveillance.launch.py
```

## Notes

- The robot model is defined in `src/robot_bringup/urdf/surveillance_robot.urdf.xacro`.
- The simulation world is in `src/robot_bringup/worlds/surveillance_world.world`.
