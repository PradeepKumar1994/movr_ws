# movr_ws
> ROS workspace for movr

# Table of contents

## Dependencies

### ROS

```
# rosserial
$ sudo apt install ros-kinetic-rosserial
$ sudo apt install ros-kinetic-rosserial-arduino 
```

```
# Joy
$ sudo apt install ros-kinetic-joy

# Set permission to make accessible to ROS
$ ls -l /dev/input/jsX              # X is the joystick number
$ sudo chmod a+rw /dev/inputjsX
```

```
# Openni - Kinect
$ sudo apt install ros-kinetic-openni-launch
```

```
# Kinect OpenCV 3
$ sudo apt install ros-kinetic-opencv3
```

```
# CV-Bridge
$ sudo apt install ros-kinetic-cv-bridge
# NOTE: You will need to go into the package's CMakeLists.txt and add the following line:
find_package(OpenCV REQUIRED)
# Do not use find_package(catkin ... but add another statement find_package(OpenCV REQUIRED)
```

### Python

```
# API.AI
# Chat bot API
# https://github.com/api-ai/apiai-python-client
$ pip install apiai
```

```
# SpeechRecognition
# Google speech recognition API wrapper
# https://pypi.python.org/pypi/SpeechRecognition/
$ pip install SpeechRecognition
```

```
# gTTS 1.2.1
# Google text-to-speech API wrapper
# https://pypi.python.org/pypi/gTTS/1.2.1
$ pip install gTTS
```

```
# pocketsphinx-python
# CMU speech recognition
# https://github.com/cmusphinx/pocketsphinx-python
# sudo apt-get install python python-all-dev python-pip build-essential swig git libpulse-dev
$ pip install pocketsphinx
```

```
# pygame
# Game engine. Required to use audio library
# https://www.pygame.org/wiki/GettingStarted
$ pip install pygame
```

```
# json
# JSON library
$ pip install json
```
## How to use
```
# Run roscore
$ roscore
```

```
# Run Python rosserial node
$ rosrun rosserial_python serial_node.py /dev/ttyACM1   # Check device name 'ls -la /dev'
```

```
# Run ROS Joy node. Opens joystick device and publishes input
$ rosrun joy joy_node
```

```
# Run movr joy node
$ rosrun movr_teleop_joy joyjoy.py
```

```
# Run voice interface
$ rosrun movr_voice hello_movr.py
```

### View Kinect sensor

```
# Launch openni
# Execute this first before running any of the commands below
$ roslaunch openni_launch openni.launch
```

```
# View RGB image
$ rosrun image_view image_view image:=/camera/rgb/image_color
```

```
# View depth image
$ rosrun image_view image_view image:=/camera/depth/image
```

```
# View depth-disparity
$ rosrun image_view disparity_view image:=/camera/depth/disparity
```

```
# To view RGB - depth correlated images, execute the following
# 1. Remap Depth and Correlate with RGB
$ rosrun rqt_reconfigure rqt_reconfigure
# Open the 'driver' option and select 'reconfigure
#
# 2. Run rviz
$ rosrun rviz rviz
# In cloud_points 2, switch the topic to:  '/camera/depth_registered/points'
```

## Development

## References
