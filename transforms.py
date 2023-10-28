import cv2 as cv
import numpy as np

img = cv.imread(r'')
cv.imshow('Sudo', img)

def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)

'''
-x => left
x => right
-y => up
y => down
'''

timg = translate(img, -100, 100)
cv.imshow('Translated', timg)

def rotate(img, angle, point=None):
    (height, width) = img.shape[:2]
    if point is None:
        point = (width//2, height//2)
    rotmat = cv.getRotationMatrix2D(point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotmat, dimensions)
'''
positive => counter clockwise
negative => clockwise
'''

rimg = rotate(img, 90)
cv.imshow('Rotated', rimg)

'''
0 => vertical
1 => horizontally
-1 => both
'''

resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resize)

flipped = cv.flip(img, -1)
cv.imshow('FLipped', flipped)
cv.waitKey(0)
