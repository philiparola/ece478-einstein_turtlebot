#!/usr/bin/python2
import cv2
import sys
import numpy
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

# Setup data
cascPath = "haarcascade_frontalface_default.xml"
webcam = cv2.VideoCapture(0)
webcamWidth = webcam.get(3)
webcamHeight = webcam.get(4)
deadzone = 200

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

black_image = numpy.zeros((288, 382))

# Detect if display is present
try:
    cv2.imshow("test image", black_image)
    displayPresent = True
    cv2.destroyAllWindows()
except:
    displayPresent = False

# ROS setup
faceAngle_pub = rospy.Publisher('face_angle', Int32, queue_size=10)
faceCount_pub = rospy.Publisher('face_count', Int32, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 10hz

while webcam.isOpened():
    rval, frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    largestFaceSize = 0
    largestFaceLocation = 0

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.line(frame, (x+(w/2),y), (x+(w/2),y-(h/8)),(0,255,0), 2)
        cv2.line(frame, (x+(w/2),y+h), (x+(w/2),y+h+(h/8)),(0,255,0), 2)
        if (w*h) > largestFaceSize:
            largestFaceSize = (w*h)
            if (x+(w/2)) > webcamWidth/2:
                largestFaceLocation = (x+(w/2)) - (webcamWidth/2)
            else:
                largestFaceLocation = ((x+(w/2)) - (webcamWidth/2))

    rospy.loginfo(largestFaceLocation)
    rospy.loginfo(len(faces))
    faceAngle_pub.publish(largestFaceLocation)
    faceCount_pub.publish(len(faces))
    rate.sleep()

    if displayPresent is True:
        cv2.line(frame, (int(webcamWidth/2)+deadzone,0),
                 (int(webcamWidth/2)+deadzone,int(webcamHeight)), (0,0,255), 3)
        cv2.line(frame, (int(webcamWidth/2)-deadzone,0),
                 (int(webcamWidth/2)-deadzone,int(webcamHeight)), (0,0,255), 3)
        cv2.line(frame, (int(webcamWidth/2),0),
                 (int(webcamWidth/2),int(webcamHeight)), (255,0,0), 2)
        cv2.imshow("Faces found", frame)
        if cv2.waitKey(10) == 27:
            # Hit esc
            break
    else:
        pass    # no display

cv2.destroyAllWindows()
