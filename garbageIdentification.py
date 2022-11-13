import cv2
import time
import datetime
import numpy as np


# https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html#identifiy-objects

def main():

    # 0 sets to video camera and 1 for webcam
    capture = cv2.VideoCapture(1)
    # image = cv2.imread('bottle.jpg')
    # need sleep time to connect to camera image
    time.sleep(5)
    while True:
        true, image = capture.read()

        time.sleep(5)
        if testForObjet(image):
            # object detected sleep for time and send to db
            time.sleep(5)


def testForObjet(image):
    net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    ln = net.getLayerNames()

    blob = cv2.dnn.blobFromImage(
        image, 1/255.0, (416, 416), swapRB=True, crop=False)
    r = blob[0, 0, :, :]

    cv2.imshow('blob', r)
    text = f'Blob shape={blob.shape}'
    cv2.displayOverlay('blob', text)
    cv2.waitKey(1)
    # net.setInput(blob)
    # t0 = time.time()
    # outputs = net.forward(ln)
    #t = time.time()

    #cv2.displayOverlay('window', f'forward propagation time={t-t0}')
    #cv2.imshow('window',  image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    exit
    detected = False
    if detected:

        print("detected")
    else:
        print("no detection")

    return detected


#fbClient = firebaseClient.firebaseClient("4HD4nUV5Kkkkt4AUxmSC")
main()
