#!/usr/bin/env python2

import os, sys
#import record
import rospy
import dialogflow
import time
from speech_synthesis.srv import synthesis_service
from std_msgs.msg import Int32
from std_msgs.msg import Float64

def send_gesture(command):
    if "Hello!" in command:
        leftWave()
    elif "Bye!" in command:
        rightWave()
    elif command is "a":
        shakeHead()
    else:
        nodHead()

def shakeHead():
    print("Shake head")
    NeckHori = rospy.Publisher('NeckHori_09/command', Float64, queue_size=10)
    NeckHori.publish(0.95)
    time.sleep(.5)
    NeckHori.publish(-0.94)
    time.sleep(.5)
    NeckHori.publish(0.95)
    time.sleep(.5)
    NeckHori.publish(0)
    
def nodHead():
    print("Nod head")
    NeckVert = rospy.Publisher('NeckVert_10/command', Float64, queue_size=10)
    NeckVert.publish(1.5)
    time.sleep(.5)
    NeckVert.publish(0)
    time.sleep(.5)
    NeckVert.publish(0.95)

def leftWave():
    print("Left wave")
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
    NeckHori.publish(0.95)
    NeckVert.publish(0.8)	
    time.sleep(1)
    LArmElbowHori.publish(1.05)
    time.sleep(1)
    LArmElbowHori.publish(0)
    time.sleep(1)
    LArmElbowHori.publish(1.05)
    time.sleep(1)
    LArmElbowHori.publish(0)


def rightWave():
    print("Right wave")
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
    NeckHori.publish(-0.94)
    NeckVert.publish(0.8)	
    time.sleep(1)
    RArmElbowHori.publish(0)
    time.sleep(1)
    RArmElbowHori.publish(1.89)
    time.sleep(1)
    RArmElbowHori.publish(0)
    time.sleep(1)
    RArmElbowHori.publish(1.89)

def bothWave():
    print("Both wave")
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
    LArmShoulderVert.publish(0)
    LArmShoulderHori.publish(0.84)
    LArmElbowVert.publish(1.05)
    LArmElbowHori.publish(-1.5)	
    time.sleep(2)
    RArmElbowHori.publish(0)
    LArmElbowHori.publish(1.05)
    time.sleep(2)
    RArmElbowHori.publish(1.05)
    LArmElbowHori.publish(0)	
    time.sleep(2)
    RArmElbowHori.publish(0)
    LArmElbowHori.publish(1.05)
    time.sleep(2)



def raiseArms():
    print("Raise arms")
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
    LArmShoulderVert.publish(0)
    LArmShoulderHori.publish(0.84)
    LArmElbowVert.publish(1.05)
    LArmElbowHori.publish(0)


def lowerArms():
    print("Lower arms")
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
    LArmShoulderVert.publish(2.52)
    LArmShoulderHori.publish(1.89)
    LArmElbowVert.publish(1.05)
    LArmElbowHori.publish(0)
    pass

def recognition(): 
    rospy.init_node('voice_recognition', anonymous=True)
    #record.record()
    os.system("./record.py")
    response = dialogflow.dialogflow_main()
    if len(response) is 0:
        response = "I can't hear you!"
    rospy.loginfo(response)
    send_gesture(response)
    print(response)
    speech_synthesis = rospy.ServiceProxy('speech_synthesis', synthesis_service)
    return speech_synthesis(response)


if __name__ == '__main__':
    rospy.wait_for_service('speech_synthesis')
    while(True):
        recognition()
        raw_input("Press Enter to continue...")

