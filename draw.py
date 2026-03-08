import cv2
import numpy as np
img = cv2.imread('photos/images.jpeg')
kernal = np.ones((3,3), np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0)
imgcanny = cv2.Canny(img, 100,100)
imgdilation = cv2.dilate(imgcanny,kernal, iterations=5)
imgerode = cv2.erode(imgdilation, kernal, iterations = 5)

cv2.imshow("gray image", imgGray)
cv2.imshow("g", imgBlur)
cv2.imshow("new", imgcanny)
cv2.imshow("thic", imgdilation)
cv2.imshow("erosion", imgerode)
cv2.waitKey(0)
