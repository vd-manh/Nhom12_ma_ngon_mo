import random
import cv2

def tracker(face_coordinates):
    track = 0
    for set in face_coordinates:
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        r = random.randint(0, 255)
        [x, y, w, h] = face_coordinates[track]
        cv2.rectangle(img, (x, y), (x + w, y + h), (b, g, r), 3)
        track += 1

trained_face_and_eye_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')  # Sử dụng tệp phân loại kết hợp
img = cv2.imread('anh.jpg')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_and_eye_coordinates = trained_face_and_eye_data.detectMultiScale(grayscale)  # Sử dụng tệp phân loại kết hợp

tracker(face_and_eye_coordinates)

width, height = 1000, 800
img = cv2.resize(img, (width, height))

cv2.imshow('Face and Eye Detector', img)
cv2.waitKey()

print("Code Completed!")