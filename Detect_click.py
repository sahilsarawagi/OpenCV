import cv2
from cv2 import imread
from cv2 import circle
import numpy as np
circles=np.zeros((4,2),np.int32)
counter=0
def mousePoints(event,x,y,flags,param):
    global counter
    if event==cv2.EVENT_LBUTTONDOWN:
        circles[counter]=x,y
        counter=counter+1
        print(circles)

img=cv2.imread('cards.jpg')
while True:
    if counter==4:
        width,height=250,350   
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])   
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]]) 
        matrix=cv2.getPerspectiveTransform(pts1,pts2)               
        imgOutput=cv2.warpPerspective(img,matrix,(width,height))     
        cv2.imshow("output",imgOutput)
        
    
    for a in range(0,4):
        cv2.circle(img,(int(circles[a][0]),int(circles[a][1])),3,(0,0,255),cv2.FILLED)  





    cv2.imshow("oRIginal",img)
    cv2.setMouseCallback("oRIginal",mousePoints)
    cv2.waitKey(1)


