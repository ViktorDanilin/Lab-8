import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:

    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # cv.imshow("hsv", hsv)
    mask = cv.inRange(hsv, (0, 0, 20), (255, 255, 166))
    result = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow("result", mask)

    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    cv.drawContours(frame, contours, -1, (0, 0, 255), 3, cv.LINE_AA, hierarchy, 2)
    cv.imshow('contours', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()