# DoubleDQN_turtlebot2
Double DQN implementation on ROS based TurtleBot 2 Robot

This is an implementation of Double DQN algorithm on a Turtlebot 2 Robot.
Python interpreter: Python 3.6
ROS Version: ROS Melodic
Gazebo: Gazebo 9
You will also need to install openai_ros ROS package(http://wiki.ros.org/openai_ros) to access open AI based environement and commands for training the robot. You can follow this tutorial from ROS to set it up: http://wiki.ros.org/openai_ros/TurtleBot2%20with%20openai_ros
Laser scan mounted on top of TurtleBot robot is used for training the robot and it is also possible to extend it to Camera images with minor changes, however, I will not show that in this code. 

Below is a list(generated via conda list) of python packages you will need, I suggest create a Conda environment with these libraries for smooth running.
**Name**                  **Version**           **Build**

_libgcc_mutex             0.1                        main

ca-certificates           2021.1.19            h06a4308_1

catkin-pkg                0.4.23                   pypi_0

certifi                   2020.12.5        py36h06a4308_0

cloudpickle               1.6.0                    pypi_0

cycler                    0.10.0                   pypi_0

dataclasses               0.8                      pypi_0

defusedxml                0.7.1                    pypi_0

distro                    1.5.0                    pypi_0

docutils                  0.16                     pypi_0

future                    0.18.2                   pypi_0

gitdb                     4.0.5                    pypi_0

gitpython                 3.1.14                   pypi_0

gym                       0.18.0                   pypi_0

kiwisolver                1.3.1                    pypi_0

ld_impl_linux-64          2.33.1               h53a641e_7

libedit                   3.1.20191231         h14c3975_1

libffi                    3.3                  he6710b0_2

libgcc-ng                 9.1.0                hdf63c60_0

libstdcxx-ng              9.1.0                hdf63c60_0

matplotlib                3.3.4                    pypi_0

ncurses                   6.2                  he6710b0_1

numpy                     1.19.5                   pypi_0

openssl                   1.1.1j               h27cfd23_0

pillow                    7.2.0                    pypi_0

pip                       21.0.1           py36h06a4308_0

pyglet                    1.5.0                    pypi_0

pyparsing                 2.4.7                    pypi_0

python                    3.6.13               hdb3f193_0

python-dateutil           2.8.1                    pypi_0

pyyaml                    5.4.1                    pypi_0

readline                  8.1                  h27cfd23_0

rospkg                    1.2.10                   pypi_0

scipy                     1.5.4                    pypi_0

setuptools                52.0.0           py36h06a4308_0 

six                       1.15.0                   pypi_0

smmap                     3.0.5                    pypi_0

sqlite                    3.33.0               h62c20be_0

tk                        8.6.10               hbc83047_0

torch                     1.8.0                    pypi_0

torchvision               0.9.0                    pypi_0

typing-extensions         3.7.4.3                  pypi_0

wheel                     0.36.2             pyhd3eb1b0_0

xz                        5.2.5                h7b6447c_0

zlib                      1.2.11               h7b6447c_3

Feel free to use this code or modify it as per your need, happy coding!
Connect over LinkedIn: https://www.linkedin.com/in/praveen-kumar-b2096391/
