import cv2
import cv2 as cv


# img = cv.imread('photos/images.jpeg')
# cv.imshow('anime', img)

capture = cv2.VideoCapture('Videos/v1.mp4')

while True:
    isTrue, frame = capture.read()

    cv2.imshow('v', frame)
    if cv.waitKey(33) & 0xFF ==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()


