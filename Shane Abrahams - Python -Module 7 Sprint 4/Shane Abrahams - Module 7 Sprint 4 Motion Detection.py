###... Sprint 4 Brief:

###... In this project we are building a facial detection system and Motion detector using OpenCV (Open Source Computer Vision Library). 
###... OpenCV is an open source computer vision and machine learning software library. 
###... OpenCV was built to provide a common infrastructure for computer vision applications 
###... and to accelerate the use of machine perception in the commercial products, and is fully supported by 
###... Python as a library for projects like this one.

# import packages
import numpy as np
from cv2 import cv2

cap = cv2.VideoCapture('Need For Speed Movie CLIP - The Car Is Loose (2014) - Aaron Paul, Imogen Poots Movie HD.mp4')

# resize the frame, convert it to grayscale
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

out = cv2.VideoWriter("Need For Speed Movie CLIP - MD.avi", fourcc, 5.0, (1280,720))

# resize the frame, convert it to grayscale
ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        # compute the bounding box for the contour, draw it on the frame,
		# and update the text
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Alot of Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    image = cv2.resize(frame1, (1280,720))
    out.write(image)
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()