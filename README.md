# DoubleDQN_turtlebot2
Double DQN implementation on ROS based TurtleBot 2 Robot

This is an implementation of Double DQN algorithm on a Turtlebot 2 Robot.

Python interpreter: Python 3.6

ROS Version: ROS Melodic

Gazebo: Gazebo 9.0.0

OS: Ubuntu 18.04

You will also need to install openai_ros ROS package(http://wiki.ros.org/openai_ros) to access open AI based environement and commands for training the robot. You can follow this tutorial from ROS to set it up: http://wiki.ros.org/openai_ros/TurtleBot2%20with%20openai_ros
Laser scan mounted on top of TurtleBot robot is used for training the robot and it is also possible to extend it to Camera images with minor changes, however, I will not show that in this code. 

Below is a list(generated via conda list) of python packages you will need, I suggest create a Conda environment with these libraries for smooth running.

_libgcc_mutex             0.1

ca-certificates           2021.1.19

catkin-pkg                0.4.23

certifi                   2020.12.5

cloudpickle               1.6.0

cycler                    0.10.0

dataclasses               0.8

defusedxml                0.7.1

distro                    1.5.0

docutils                  0.16

future                    0.18.2

gitdb                     4.0.5

gitpython                 3.1.14

gym                       0.18.0

kiwisolver                1.3.1

ld_impl_linux-64          2.33.1

libedit                   3.1.20191231

libffi                    3.3

libgcc-ng                 9.1.0

libstdcxx-ng              9.1.0

matplotlib                3.3.4

ncurses                   6.2

numpy                     1.19.5

openssl                   1.1.1j

pillow                    7.2.0

pip                       21.0.1

pyglet                    1.5.0

pyparsing                 2.4.7

python                    3.6.13

python-dateutil           2.8.1

pyyaml                    5.4.1

readline                  8.1

rospkg                    1.2.10

scipy                     1.5.4

setuptools                52.0.0

six                       1.15.0

smmap                     3.0.5

sqlite                    3.33.0

tk                        8.6.10

torch                     1.8.0

torchvision               0.9.0

typing-extensions         3.7.4.3

wheel                     0.36.2

xz                        5.2.5

zlib                      1.2.11

To use the project, first create a ROS package with name fa_turtlebot inside .../catkin_ws/src .Then paste files of this repository inside .../catkin_ws/src/fa_turtlebot/src, build the package. Open terminal and activate the environement with the python packages, then type roslaunch fa_turtlebot start_training.launch to start the training. If everything is set right, you should see a Gazebo window popup, with robot moving inside it, as can be seen in snapshot.png. You can use the rviz config file to visualize laser scan data map as the robot progresses in the environment.

Feel free to use or modify this code as per your need, happy coding!
Connect over LinkedIn: https://www.linkedin.com/in/praveen-kumar-b2096391/

Follow me on my Medium blog, I will be adding some interesting stuff soon: https://praveenkumar2909.medium.com/
