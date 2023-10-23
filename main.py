import random
import cv2

def draw_face_rectangles(image, face_coordinates):
    for (x, y, w, h) in face_coordinates:
        # Generate a random RGB color for the rectangle
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv.rectangle(image, (x, y), (x + w, y + h), color, 3)

trained_face_and_eye_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')  # Sử dụng tệp phân loại kết hợp
img = cv2.imread('anh.jpg')
if img is None :
    print("Không tìm thấy file ảnh")


grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_and_eye_coordinates = trained_face_and_eye_data.detectMultiScale(grayscale)  # Sử dụng tệp phân loại kết hợp

draw_face_rectangles(img,face_and_eye_coordinates)

width, height = 800, 600
img = cv2.resize(img, (width, height))

cv2.imshow('Face and Eye Detector', img)
cv2.waitKey()
cv.destroyAllWindows()

print("Code Completed!")
