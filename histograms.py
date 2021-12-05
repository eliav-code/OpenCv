import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('people.jpg',)
cv.imshow('People', img)

gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
# cv.imshow('Gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8',)
mask = cv.circle(blank, [img.shape[1]//2 - 70, img.shape[0]//2], 100, 255, -1,)

masked = cv.bitwise_and(gray, gray, dst=None, mask=mask)
cv.imshow('Mask', masked)

# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256],)
# plt.figure()
# plt.title('Grayscale Histograms')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()


plt.figure()
plt.title('Color Histograms')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
# Color histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], masked, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()
cv.waitKey(0)
