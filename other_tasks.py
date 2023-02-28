import cv2
import dlib
import numpy as np

model_detector = dlib.simple_object_detector("tld.swm")
font = cv2.FONT_HERSHEY_COMPLEX
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    boxes = model_detector(frame)
    for box in boxes:
        (x, y, xb, yb) = [box.left(), box.top(), box.right(), box.bottom()]
        cv2.rectangle(frame, (x, y), (xb, yb), (0, 0, 225), 2)
        string = str(int(x+((xb-x)/2))) + " " + str(int(y+((yb-y)/2)))
        center = ((int(x+((xb-x)/2))), int(y+((yb-y)/2)))
        cv2.putText(frame, string, center, font, 0.5, (255, 0, 0))
        cv2.circle(frame, center, 5, (255, 0, 0), 2)
        if center[0] > 350:
            print('Правая половина')
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
