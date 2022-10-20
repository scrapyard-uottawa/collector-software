import cv2 as cv
import numpy as np

#  open the raspbery pi camera in opencv
cap = cv.VideoCapture(0)

#  set the resolution of the camera to 640x480
cap.set(3, 640)
cap.set(4, 480)

# open the camera in a window for 30 seconds
while True:
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
