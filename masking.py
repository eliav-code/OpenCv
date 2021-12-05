import cv2 as cv
import numpy as np
# Pay attention that the mask have to be the same size or less of the original image.

img = cv.imread('people.jpg',)
cv.imshow('People', img)

blank = np.zeros(img.shape[:2], dtype='uint8',)
cv.imshow('Blank image', blank)

# mask_c = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask_c', mask_c)
#
# mask_r = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2),
# (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
# cv.imshow('Mask_r', mask_r)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, thickness=-1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
weird_shape = cv.bitwise_and(rectangle, circle)
cv.imshow('Weird Shape', weird_shape)

masked_image = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Masked image', masked_image)
cv.waitKey(0)
