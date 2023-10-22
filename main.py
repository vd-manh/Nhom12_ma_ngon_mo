import random
import cv2


# Function to Keep track of all the faces present
def tracker(face_coordinates):
  track = 0
  # Looping through all the faces present in the image or frame
  for set in face_coordinates:
    # Assigning random values from 0 to 255 to form a different rbg mixture of coloured squares for each face
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r = random.randint(0, 255)
    [x, y, w, h] = face_coordinates[track]  # Assigning the face coordinates to x,y,w,h to be used in the function below
    cv2.rectangle(img, (x, y), (x + w, y + h), (b, g, r), 3)
    track += 1


trained_face_data = cv2.CascadeClassifier(
  cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # Assigining the trained face data to a variable

# Importing the image fam.jpg from the directory and assigning it to the varible img
img = cv2.imread('anh.jpg')

grayscale = cv2.cvtColor(img,
                         cv2.COLOR_BGR2GRAY)  # COnerts the coloured image to a gray scale to be easily decipherable by the program

face_coordinates = trained_face_data.detectMultiScale(
  grayscale)  # Asssigning the nested list of cordinates of the faces detected to a variable face_coordinates

tracker(face_coordinates)  # Calling the tracker function on face coordinates

cv2.imshow('Face Detector',
           img)  # Displays the image in a program called face detector with rectangles on the detected faces
cv2.waitKey()

print("Code Completed!")