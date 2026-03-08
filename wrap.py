import cv2
import numpy as np

img = cv2.imread('photos/cards.jpg')

width,height=250,350
pts1=np.float32([[97,189],[293,186],[97,486],[293,486]])
pts2 = np.float32([[25,25],[width,25],[25,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput= cv2.warpPerspective(img,matrix,(width,height))   

cv2.imshow('image',img)
cv2.imshow("img1",imgOutput)
cv2.waitKey(0)