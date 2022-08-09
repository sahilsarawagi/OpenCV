import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
print(img)
# img[:]=255,0,0  # As it follows BGR (img will have blue color) , if we want to color only specific region in image then we have to use img[30:40,89:55] means we have to give height and width region 
cv2.line(img,(0,0),(100,100),(0,255,0),2) #it has parameter (point 1 for line,point 2 for line, color , thickness)  
cv2.rectangle(img,(359,100),(450,200),(0,0,255),cv2.FILLED)  #it has parameter (point 1 for line,point 2 for line, color , thickness)
cv2.circle(img,(150,400),50,(255,56,55),3) # (img, center, radius,color, thickness)
cv2.putText(img,"Draw Shape",(75,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)
cv2.imshow("Image",img)
cv2.waitKey(0)