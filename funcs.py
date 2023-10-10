import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\Samhruth\Pictures\Saved Pictures\ForEncry.jpeg')
cv.imshow('Sudo', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) #increase kernel size to increase blur
cv.imshow('Blurred', blur)

#Edge cascade using Canny
canny = cv.Canny(img, 100, 200)
cv.imshow('Canny', canny)

#dilation to thicken the edges
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow('Dilated', dilated)

#eroding to thin the dilated edges
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow('Eroded', eroded)

resize = cv.resize(img, (500, 500)) 
'''
no arg => without taking aspect ratio
interpolation arg:
cv.INTER_AREA => Scale image down
cv.INTER_LINEAR/INTER_CUBIC => Scale image up
Cubic is slow but high quality
'''
cv.imshow('Resized', resize)

cropped = img[50:350, 100:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)