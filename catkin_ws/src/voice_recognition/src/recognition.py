#!/usr/bin/env python2

import os, sys
#import record
import rospy
import dialogflow
#from speech_synthesis.srv import *

def recognition():
    #record.record()
    os.system("./record.py")
    response = dialogflow.dialogflow_main()
    #synthesize_voice = rospy.ServiceProxy('speech_synthesis', synthesis_service)
    #return speech_synthesis()
    if len(response) is 0:
        response = "a"
    command = "rosservice call \/speech_synthesis \'" + response + "\'"
    print(command)  # Somehow fixes a type error?
    os.system(str(command))


if __name__ == '__main__':
    rospy.wait_for_service('speech_synthesis')
    while(True):
        recognition()
        raw_input("Press Enter to continue...")

