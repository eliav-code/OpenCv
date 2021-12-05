import os
import cv2 as cv
import numpy as np

# img = cv.imread()
# cv.imshow('Image', img)
# cv.waitKey(0)

DIR = r'C:\Users\eliav\OneDrive\שולחן העבודה\Python\Pictures for face recognize'

people = []

for i in os.listdir(DIR):
    people.append(i)

print(people)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        # save the path of each directory of person.
        label = people.index(person)  # save the index of each person.

        for image in os.listdir(path):  # pass all the images in the specific directory.
            img_path = os.path.join(path, image)

            img_array = cv.imread(img_path,)
            gray = cv.cvtColor(img_array, cv.COLOR_BGRA2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces_rect:  # Draw the rectangle on the screen
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training done --------------------------->')
features = np.array(features, dtype=object)
labels = np.array(labels)

# print(f'length of the features = {len(features)}')
# print(f'length of the labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
