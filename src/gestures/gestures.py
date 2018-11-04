#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    	listener()
    except rospy.ROSInterruptException:
        pass




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