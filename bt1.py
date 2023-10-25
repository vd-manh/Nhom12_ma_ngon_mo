import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

selected_filter = None

def apply_filter(filter_type):
    global img, selected_filter
    if img is not None:
        if filter_type == "sharpen_1":
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        elif filter_type == "sharpen_2":
            kernel = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
        elif filter_type == "sharpen_3":
            kernel = np.array([[-1, -1, -1, -1, -1],
                               [-1, 2, 2, 2, -1],
                               [-1, 2, 8, 2, -1],
                               [-1, 2, 2, 2, -1],
                               [-1, -1, -1, -1, -1]]) / 8.0
        else:
            kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

        output = cv2.filter2D(img, -1, kernel)
        cv2.imshow('Filtered Image', output)
        selected_filter = filter_type
def apply_effect(effect_type):
    global img, selected_filter
    if img is not None:
        if effect_type == "grayscale":
            output = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif effect_type == "invert_colors":
            output = cv2.bitwise_not(img)
        # Thêm hiệu ứng mới ở đây
        cv2.imshow('Filtered Image', output)
        selected_filter = effect_type

img = cv2.imread('anh1.JPG')
rows, cols = img.shape[:2]
kernel_identity = np.array([[0,0,0], [0,1,0], [0,0,0]])
kernel_3x3 = np.ones((3,3), np.float32) / 9.0
kernel_5x5 = np.ones((5,5), np.float32) / 25.0
cv2.imshow('Original', img)
output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('Identity filter', output)
output = cv2.filter2D(img, -5, kernel_3x3)
cv2.imshow('3x3 filter', output)
output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow('5x5 filter', output)
cv2.waitKey(0)