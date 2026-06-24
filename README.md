# Obsidian Eye

## Overview

Obsidian Eye is an autonomous drone-based monitoring and verification system designed to enhance the protection of critical infrastructure, particularly oil pipelines and remote facilities.

The system combines multiple sensing technologies to detect, verify, and classify potential aerial threats while reducing false alarms and improving situational awareness for operators.

---

## Problem Statement

Monitoring long oil pipelines and remote facilities presents several operational challenges.

Natural terrain such as hills, valleys, and uneven landscapes can create blind spots that reduce the effectiveness of ground-based surveillance systems. Additionally, small low-altitude drones are becoming increasingly difficult to detect and classify accurately, which may lead to false alarms or delayed responses.

In some scenarios, communication coverage may also become weak or unreliable, reducing situational awareness for ground operators.

---

## Proposed Solution

Obsidian Eye acts as an intelligent aerial support platform that can be deployed when suspicious activity is detected or when additional verification is required.

The system autonomously navigates to the target area and performs multi-sensor threat assessment using:

- RF Signal Detection
- Acoustic Analysis
- YOLO-Based Visual Verification
- Autonomous Decision Engine

By combining data from multiple sensors, the system reduces false alarms and improves confidence in threat identification.

---

## System Workflow

1. Ground monitoring systems detect suspicious activity.
2. Obsidian Eye is deployed to the target location.
3. RF signals are analyzed for drone-related transmissions.
4. Acoustic sensors verify the presence of drone propeller signatures.
5. The onboard camera performs visual verification using YOLO.
6. A weighted decision engine evaluates all sensor inputs.
7. The system classifies the situation as:
   - Confirmed Threat
   - Suspicious Activity
   - No Threat

---

## Operational Scenario

A ground surveillance system detects unusual activity near an oil pipeline section located in a terrain-obstructed area.

Obsidian Eye is launched to investigate the location and provide real-time verification. The drone analyzes the environment using multiple sensors and delivers an accurate threat assessment to support rapid and informed decision-making.

---

## Project Evolution

Obsidian Eye started as a multi-sensor drone detection and verification system that combines RF analysis, acoustic sensing, and YOLO-based visual confirmation to reduce false alarms.

The project is currently being expanded with PX4 and Gazebo simulation to evaluate autonomous mission execution, target verification, and critical infrastructure monitoring in realistic environments.

Future development includes advanced sensor integration, improved autonomous tracking, and simulation-based testing in complex operational scenarios.

---

## Technologies Used

- Python
- PX4 Autopilot
- Gazebo Sim
- QGroundControl
- MAVSDK
- OpenCV
- YOLOv8
- Multi-Sensor Fusion
---

## Development Environment

- Ubuntu 22.04
- Visual Studio Code
- GitHub
- PX4 SITL Simulation
- Gazebo Simulation Environment

---

## Future Development

- Advanced Autonomous Tracking
- Airborne Radar Integration
- Thermal Imaging Support
- Enhanced Mission Planning
- Multi-Drone Coordination
- Real-Time Threat Assessment Improvements



Unmanned Systems Trainee
ابي نفس هذي بس اختصرهااا بسس
