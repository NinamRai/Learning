
import cv2 as cv
from caer.globals import INTER_AREA


def ninam(frame,scale_va5lue=0.2):
    width = int (frame.shape[1]*scale_va5lue)
    height = int (frame.shape[0]*scale_va5lue)
    dimension = (width, height)

    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('./Videos/v1.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = ninam(frame)

    cv.imshow('1', frame)
    cv.imshow('2', frame_resized)
    if cv.waitKey(20) & 0xFF== ord('k'):
        break


capture.read()
cv.destroyAllWindows()