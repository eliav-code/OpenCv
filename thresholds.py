import cv2 as cv

img = cv.imread('people.jpg',)
cv.imshow('People', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY, )
cv.imshow('Simple threshold', thresh)

threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV, )
cv.imshow('Simple threshold inverse', thresh_inverse)

# Adaptive thresholding --> give the computer to choose the optimal thresholding value to be written.
adaptive_thresh_m = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 5,)
cv.imshow('Adaptive thresholding', adaptive_thresh_m)

# adaptive_thresh_g = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 5,)
# cv.imshow('Adaptive thresholding', adaptive_thresh_g)

cv.waitKey(0)
