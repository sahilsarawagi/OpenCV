import imp
import cv2
from cv2 import imshow
import numpy as np    # we wanted to import matrix for kernel  for dilation and erosion
kernel= np.ones((5,5),np.uint8) # we need matrix of ones 5*5 which is unsigned int bits 8
print(kernel)


# Code for changing image color

# img =cv2.imread("temple.jpg",0)   # if we write 0 after path of the image, it will change color to grayscale
img =cv2.imread("temple.jpg")
# cv2.imshow("Temple",img)
imGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # or we can change the color to gray by this method
cv2.imshow("GrayScale",imGray)
cv2.imshow("Temple",img)



# Code for making image blur
 
imgBlur=cv2.GaussianBlur(img,(5,5),0)  # this (5,5) can be only odd no. and if you increase it bluriness of image will increase
cv2.imshow("ImageBlur",imgBlur)

# Code for image showing the edges of the main original image
imgCanny=cv2.Canny(img,100,100)  # these 100 and 100 are the threshold value if we increase it, it will increase the detection of edges
cv2.imshow("Canny",imgCanny)

# We can increase the size edge and decrease it, this is called dilation and Erosion

# Dilation
imgDilation= cv2.dilate(imgCanny,kernel,iterations=1)  # iterations means how many time it repeat itself means how many time it dilate the edge
cv2.imshow("Img Dilation",imgDilation)

# Erosion
imgErosion=cv2.erode(imgDilation,kernel,iterations=1)   # here we have used imgDilation for erosion bcs if we had used imgCanny imgage we might not see any thing bcs it would erode whole image
cv2.imshow("Img Erosion",imgErosion)
cv2.waitKey(0)

