import cv2
import sys

# Get user supplied values
cascPath = "haarcascade_frontalface_default.xml"
webcam = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

while webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
#else:
#    rval = False


    # Read the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #cv2.imshow("Faces found", frame)
    #cv2.waitKey(0)
