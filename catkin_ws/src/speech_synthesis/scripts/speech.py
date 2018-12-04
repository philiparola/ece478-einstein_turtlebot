#!/usr/bin/env python

# Speech Synthesis Script
# V1.0
# Created by Scott Matsuo for Intelligent Robotics 1 Project 2
# Last Update - 12/03/2018
#
#
# Service Requests
# /phrase - String
#
# Service Response
# /status - int32

from speech_synthesis.srv import synthesis_service
import rospy
import boto3
from pygame import mixer

import pyttsx

polly_client = boto3.Session(
	aws_access_key_id="AKIAIPRMWBCHKHIPA2OA",                     
	aws_secret_access_key="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",
	region_name='us-west-2').client('polly')

mixer.init()

def handle_speech_synthesis(req):
	'''
	response = polly_client.synthesize_speech(VoiceId='Joey',
				OutputFormat='mp3', 
				Text = str(req))
	file = open('speech.mp3', 'w')
	file.write(response['AudioStream'].read())
	file.close()
	mixer.music.load('speech.mp3')
	mixer.music.play()
	'''
	engine = pyttsx.init()
	#word = str(req)[6:-1]
	engine.say(str(req)[6:-1])
	rospy.loginfo(str(req))
	engine.runAndWait()
	return 1
	
def speech_synthesis_server():
	rospy.init_node('speech_synthesis_server')
	s = rospy.Service('speech_synthesis', synthesis_service, handle_speech_synthesis)
	print("Ready to synthesize.")	
	rospy.spin()

if __name__ == "__main__":
	speech_synthesis_server()
