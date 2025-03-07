import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    min_gray  = np.array([84,40,55])
    max_gray  = np.array([117,255,255])
    mask = cv.inRange(hsv,min_gray,max_gray)

    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()