import cv2 as cv

img = cv.imread('cat.jpg',)
cv.imshow('Cat', img)


# Converting the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
cv.imshow('Gray', gray)


# blur the image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# Edge cascade

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[100:200, 0:400]  # The first parameter is columns, and the second parameter is rows.
cv.imshow('Cropped', cropped)

cv.waitKey(0)
