#!/usr/bin/python3
import cv2
import sys
import numpy

# Setup data
cascPath = "haarcascade_frontalface_default.xml"
webcam = cv2.VideoCapture(0)
webcamWidth = webcam.get(3)

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

    #print("Found {0} faces!".format(len(faces)))

    largestFaceSize = 0
    largestFaceLocation = 0

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if (w*h) > largestFaceSize:
            largestFaceSize = (w*h)
            if (x+(w/2)) > webcamWidth/2:
                largestFaceLocation = (x+(w/2)) - (webcamWidth/2)
            else:
                largestFaceLocation = ((x+(w/2)) - (webcamWidth/2))

    print("Face is {0} degrees from the center!".format(largestFaceLocation))

    if displayPresent is True:
        cv2.imshow("Faces found", frame)
        if cv2.waitKey(10) == 27:
            # Hit esc
            break
    else:
        pass    # no display

cv2.destroyAllWindows()
