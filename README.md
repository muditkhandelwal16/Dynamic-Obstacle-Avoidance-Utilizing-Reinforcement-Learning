# Dynamic-Obstacle-Avoidance-Utilizing-Reinforcement-Learning
## Requirements-
  ROS2 distro: Humble  
  Gazebo classic: Gazebo multi-robot simulator, version 11.10.2  
  Turtlebot3  
## Clone the repo using this command exactly
```
	git clone https://github.com/muditkhandelwal16/Dynamic-Obstacle-Avoidance-Utilizing-Reinforcement-Learning.git bumperbot_ws
```
## Build and run
```
	colcon build --symlink-install
	. install/setup.bash
```
## Run 
```
	ros2 launch bumperbot_bringup simulated_robot.launch.py world_name:=small_house

```
and see if it works
