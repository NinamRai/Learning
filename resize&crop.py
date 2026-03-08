import cv2
import numpy as np

img = cv2.imread('photos/images.jpeg')
print(img.shape)
imgResize= cv2.resize(img,(500,500))
imcropped = imgResize[0:200,0:200]
cv2.imshow("Image",img)
cv2.imshow("resize",imgResize)
cv2.imshow("crop",imcropped)
cv2.waitKey(0)
