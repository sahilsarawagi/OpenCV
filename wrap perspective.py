import cv2
import numpy as np

img = cv2.imread("cards.jpg")
width,height=250,350    # this is the width and height we have defined in the size we want to see output image 
pts1=np.float32([[95,185],[211,67],[411,320],[499,167]])    # this is pts1 (it is the corner of card which we want to see as wrap perspective)
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]]) #this is pts2 (this is the size for output image)
matrix=cv2.getPerspectiveTransform(pts1,pts2)               # this will transform pts1 to pts2
imgOutput=cv2.warpPerspective(img,matrix,(width,height))     # 

print([[95,185],[211,67],[411,320],[499,167]]) 
print([[0,0],[width,0],[0,height],[width,height]])
for a in range(0,4):
    cv2.circle(img,(int(pts1[a][0]),int(pts1[a][1])),5,(0,0,255),cv2.FILLED)  # this is the marking of circle at the corner point of img

cv2.imshow("original",img)
cv2.imshow("output",imgOutput)

cv2.waitKey(0)