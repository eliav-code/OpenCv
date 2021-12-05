import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg',)
cv.imshow('Cat', img)
blank = np.zeros(img.shape[:2], dtype='uint8')
b, g, r = cv.split(img,)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('Blue', blue)  # show blue distribution pixels on a grayscale image.
cv.imshow('Green', green)  # show green distribution pixels on a grayscale image.
cv.imshow('Red', red)  # show red distribution pixels on a grayscale image.

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged image', merged)
cv.waitKey(0)
