import cv2 as cv  # openCv expects to receive BGR image
# import matplotlib.pyplot as plt  # matplotlib expects to receive RGB image.

img = cv.imread('cat.jpg')
# cv.imshow('Cat', img)
#
# plt.imshow(img)
# plt.show()
#
# # BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('Gray', gray)

# BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# # BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)
#
# # BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# HSV to BGR
# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSV-->BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR', lab_bgr)

# plt.imshow(rgb)
# plt.show()
cv.waitKey(0)
