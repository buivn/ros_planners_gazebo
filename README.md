# ROS Planning Interfaces
This repo is to provide planning interface connecting from planners to robot's models or physical robots.

The initial applications aim to:
1. Manipulator - fetch manipulator.
The input is a pose/joint target, then the planner gets the pose and the robot models to generate trajectories.
The trajectories are then transferred to the physical robots or sim-robots.
- Installation: ROS Noetic - Ubuntu 20.06
- Several ROS packages: moveit_python, moveit/planning_scene_interface, moveit/move_group_interface

Procedures:
Run two launch files and a planning script:
- roslaunch fetch_gazebo planning.launch
- roslaunch fetch_moveit_config move_group.launch

The first launch file loads an Gazebo environment and a robot robot model. The second launch file loads a planner for planning.

- rosrun fetch_gazebo_moveit planning_pose.py 
This script provide some target pose for the manipulator to move.


<!-- 2. Mobile robots -->

