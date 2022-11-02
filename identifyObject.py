import cv2
import time
import datetime
import numpy as np

# https://automaticaddison.com/how-to-detect-and-draw-contours-in-images-using-opencv/
# https://stackoverflow.com/questions/28013435/how-i-can-count-bounding-boxes-in-each-frame


def main():
    # 0 sets to video camera and 1 for webcam
    capture = cv2.VideoCapture(0)
    # image = cv2.imread('bottle.jpg')
    # need sleep time to connect to camera image
    time.sleep(10)
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
    imagegrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, imageBinary = cv2.threshold(
        imagegrey, 100, 255, cv2.THRESH_OTSU)

    # invert the image
    imageInverted = ~imageBinary

    # find the contures
    contours, hierarchy = cv2.findContours(
        imageInverted, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # draw contures on a copy of the image
    imageContures = image.copy()
    cv2.drawContours(imageContures, contours, -1, (0, 255, 0), 3, 32)

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        print(w)
        print(h)
        # if detected contures have above a certain width and hight then an object was detected.
        if w >= 20 and h >= 20:
            print("here 2")
            imageRectangle = image.copy()
            cv2.rectangle(imageRectangle, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(imageRectangle, "object detected", org=(
                50, 50), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.FILLED)
            cv2.imwrite('objetDetected 2' +
                        str(datetime.datetime.now()) + '.png', imageRectangle)

            return True
    return False
    # cv2.imshow('detection', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


main()
