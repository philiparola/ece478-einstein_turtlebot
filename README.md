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
The controller was used only for Part 2, but it very likely works in Part 1.
#### Install ROS to Raspberry Pi (INCOMPLETE)
There are many ways to install ROS on a Raspberry Pi.  [The offical method](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi) failed for us, but may work for you.  Melih seems to have followed that guide.
If you download Melih's custom ROSPi images (download links withheld; we see you crawlers), it is a zip file seperated into parts, and will need to be combined.  On Unix, run 'rospi.zip.00* > rospi.zip' to combine them.  Then burn the .img file to the SD by running 'sudo dd bs=4M if=rospi.img of=/dev/sdX conv=fsync' (DESTRUCTIVE: triple check to make sure the command is correct).
On Windows, follow [this guide to combine the files](http://mwiki.gichd.org/IM/Combine_several_zip_files), then [this guide to write to SD](http://www.alanlay.com/blog/2014/6/8/raspberry-pi).

You are definatly going to want to make sure that your filesystem is fully expanded. Run 'sudo raspi-config', and the TUI is actually intuitive.

#### Missing ROS packages
You may have more packages missing than us, but this should point you in the right direction.
Run 'rosdep update'
TODO: NOT YET COMPLETE.  As of now, the Pi isn't working.  actionlib (required by my_dynamixel_tutorial, and probably the others) is missing, and I haven't figured out how to install it.

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



## Project 2
 Please note that I will keep updating this announcement!

Project 2 is due on Dec 7th. Friday at 5:00 PM

Project 2 is 30% of your final grade.

Project 2 Grading:

* ROS Implementation: 30 points
* Speech Recognition with Dialogflow: 10 points
* Speech Synthesis with Amazon Polly: 10 points
* Demo : 10 points
* Team Work: 10 points
* Project Report and Deliverables: 30 points

You can find more information about project 2 grading, the requirements, and demo below.

### Project 2 Requirements:

For project 1 you successfully built robots that can do different kinds of motions such as moving forward, backward, left, right, turning around, dancing, drumming etc.  For project 2 you must implement all these functions in ROS. (30 points) 

* I should be able to control your robot by publishing to ROS topics
* I should be able to see the current state of the robot by subscribing to topics. Any sensor data, positions of all the actuators etc..
* Your ROS project must be modular which means that you have to make sure that each node responsible for doing only one job and they should not depend on each other. If you really believe that it is necessary and there is no other way to do it, maybe you can do two things in one node. DO NOT try to implement everything in one node. For example:
    * node1: responsible for motion: subscribes to a topic/s and moves the robot forward, backward, left, right etc,
    * node2: responsible for speech recognition,
    * node3: responsible for speech synthesis etc.,
    * node 4: responsible for reading sensors and publishing sensor values to topics
    * etc...
* When you create topics, you should pick good names
* You can use your computer or a Raspberry Pi to use ROS 
    You must implement speech recognition into your robot by using Google Dialogflow. (10 points)
* You are going to create a ROS node or a service to complete this part.
* You will create several dialogs using Dialogflow.
* I should be able to have a small talk with your robot.
* A Part of Lecture 9 is going to be about Speech Recognition and Dialog Flow.
* Also, I recorded a video lecture about How to use Dialogflow with Python? I am going to post it on D2L on Tuesday.



You must implement speech synthesis into your robot by using Amazon Polly.  (10 points)

* Your robot must be able to speak when I publish any string to a topic
* You are going to create a ROS node or a service to complete this part.
* You must choose a voice that fits the character of your robot.
* A Part of Lecture 9 is going to be about Speech Synthesis and Amazon Polly.
* Also, I recorded a video lecture about How to use Amazon Polly with Python? I am going to post it D2L on Tuesday.

Demo and Presentation (10 points) :

* You must play a small part in Dr. Perkowski's Robot Theater Scripts. (I will post more information about this requirement)
* You must work with another team to complete the Robot Theater requirement.
* You have 30 minutes to complete your demo
    * ROS Implementation: 30 points
    * Speech Recognition with Dialogflow: 10 points
    * Speech Synthesis with Amazon Polly: 10 points
    * Demo : 10 points
    * Team Work: 10 points
    * Project Report and Deliverables: 30 points
* If you are late for your demo, you have to wait until the next available demo time to do your demo.

Teamwork is important, so when you demo your project2 each team member must talk about their part in the project (10 points)

You can select your time slot for your demo at TBD.

* Make sure you type your name and your project partner's full names when you submit your request.
    * Ex: Melih Erdogan - Marek Perkowski
* It is enough if only one team member submits your demo time.
* You can only choose one timeslot.
* All team members should come to the demo. 
* Please make sure that you are ready to do your demo before your demo time and do not use your demo time to set up your robots and computers

Project Deliverables:  (30 points) - Dec 7th, Friday is the due date for project deliverables 

* Submit your project files on D2L in a zip file. (TeamName_Robotics1_Fall2018_Project2.zip)
    One submission from each team is enough.
* PowerPoint Slides
* Porject2 Report (word and .pdf files)
* Pictures
* Videos (Links Only)
* You must create a GitHub repository for your project and all project files (Add the link to your repository into your project report)
* Use this repository as an example.
    https://github.com/mlherd/sample_project

Melih

Teaching Assistant

### Project 2 Setup for more libraries
This part of the project utilizes Amazon Polly and Google DialogFlow for it's speech engine.  These take a little bit of work to install.
```shell
# You may run the following remove operations if you encounter errors
sudo apt remove python-pyasn1-modules
sudo pip2 uninstall pyasn
sudo pip2 install dialogflow
sudo apt-get install python-pyaudio
# if libsound.so not found YOU MAY HAVE TO RUN sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
export GOOGLE_APPLICATION_CREDENTIALS="/home/parola/turtlebot-1cb15-3ecbc66bd3e8.json"

sudo pip install boto3
sudo pip install awscli
sudo pip install pygame
aws configure
    AWS Access Key ID [None]: SECRET
    AWS Secret Access Key [None]: SECRET
    Default region name [None]: us-west-2
    Default output format [None]: mp3
```

## Running Project 2
Project 2 consists of two parts; robot theater, and interactive mode.

### Robot Theater
Robot Theater mode is where the robot uses Amazon Polly to speak lines from a play alongside another robot.  You must be connected to a LAN to run in this mode, because the director controls both robots speaking lines.
TODO: Network layout, how to launch

### Interactive Mode 
The robot utilizes Amazon Polly and Google DialogFlow to interact with people.  The robot will speak in response to people, and gesture depending on what has been said.
To run interactive mode:
```shell
chmod a+rw /dev/ttyUSB0		# Unless more than one USB->Serial adapter
roslaunch my_dynamixel_tutorial controller_manager.launch
roslaunch my_dynamixel_tutorial start_all_motor_controller.launch
rosrun speech_synthesis speech.py
roslaunch voice_recognition voice_recognition.launch
# To test, rosservice call /speech_synthesis 'Hello!'
```
