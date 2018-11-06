# ece478-turtlebot
The Einstein TurtleBot for ECE478@PSU (Robotics I), Fall 2018

## Authors
[@philiparola](https://github.com/philiparola) 
[@k10scmats](https://github.com/k10scmats) 

## License
All original code produced by this team is licensed under the GPLv2.  All code from previous terms, outside projects, etc. are licensed under their own terms.

## Repository Structure
```
archive         --> Old code from previous students
cad             --> CAD files
catkin_ws       --> Source code
deliverables    --> Lab report and presentation, as well as supplementary media
docs            --> Misc. documentation (eg: BOM, purchase list)
```

## Project Requirements
Project 1 is due ~~Monday November 5~~ Wednesday November 7th.  You can and should use software from previous classes that is on D2L, software from Melih and from Internet. Just write what software you use and for what. 

The minimum requirements for Human on Mobile Base robots are the following:
1.	~~Robot muse be able to move forward, backward, left, right, turn around, dance.~~ Due to unavoidable drama, this is no longer a requirement for us.
2.	Robot must have some simple body gestures like greeting, hello, good bye, shake hand, etc.
3.	~~Robot must have speech capabilities: word or sentence recognition and text to speech.~~
4.	Robot must have some vision capabilities: recognize human face (not who this person is, only that human is present and where) , recognize object (like big red box or yellow round object etc), or recognize another robot (which one).
5.	~~Robot must use some type of Machine Learning, Evolutionary algorithm, neural net or fuzzy logic. Take it from previous projects and integrate.~~ This requirement appears to have been dropped, but we've still implemented fuzzy logic.
6.	You have to deliver 3 items: (1) report in Word, (2) presentation in PowerPoint, (3) video. Report must be inclusive and the role of each student from the team should be clear. PPT presentation must allow you to deliver a good speech in front of class, what did you achieve, what else you want to learn.

## Platform
This project is for the [TurtleBot2](https://www.turtlebot.com/turtlebot2/).  (From [Wikipedia](https://en.wikipedia.org/wiki/TurtleBot)) TurtleBot is a low-cost, personal robot kit with open source software. TurtleBot was created at Willow Garage by Melonee Wise and Tully Foote in November 2010.  The TurtleBot kit consists of a mobile base, 3D Sensor, laptop computer, and the TurtleBot mounting hardware kit. In addition to the TurtleBot kit, users can download the TurtleBot SDK from the ROS wiki.

The TurtleBot2 uses [ROS Kinetic](http://wiki.ros.org/kinetic/Installation) as its software platform.

### Setup Controller
Due to unavoidable drama, we are no longer using the mobile base of the TurtleBot.  We are going to be running the demo off of a laptop.

<strike>Hardware: Intel Joule (Unknown version)

OS Version: Linux turtlebot2 4.4.0-1000-joule #0+joule21-Ubuntu SMP PREEMPT Thu Mar 16 14:46:45 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

u: turtle2

p: turtlebot


Ubuntu 16.04 and ROS Kinetic came preinstalled courtesy of Melih.

1) Clone Github Repo
2) TBD
</strike>
 
### Setup Development computer
Following the [ROS Kinetic install guide](http://wiki.ros.org/kinetic/Installation/Ubuntu):
```bash
# Setup ROS Kinetic
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
sudo rosdep init
rosdep update
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
# Install required (non-default) ROS packages
sudo apt-get install ros-kinetic-dynamixel-controllers
# Install extra dev tools
sudo apt install python-opencv python-pip python3-pip python-dev python3-dev

# Optional: Install development environment
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install chromium-browser code vim vim-gtk
```

## Building the project
### NOTE: Catkin configured itself to use absolute paths, so you will have to fix this before building.  You can run:
```bash
find . -type f | xargs sed -i  's/home\/parola\/ece478-turtlebot\/catkin_ws/home\/YOUR_NAME\/ece478-turtlebot\/catkin_ws/g'
```

```bash
source /opt/ros/kinetic/setup.bash
source <repository_dir>/catkin_ws/devel/setup.bash
cd catkin_ws/
catkin_make
```
 
## Running the project
```bash
chmod a+rw /dev/ttyUSB0		# Unless more than one USB->Serial adapter
# Now launch these in seperate terminals, or some other method of multitasking
roslaunch my_dynamixel_tutorial controller_manager.launch
roslaunch my_dynamixel_tutorial start_all_motor_controller.launch
roslaunch face_detection face_detection.launch
roslaunch gesture_controls gesture_controls.launch
```
