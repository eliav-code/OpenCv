import cv2 as cv

img = cv.imread('cat.jpg',)
cv.imshow('Cat', img)

# Average
average = cv.blur(img, (7, 7))
cv.imshow('Average', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian blur', gauss)

# Median blur
median = cv.medianBlur(img, 7, )
cv.imshow('Median blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25,)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)
