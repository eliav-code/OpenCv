import cv2 as cv

# images:

# img = cv.imread('cat.jpg',)

# cv.imshow('Cat',img)

# cv.waitKey(0)

# videos:

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('e'):
        break
capture.release()
cv.destroyAllWindows()
