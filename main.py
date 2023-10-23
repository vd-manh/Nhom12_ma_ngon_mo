import random
import cv2

def draw_face_rectangles(image, face_coordinates):
    for (x, y, w, h) in face_coordinates:
        # Generate a random RGB color for the rectangle
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv.rectangle(image, (x, y), (x + w, y + h), color, 3)
#NHAN DIEN KHUON MAT TU VID
# Tạo đối tượng VideoCapture để lấy video từ webcam (hoặc camera mạng)
cap = cv2.VideoCapture(0)  # Số 0 thường tương ứng với webcam máy tính
# Tạo bộ phân loại khuôn mặt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    # Đọc khung hình từ video
    ret, frame = cap.read()

    # Chuyển ảnh thành ảnh xám (cải thiện hiệu suất)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Xác định khuôn mặt trong khung hình
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Vẽ hình chữ nhật xung quanh khuôn mặt đã xác định
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Hiển thị video với các khuôn mặt đã xác định
    cv2.imshow('Face Detection', frame)

    # Thoát vòng lặp khi nhấn phím bất kì
    key = cv2.waitKey(1)
    if key != -1:
        running = False

# Giải phóng tài nguyên và đóng cửa sổ video
cap.release()
cv2.destroyAllWindows()
########
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
