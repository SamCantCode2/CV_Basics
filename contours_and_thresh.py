import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Samhruth\Pictures\Saved Pictures\ForEncry.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(img, 150, 160)
cv.imshow('Sudo', img)
cv.imshow('Edges', canny)

conts, hier = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #below 125 is black, above that is white
cv.imshow('Threshold', thresh)

cv.waitKey(0)