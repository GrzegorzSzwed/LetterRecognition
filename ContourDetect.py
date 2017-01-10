__author__= 'Grzegorz Szwed'

import numpy as np
from transform import four_point_transform
from transform import order_points
import imutils
from skimage.filters import threshold_adaptive
import argparse
import cv2


def FindAllContours(arg):
    #cv2.imshow("With all contours", argument)
    nazwa = "Test3/obiekt"
    size = 40, 40
    normal = cv2.cvtColor(arg, cv2.COLOR_GRAY2BGR)
    __, contours, hierarchy = cv2.findContours(arg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    i=0
    while i < len(contours):
        cnt = contours[i]
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.2 * peri, True)
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 12 and h >12: #do not include the hiss
            cv2.rectangle(normal, (x, y), (x + w, y + h), (255, 0, 0), 1)
            nowanazwa = nazwa + str(i) + ".jpg"
            cropped = arg[y:(y + h), x:(x + w)]
            dim = (28, 28)
            resized = cv2.resize(cropped, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow(nowanazwa, resized)
            key = cv2.waitKey(0)

            if key == ord('s'):  # wait for 's' key to save and exit
                cv2.imwrite(nowanazwa, resized)
                cv2.destroyWindow(nowanazwa)
            elif key == ord('p'):
                cv2.destroyWindow(nowanazwa)
        i+=1
    cv2.imshow("kontury", arg)

def FindTheField(argument):
    image = cv2.imread(argument)
    orig = image.copy()

    ratio = image.shape[0] / 500.0
    image = imutils.resize(image, height=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)  # noise reduction
    edged = cv2.Canny(gray, 75, 200)  # canny filter '1986

    __, contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    # loop over the contours
    for c in contours:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break


    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", image)
    # apply the four point transform to obtain a top-down
    # view of the original image
    warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

    # convert the warped image to grayscale, then threshold it
    # to give it that 'black and white' paper effect
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    warped = threshold_adaptive(warped, 251, offset=10)
    warped = warped.astype("uint8") * 255

    # show the scanned images
    cv2.imshow("Scanned", imutils.resize(warped, height=650))

    FindAllContours(warped)


FindTheField("Test3/piwo.jpg")

klucz = cv2.waitKey(0)
if klucz == 27:
    cv2.destroyAllWindows()
