#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Float64

face_angle_global = None


def callback(data):
	global face_angle_global
	face_angle_global = data.data
	# rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def leftWave():
	print("LEFT")


def rightWave():
	print("RIGHT")






rospy.init_node('gesture_control', anonymous=True)
sub = rospy.Subscriber("face_angle", Int32, callback)
rate = rospy.Rate(10) # 10hz

while not rospy.is_shutdown():
	rospy.Subscriber("face_angle", Int32, callback)
	if -100 < face_angle_global < 100:
		if face_angle_global < 0:
			leftWave()
		else:
			rightWave()
	else:
		print("not in range")
		pass
	rate.sleep()



# main thread psuedocode
	# setup ros subscriptions and publishers
	# main loop
		# get in face 
		# if face in detection zone
			# detect the side
				# enter animation, animation will have waiting built in to block from main loop
			# else
				# enter otherside animation
		# else (if not in detection zone)
			# pass (perhaps wait?)
	# set break condition for main loop
	# return

# animation pseudocode
	# publish default positions
	# publish arm position
		# order the publishes properly, of course
	# wait
	# publish next arm position in sequeence of poses
	# wait aain
	# repeat this until done
	# wait
	# reset to default position
	# return
