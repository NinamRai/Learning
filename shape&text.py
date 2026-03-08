import cv2
import numpy as np

img = (np.ones((500,500,3),np.uint8))
img1 = (np.ones((500,500,3),np.uint8))
# img[:]=128,222,138
cv2.line(img,(20,20,),(300,300),(123,255,123),2)
cv2.rectangle(img1,(20,200),(250,350),(250,220,100),2)
cv2.circle(img1,(135,275),30,(255,0,255),2)
cv2.putText(img1,"LADO KHA MACHIKNEY", (50,275),cv2.FONT_HERSHEY_SIMPLEX,1,(255,150,150),1)

cv2.imshow('black',img)
cv2.imshow('white', img1)
# print(img)
cv2.waitKey(0)