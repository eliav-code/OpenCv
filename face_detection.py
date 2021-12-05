import cv2 as cv

# img = cv.imread('people.jpg',)
# cv.imshow('People', img)

# Face detection in a live stream video by use of haar_cascade. To use in image just replace the frame with an image.
capture = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('Camera', gray)
    # cv.imshow('Video', frame)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    print(f'Number of faces found = {len(faces_rect)}')  # print the number of the faces who are recognized.
    for (x, y, w, h) in faces_rect:  # Draw the rectangle on the screen
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.imshow('Detected faces', frame)
    if cv.waitKey(20) & 0xFF == ord('e'):
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)
