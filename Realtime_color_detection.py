from unittest import result
import cv2
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
import numpy as np

# frameWidth= 640
# frameHeight= 360

cap=cv2.VideoCapture(0)
# cap(3,frameWidth)
# cap(4,frameHeight)
def empty(a):
    pass
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE MIN","HSV",0,179,empty)
cv2.createTrackbar("HUE MAX","HSV",179,179,empty)
cv2.createTrackbar("SAT MIN","HSV",0,255,empty)
cv2.createTrackbar("SAT MAX","HSV",255,255,empty)
cv2.createTrackbar("VALUE MIN","HSV",0,255,empty)
cv2.createTrackbar("VALUE MAX","HSV",255,255,empty)


while True:
    _,img= cap.read()
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("HUE MIN","HSV")
    h_max=cv2.getTrackbarPos("HUE MAX","HSV")
    s_min=cv2.getTrackbarPos("SAT MIN","HSV")
    s_max=cv2.getTrackbarPos("SAT MAX","HSV")
    v_min=cv2.getTrackbarPos("VALUE MIN","HSV")
    v_max=cv2.getTrackbarPos("VALUE MAX","HSV")
    print(h_min)
    lower= np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imghsv,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    h_stack=np.stack([img,result])

    cv2.imshow("Original", img)
    # cv2.imshow("HSV COLOR SPACE", imghsv)
    # cv2.imshow('Mask',mask)
    # cv2.imshow("Result",result)
    cv2.imshow("Horizontal Stacking",h_stack)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()