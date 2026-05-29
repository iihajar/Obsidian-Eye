# Obsidian-Eye

## Autonomous Multi-Sensor Drone Monitoring and Detection System

Obsidian-Eye is an intelligent drone monitoring system that combines multiple detection methods to improve drone identification accuracy and reduce false alarms.

## Features

- RF Detection
- Acoustic Detection
- YOLO Visual Verification
- Decision Making Module
- Autonomous Tracking
- Battery Monitoring
- Altitude Monitoring
- Connection and Arming Checks

## Project Structure

```text
main.py
check_module.py
monitor_module.py
rf_module.py
acoustic_module.py
yolo_module.py
decision_module.py
mission_items.py
```

## Workflow

## Workflow

Start Monitoring
       ↓
RF Scan
       ↓
Acoustic Analysis
       ↓
Suspicious Target?
       ↓
      Yes
       ↓
YOLO Verification
       ↓
Decision Module
       ↓
 ┌───────────────────┬─────────────────────┐
 │                   │
 ▼                   ▼
Continue        Confirmed Drone
Monitoring             ↓
                        ▼
              Autonomous Tracking

## Safety Checks

- Connection Check
- Arming Check
- Battery Monitoring
- Altitude Monitoring

## Author

Hajer Alajhar
