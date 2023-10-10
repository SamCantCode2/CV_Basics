import cv2 as cv
import numpy as np

#images
blank = np.zeros((500, 500, 3), dtype = 'uint8')
green = np.zeros((500, 500, 3), dtype = 'uint8')
green[100:200, 300:400] = 0, 255, 0
cv.imshow('Green', green)
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2) #can also use blank.shape[0], blank.shape[1]
cv.rectangle(blank, (250, 0), (500, 500), (255, 0, 0), thickness=cv.FILLED) #can also use thickness = -1
cv.circle(blank, (125, 375), 115, (0, 0, 255), thickness=10)
cv.line(blank, (0, 0), (blank.shape[1], blank.shape[0]), (255, 255, 255), thickness=5)
cv.putText(blank, "Hello World", (100, 100), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(255, 0, 255), thickness=1)
cv.imshow('Rectangle', blank)
cv.waitKey(0)