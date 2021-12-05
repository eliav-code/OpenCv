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



cv.waitKey(0)
