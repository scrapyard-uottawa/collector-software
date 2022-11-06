import cv2
import time
import datetime
import numpy as np
import firebaseClient

# https://automaticaddison.com/how-to-detect-and-draw-contours-in-images-using-opencv/
# https://stackoverflow.com/questions/28013435/how-i-can-count-bounding-boxes-in-each-frame


def main():
    # 0 sets to video camera and 1 for webcam
    capture = cv2.VideoCapture(1)
    # image = cv2.imread('bottle.jpg')
    # need sleep time to connect to camera image
    time.sleep(2)
    while True:
        true, image = capture.read()

        time.sleep(5)
        if testForObjet(image):
            # object detected sleep for time and send to db
            time.sleep(5)


def testForObjet(image):

    # saves image photo
    # needs to send to db

    # turn image greyscale
    imageGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #imageBlur = cv2.GaussianBlur(imageGrey, (5, 5), 0)
    ret3, imageBinary = cv2.threshold(
        imageGrey, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print(ret3)

    cv2.imwrite('objetDetected 2' +
                str(datetime.datetime.now()) + '.png', imageBinary)

    # find the contures
    contours, hierarchy = cv2.findContours(
        imageBinary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # draw contures on a copy of the image
    imageContures = image.copy()
    cv2.drawContours(imageContures, contours, -1, (0, 255, 0), 3, 32)
    imageRectangle = image.copy()
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        # if detected contures have above a certain width and hight then an object was detected.
        detected = False
        if 1920 > w and w >= 50 and h >= 50 and 1080 > h and 130 > ret3:
            detected = True
            cv2.rectangle(imageRectangle, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imwrite('objetDetected 2' +
                str(datetime.datetime.now()) + '.png', imageContures)
    if detected:
        #cv2.putText(imageRectangle, "object detected", org=( 50, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.FILLED)
        cv2.imwrite('objetDetected.png', imageRectangle)
        fbClient.uploadNewCollectionEvent('objetDetected.png', 0.0, 'UNKNOWN')
        print("detected")
    else:
        print("no detection")

    return detected

    # cv2.imshow('detection', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


fbClient = firebaseClient.firebaseClient("4HD4nUV5Kkkkt4AUxmSC")
main()
