import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, thickness=-1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise_and', bitwise_and)

# bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_or', bitwise_or)

# bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise_xor', bitwise_xor)

# bitwise NOT
bitwise_not_r = cv.bitwise_not(rectangle)
cv.imshow('Rectangle not', bitwise_not_r)

bitwise_not_c = cv.bitwise_not(circle)
cv.imshow('Circle not', bitwise_not_c)




cv.waitKey(0)
