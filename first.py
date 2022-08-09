from random import sample
import cv2   # cv stand for computer vision

# for IMAGE 

# img=cv2.imread("temple.jpg")   #this read the image

# cv2.imshow("Temple",img) #this will show the img

# cv2.waitKey(5000)   #now it will show the image for 5000ms=5sec , if we want that it shows the image for infinity time, then put the 0 at the place of 5000


# for VIDEO

framewidth= 64
frameheight= 36
cap = cv2.VideoCapture("sample.mp4")
# cap = cv2.VideoCapture(0)   # this will open up the web cam  (for pc value for the web cam is 0)
# cap.set(3,framewidth)
# cap.set(4,frameheight)


while True:
    sucess,img= cap.read()   # it will read from cap and then store in the img
    img=cv2.resize(img,(framewidth,frameheight))
    cv2.imshow("Video",img)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break