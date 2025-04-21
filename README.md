# 🤖 ROS2 Obstacle Avoidance Bot

A ROS2-based mobile robot simulation that performs basic obstacle avoidance using LIDAR data in a Gazebo world. This project demonstrates a foundational robotics behavior using real-time sensor feedback and autonomous motion planning.

---

## 🚀 Project Overview

This bot reads `LaserScan` data from a simulated LIDAR sensor and makes movement decisions based on nearby obstacles. If an object is detected within a threshold distance, the bot stops and rotates to avoid collision. Otherwise, it continues forward.

This is part of my learning journey in robotics and ROS2, and it showcases:
- Real-time data processing
- Sensor-based navigation
- Launch file setup and robot control using Python

---

## 🛠️ Tech Stack

- **ROS2 Humble** (rclpy)
- **Gazebo Classic**
- **Python 3**
- **URDF/Xacro** for robot description
- **RViz2** (optional) for visualization

---

## 📁 Project Structure

ros2-obstacle-avoidance-bot/
├── launch/
│   └── obstacle_avoidance.launch.py        # ✅ Launches everything
├── obstacle_avoidance/
│   ├── __init__.py
│   └── bot_controller.py                   # ✅ Main ROS2 Node
├── urdf/
│   └── bot.urdf.xacro                      # ✅ Basic robot model
├── worlds/
│   └── test_world.world                    # ✅ Basic Gazebo world
├── media/
│   └── demo.gif                            # (Add this later after sim)
├── README.md                               # ✅ You already have
├── package.xml                             # ✅ ROS2 metadata
├── setup.py                                # ✅ Python ROS2 setup
└── requirements.txt                        # Optional for non-ROS stuff


---

## 🎮 How to Run (Simulation)

1. **Build the workspace:**

```bash
colcon build --packages-select obstacle_avoidance
source install/setup.bash
