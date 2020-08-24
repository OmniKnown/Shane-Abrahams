###... Sprint 4 Brief:

###... In this project we are building a facial detection system and Motion detector using OpenCV (Open Source Computer Vision Library). 
###... OpenCV is an open source computer vision and machine learning software library. 
###... OpenCV was built to provide a common infrastructure for computer vision applications 
###... and to accelerate the use of machine perception in the commercial products, and is fully supported by 
###... Python as a library for projects like this one.


import numpy as np
from cv2 import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

img = cv2.imread("Sitting with the pose.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow("img",img)

k = cv2.waitKey(0)
if k == 27:
    # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord("s"):
    # wait for 's' key to save and exit
    cv2.imwrite("NewSitting with the pose.png",img)
    cv2.destroyAllWindows()
