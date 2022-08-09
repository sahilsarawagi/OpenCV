import imp
from tkinter import HORIZONTAL
import cv2
from cv2 import imshow
import numpy as np    
kernel= np.ones((5,5),np.uint8) 
print(kernel)

img=cv2.imread("temple.jpg")
imGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
imgBlur=cv2.GaussianBlur(img,(5,5),0)  
imgCanny=cv2.Canny(img,100,100)  
imgDilation= cv2.dilate(imgCanny,kernel,iterations=1)  
imgErosion=cv2.erode(imgDilation,kernel,iterations=1)   

img=cv2.resize(img,(0,0),None,0.5,0.5)
imGray=cv2.resize(imGray,(0,0),None,0.5,0.5)
imgBlur=cv2.resize(imgBlur,(0,0),None,0.5,0.5)
imgCanny=cv2.resize(imgCanny,(0,0),None,0.5,0.5)
imgDilation=cv2.resize(imgDilation,(0,0),None,0.5,0.5)
imgErosion=cv2.resize(imgErosion,(0,0),None,0.5,0.5)

imGray=cv2.cvtColor(imGray,cv2.COLOR_GRAY2BGR)
imgBlur=cv2.cvtColor(imgBlur,cv2.COLOR_GRAY2BGR)
imgCanny=cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
imgDilation=cv2.cvtColor(imgDilation,cv2.COLOR_GRAY2BGR)
imgErosion=cv2.cvtColor(imgErosion,cv2.COLOR_GRAY2BGR)


hor=np.hstack((imgCanny,imgDilation,imgErosion))
hor2=np.hstack((img,imgCanny,imgBlur))
ver=np.hstack(hor,hor2)
cv2.imshow('horizontal',ver)
cv2.waitKey(0)




 






