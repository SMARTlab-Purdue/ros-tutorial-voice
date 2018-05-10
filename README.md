# ROS Tutorial for Controlling Robot using Voice
ROS tutorial by Purdue SMART lab: This tutorial shows how to use ROS packages to control robot using voice.

# Objectives
This tutorial briefly covers how to control a robot over voice command. The user can control the robot using voice command and the robot acknowledges back to the user through a text-to-speech system, after executing the control action.

E.g. Once the user ask the robot to "forward". The robot executes it and then sends a message over voice to the user saying the the "Requested action executed".

## Demonstration video:
Please watch the videos below to get an idea of what you can expect to achieve from this tutorial.

https://youtu.be/DZRAPy7TteU>

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/DZRAPy7TteU/0.jpg)](https://youtu.be/DZRAPy7TteU)


# Credits
This tutorial is prepared by Manoj Penmetcha (mpenmetc@purdue.edu) and Yeonju Ho.

The git repository is maintained by Ramviyas Parasuraman (ramviyas@purdue.edu).

We acknowledge the following sources that were used to prepare this tutorial:

Voice Recognition: http://jokla.me/robotics/speech-recognition-ros/

IBM TTS API: https://github.com/ArthurHlt/tts-watson-ros

# Prerequisites

Fundamental background of using Linux-based OS and ROS will be required to fully understand the following tutorial. For more information, please visit:

http://wiki.ros.org/ROS/Tutorials

and

http://files.ubuntu-manual.org/manuals/getting-started-with-ubuntu/14.04e2/en_US/screen/Getting%20Started%20with%20Ubuntu%2014.04%20-%20Second%20edition.pdf

# Tutorial

* [Section 1: Installation of relevant dependencies/packages](https://github.com/SMARTlab-Purdue/ros-tutorial-gazebo-simulation/wiki/Sec.-1:-Installation-of-dependencies)

* [Section 2: Driving Husky robot in Gazebo simulation](https://github.com/SMARTlab-Purdue/ros-tutorial-gazebo-simulation/wiki/Sec.-2:-Driving-the-Husky-robot-in-Gazebo)

* [Section 3: Creating a custom robot and a custom sensor](https://github.com/SMARTlab-Purdue/ros-tutorial-gazebo-simulation/wiki/Sec.-3:-Creating-a-custom-robot-and-sensor-model)

* [Section 4: Creating a light sensor plugin in Gazebo](https://github.com/SMARTlab-Purdue/ros-tutorial-gazebo-simulation/wiki/Sec.-4:-Creating-a-light-sensor-plugin)

# Summary
In this tutorial, we presented an introduction to using Gazebo simulation for robot navigation and control. Also, we saw how to create a custom robot with a custom sensor and able to publish the sensor outputs on ROS topics. 

The tutorials are summarized and adapted from the sources mentioned in Section 2. We hope this tutorial will be helpful to anyone starting out with Gazebo and ROS.


