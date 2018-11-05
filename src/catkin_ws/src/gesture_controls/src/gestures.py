#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Float64
import time

face_angle_global = None


def callback(data):
	global face_angle_global
	face_angle_global = data.data
	# rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def leftWave():
	print("LEFT")
	RArmShoulderVert = rospy.Publisher('RArmShoulderVert_01/command', Float64, queue_size=10)
	RArmShoulderHori = rospy.Publisher('RArmShoulderHori_02/command', Float64, queue_size=10)
	RArmElbowVert = rospy.Publisher('RArmElbowVert_03/command', Float64, queue_size=10)
	RArmElbowHori = rospy.Publisher('RArmElbowHori_04/command', Float64, queue_size=10)
	LArmShoulderVert = rospy.Publisher('LArmShoulderVert_05/command', Float64, queue_size=10)
	LArmShoulderHori = rospy.Publisher('LArmShoulderHori_06/command', Float64, queue_size=10)
	LArmElbowVert = rospy.Publisher('LArmElbowVert_07/command', Float64, queue_size=10)
	LArmElbowHori = rospy.Publisher('LArmElbowHori_08/command', Float64, queue_size=10)
	NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
	NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
	RArmShoulderVert.publish(0)
	RArmShoulderHori.publish(0)
	RArmElbowVert.publish(1.05)
	RArmElbowHori.publish(1.89)
	LArmShoulderVert.publish(0)
	LArmShoulderHori.publish(0.84)
	LArmElbowVert.publish(1.05)
	LArmElbowHori.publish(0)
	NeckHori.publish(0)
	NeckVert.publish(0.8)	
	time.sleep(1)
	LArmElbowHori.publish(1.05)
	time.sleep(1)


def rightWave():
	print("RIGHT")
	RArmShoulderVert = rospy.Publisher('RArmShoulderVert_01/command', Float64, queue_size=10)
	RArmShoulderHori = rospy.Publisher('RArmShoulderHori_02/command', Float64, queue_size=10)
	RArmElbowVert = rospy.Publisher('RArmElbowVert_03/command', Float64, queue_size=10)
	RArmElbowHori = rospy.Publisher('RArmElbowHori_04/command', Float64, queue_size=10)
	LArmShoulderVert = rospy.Publisher('LArmShoulderVert_05/command', Float64, queue_size=10)
	LArmShoulderHori = rospy.Publisher('LArmShoulderHori_06/command', Float64, queue_size=10)
	LArmElbowVert = rospy.Publisher('LArmElbowVert_07/command', Float64, queue_size=10)
	LArmElbowHori = rospy.Publisher('LArmElbowHori_08/command', Float64, queue_size=10)
	NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
	NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
	RArmShoulderVert.publish(2.52)
	RArmShoulderHori.publish(0.95)
	RArmElbowVert.publish(1.05)
	RArmElbowHori.publish(1.89)
	LArmShoulderVert.publish(2.52)
	LArmShoulderHori.publish(1.89)
	LArmElbowVert.publish(1.05)
	LArmElbowHori.publish(0)
	NeckHori.publish(0)
	NeckVert.publish(0.8)	
	time.sleep(1)
	RArmElbowHori.publish(1.89)
	time.sleep(1)





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
