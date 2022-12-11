import cv2
#import tensorflow as tf
from collections import OrderedDict
import time
import datetime
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.saved_model import load
from tensorflow.image import resize
from tensorflow import reshape
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import zipfile
import argparse
#import firebaseClient 

#test
# https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html#identifiy-objects

def main():

    # 0 sets to video camera and 1 for webcam
    capture = cv2.VideoCapture(0)
    # image = cv2.imread('bottle.jpg')
    # need sleep time to connect to camera image
    time.sleep(5)
    while True:
        true, image = capture.read()
        testForObjet(image)


def testForObjet(image):
    #  model from GarbageML
    #garbageNet = load("model")
    #garbageNet = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
    # blob
    #i
    # image = cv2.resize(image, )
    img_array = np.array(image)
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (127.5, 127.5, 127.5), False)
    #image = image.resize((300,300))
    blob = reshape(blob,shape = [1,300,300, 3])

    garbageNet = load_model("model")
    #garbageNet(inputs=blob, outputs=outputs).setInput(blob)
    outputs = []
    p = garbageNet.predict(blob)
    n = (garbageNet.predict(blob) > 0.5).astype("int32")
    c = np.argmax(garbageNet.predict(blob), axis=1)
    print(p)
    print(c)
    print(n)
    class_names = ["cardboard", "glass", "metal", "paper", "plastic","trash"]
    cv2.putText(image, class_names[c[0]], org=( 50, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.FILLED)
    #cv2.putText(image,str(p[0][c[0]]), org=( 50, 100), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.FILLED)
    cv2.putText(image, "confidence: " + str(p[0][c[0]] *100 ) + "%", org=( 50, 100), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.FILLED)
    cv2.imwrite('objetDetected 2' +str(datetime.datetime.now()) + '.png', image)
    # fbClient = firebaseClient.firebaseClient("4HD4nUV5Kkkkt4AUxmSC")
    # fbClient.uploadNewCollectionEvent('objetDetected.png', 0.0, class_names[c[0]])

#fbClient = firebaseClient.firebaseClient("4HD4nUV5Kkkkt4AUxmSC")
main()