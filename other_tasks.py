# 4th variant
import cv2 as cv
import dlib
import numpy as np

# training model on ipynb

model_detector = dlib.simple_object_detector("tld.swm")  # use dlib model
font = cv.FONT_HERSHEY_COMPLEX
cap = cv.VideoCapture(0)
img = cv.imread('fly64.png')
img = cv.resize(img, (20, 20))
img_height, img_width, _ = img.shape  # size of img
while True:
    ret, frame = cap.read()

    boxes = model_detector(frame)
    for box in boxes:
        (x, y, xb, yb) = [box.left(), box.top(), box.right(), box.bottom()]
        cv.rectangle(frame, (x, y), (xb, yb), (0, 0, 225), 2)  # drawing contour
        center = ((int(x + ((xb - x) / 2))), int(y + ((yb - y) / 2)))  # cords of center
        x_center = center[0]
        y_center = center[1]
        string = str(x_center) + " " + str(y_center)
        cv.putText(frame, string, center, font, 0.5, (255, 0, 0))
        cv.circle(frame, center, 5, (255, 0, 0), 2)
        frame[y_center:y_center + img_height, x_center:x_center + img_width] = img  # add img to center of frame
        if x_center > 350:  # condition for right side frame
            print('Правая половина')
    cv.imshow("frame", frame)  # show frame with contour and cord of center

    if cv.waitKey(1) == ord("q"):

        break

cap.release()
cv.destroyAllWindows()
