import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg',)
cv.imshow('Cat', img)

# Translation


def translate(image, x, y):
    # the function gets an image to shift,
    # and x,y for the number of pixels that will be shifted in x and y axes.
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])  # [1] is the width and [0] is the height.
    return cv.warpAffine(img, transmat, dimensions,)


# (-x) --> Left
# (-y) --> up
# (x) --> right
# (y) --> down
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation


def rotate(image, angle, rot_point=None):
    (height, width) = image.shape[:2]
    if rot_point is None:
        rot_point = (width//2, height//2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(image, rot_mat, dimensions,)


rotated = rotate(img, 45, )
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45,)
cv.imshow('Rotated_rotated', rotated_rotated)

rotated_img = rotate(img, 90,)
cv.imshow('Rotated_img', rotated_img)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip_v = cv.flip(img, 0)  # vertically flip
cv.imshow("Flip_v", flip_v)
flip_h = cv.flip(img, 1)  # horizontally flip
cv.imshow('Flip_h', flip_h)
flip_both = cv.flip(img, -1)  # both vertically and horizontally
cv.imshow('Flip_b', flip_both)

# Cropping
cropped = img[50:100, 70:120]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
