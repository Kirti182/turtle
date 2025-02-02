cmake_minimum_required(VERSION 3.5)
project(ugv_package)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)

# Install Python modules
install(PROGRAMS
  # Add any Python scripts you want to install here
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/
)

# Install world files
install(DIRECTORY worlds/
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
