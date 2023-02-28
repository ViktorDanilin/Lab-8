# 4th variant
import cv2 as cv


def nothing(x):
    pass


img = cv.imread('images/variant-4.jpeg')  # default image
# img = cv.imread('img.png') # image for testing blue filter
# img = cv.resize(img, (300, 350))
blue, green, red = cv.split(img) # only blue color
while True:
    cv.imshow('blue', blue)  # show blue image
    cv.imshow('image', img)  # show image without filter
    mask = cv.inRange(img, (0, 0, 0), (255, 100, 0))
    # filter params: frame, minb, ming, minr, maxb, maxg, maxr
    result = cv.bitwise_and(img, img, mask=mask)  # show filtered image
    cv.imshow("result", result)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
