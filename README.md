🧠 ROS 2 Object Detection with TurtleBot3 (Waffle Pi)
This project showcases real-time color-based object detection in a Gazebo simulation using the TurtleBot3 Waffle Pi model equipped with a simulated RGB camera. Built using ROS 2 Humble, it detects colored objects in the environment (like red or green) and processes camera input using OpenCV.

🚀 Features
🐢 Simulated TurtleBot3 Waffle Pi in a house environment (Gazebo)

🎥 RGB camera simulation with live feed via rqt_image_view

🟥🔲 Real-time color detection (Red/Green/Customizable via HSV)

📡 Publishes detection output and camera topics

🔄 Visualizes the entire node graph using rqt_graph

🧩 Modular ROS 2 package (object_detector) to easily extend detection logic

📦 Package Structure

ros2_ws/
└── src/
    └── object_detector/
        ├── detect_color.py
        ├── setup.py
        ├── package.xml
        └── ...
🎮 How to Use
Launch Gazebo Simulation


export TURTLEBOT3_MODEL=waffle_pi
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
Run Object Detector Node

ros2 run object_detector detect_color
Visualize Camera Feed

ros2 run rqt_image_view rqt_image_view
(Optional) Move the robot manually or via keyboard/teleop.

🔧 Requirements
ROS 2 Humble

Gazebo

turtlebot3_gazebo and turtlebot3_msgs packages

Python 3, OpenCV

rqt, rqt_graph, rqt_image_view

