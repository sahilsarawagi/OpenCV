import cv2

#Resizeing of the image
img=cv2.imread("temple.jpg")
print(img.shape)  # here 639 is height, 959 is width and 3 means channel which is  BGR
width,height=180,170
imgResize=cv2.resize(img,(width,height))
print(imgResize.shape)

cv2.imshow("image",img)
cv2.imshow("imageResize",imgResize)



# Croping of the image
imgCroped=img[0:450,0:959]
cv2.imshow("imgCroped",imgCroped)

#
imgCropResize=cv2.resize(imgCroped,(img.shape[1],img.shape[0]))
cv2.imshow("imgCropedResize",imgCropResize)
cv2.waitKey(0)