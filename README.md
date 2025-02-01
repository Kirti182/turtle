# UGV Simulation with ROS2 Humble Ubuntu (22.04) and TurtleBot3

The project demonstartes an UGV solution using ROS2 Humble,TurtleBot3,Gazebo,RViz,and SLAM Cartographer(TurtleBot3).The UGV performs sensor readings, Navigation in Simulated world of obstacles, SLAM for mapping, and visualization in RViz. 

**ROS 2 Nodes for Sensor Readings** –  Publisher generates random sensor data, and a subscriber evaluates it according to the computational task.<br/>

**TurtleBot3 Simulation in Gazebo** –  A world with obstacles/objects.<br/>

**SLAM (Cartographer)** –  Autonomous mapping of the environment using TurtleBot3.<br/>

**Visualization in RViz** –  Camera & LiDAR scans, and the 2D SLAM map are displayed in RViz.

## Installation & Dependencies

### Ensure ROS 2 Humble is installed
```bash
sudo apt install ros-humble-desktop
```

Please follow [the official ROS2 Documentation(Debian pkg)](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html) to install ROS2 Humble.

Setting up the ROS2 Workspace
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
ros2 pkg create ugv_package --build-type ament_python  
cd ugv_package  
mkdir ugv_package  
touch ugv_package/sensor_publisher.py scripts/sensor_subscriber.py 
chmod +x ugv_package/*.py
```
### For ROS Nodes Code Implementation

Build
```bash
cd ~/ros2_ws 
colcon build --packages-select ugv_package
source install/setup.bash
```

Run 
```bash
ros2 run ugv_package sensor_publisher  
ros2 run ugv_package sensor_subscriber
```
**Watch the demonstration here**
[subcriber_readings](https://drive.google.com/file/d/1t39hPlMtHfeuI-3iwAiVgLlqPh81NjTC/view?usp=sharing)
[publisher_readings](https://drive.google.com/file/d/1muEqbCgBzzJ3uWuDzKc_pDXxm7IlId50/view?usp=sharing)


1. Install Gazebo
    ```bash 
    sudo apt install ros-humble-gazebo-ros-pkgs
    ```
    Launch Gazebo<br/>
   ```bash
   gazebo --verbose ugv_world.world
   ``` 

3. Install Cartographer<br/>
```bash   
sudo apt install ros-humble-cartographer  
 sudo apt install ros-humble-cartographer-ros
 ```

3. Install TurtleBot3 Simulation Package<br/>
```bash   
cd ~/turtlebot3_ws/src/  
git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git  
cd ~/turtlebot3_ws && colcon build --symlink-install
```

### Running the Simulation

Launch Gazebo with TurtleBot3<br/> 
```bash
export TURTLEBOT3_MODEL=waffle  
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Verify Camera and Lidar Topics<br/> 
```bash
ros2 topic list` (/camera/color/image_raw, /camera/depth/image_raw, /scan)<br/> 
ros2 topic echo /camera/color/image_raw
```
Launch RViz<br/>
```bash
ros2 launch turtlebot3_gazebo turtlebto3_gazebo_rviz.launch
```

RViz for Camera (Launch in a new terminal)<br/>
```bash
ros2 run rviz2 rviz2
```
Operate TurtleBot3 Teleop (in a new terminal)<br/> 
```bash
ros2 launch turtlebot3_teleop turtlebot3_teleop_key.launch
```

### For SLAM Simulation(each in new terminal)<br/> 

Launch Simulation World<br/> 
```bash
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Run SLAM Node<br/> 
```bash
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```

Run Teleop Node<br/> 
```bash
export TURTLEBOT3_MODEL=waffle
ros2 run turtlebot3_teleop teleop_keyboard 
```

Save map<br/> 
```bash
ros2 run nav2_map_server map_saver_cli -f ~/map
```

### Resources<br/> 

[Refer for TurtleBot3 Simulation](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)


 


   

