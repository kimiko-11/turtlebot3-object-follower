A ROS 2-based object tracking project where a TurtleBot3 Waffle Pi detects and follows a red-colored object using its camera feed in the Gazebo simulation environment.

🚀 Features
Real-time color detection (red object)

Object centroid tracking on X-axis

Publishes velocity commands to follow the object

Works with TurtleBot3 Waffle Pi in Gazebo

🧰 Tech Stack
ROS 2 Humble

Gazebo Simulator

OpenCV (for image processing)

Python

📦 Usage

ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
ros2 run color_tracker color_tracker_node
Make sure to set your environment and install all dependencies.

🧠 Future Scope
Track multiple colors

Integrate depth estimation

Deploy on physical TurtleBot

