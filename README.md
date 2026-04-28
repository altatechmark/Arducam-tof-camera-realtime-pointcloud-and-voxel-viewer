# Arducam TOF Camera Real-time Point Cloud and Voxel Viewer

## Overview

This project provides a real-time visualization system for Arducam Time-of-Flight (TOF) depth cameras. It captures depth data from the camera, processes it into 3D point clouds, and displays them in interactive web-based viewers. The system includes both point cloud and voxelized views, with support for kiosk mode operation on Raspberry Pi devices.

The application consists of:
- A Python backend that captures and processes camera data
- A Flask web server serving interactive 3D visualizations
- Browser-based viewers using Three.js for 3D rendering
- GPIO-controlled navigation for kiosk deployments

## Features

- **Real-time Depth Capture**: Continuous capture from Arducam TOF cameras
- **Point Cloud Generation**: Converts depth data to 3D point clouds with filtering
- **Interactive 3D Visualization**: Web-based viewers with orbit controls
- **Multiple View Modes**:
  - Standard point cloud viewer
  - Voxelized point cloud viewer
- **Kiosk Mode Support**: GPIO button navigation for Raspberry Pi
- **Browser Extension**: Chrome extension for automated navigation
- **Caching Disabled**: Ensures real-time updates in viewers

## How to Run

### Prerequisites

- Python 3.x
- Arducam TOF camera and SDK
- Flask
- OpenCV
- NumPy
- Three.js (loaded via CDN)
- For kiosk mode: Raspberry Pi with GPIO pins

### Installation

1. Clone or download the project
2. Install Python dependencies:
   ```bash
   pip install flask opencv-python numpy
   ```
3. Install Arducam SDK (follow Arducam documentation)

### Running the Application

1. **Start the camera capture**:
   ```bash
   python viz2.py
   ```
   This will begin capturing depth data and saving point clouds to `static/pointcloud.json`

2. **Start the web server** (in a separate terminal):
   ```bash
   python app.py
   ```
   The server will run on `http://localhost:5000`

3. **Access the viewers**:
   - Point cloud view: `http://localhost:5000/`
   - Voxel view: `http://localhost:5000/voxel`

### Kiosk Mode (Raspberry Pi)

For automated kiosk operation:

1. Ensure GPIO pins 23 and 24 are connected to buttons
2. Run the kiosk script:
   ```bash
   python kiosk.py
   ```
   This will start the Flask server, camera capture, and Chromium in kiosk mode with button navigation.

### Browser Extension

The `button_navigation_extension` provides automated navigation between views in kiosk mode. Install it as an unpacked extension in Chrome.

## Project Structure

```
├── app.py                 # Main Flask application
├── kiosk.py               # Kiosk mode script with GPIO controls
├── kiosk-backup.py        # Backup kiosk script
├── viz2.py                # Camera capture and point cloud processing
├── README.md              # This file
├── static/
│   └── pointcloud.json    # Generated point cloud data
├── templates/
│   ├── index.html
│   ├── pcd_view.html
│   ├── pcl_view_json.html # Main point cloud viewer
│   ├── voxalized_pcd_view.html
│   └── voxel_pcl_viewer.html # Voxel viewer
└── button_navigation_extension/
    ├── manifest.json      # Chrome extension manifest
    ├── background.js      # Extension background script
    └── content.js         # Content script for navigation
```
