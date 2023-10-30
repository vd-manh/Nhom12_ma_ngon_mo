import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

selected_filter = None
img = None  # Initialize img as None

def apply_filter(filter_type):
    global selected_filter
    if img is not None:
        if filter_type == "sharpen_1":
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1])
        elif filter_type == "sharpen_2":
            kernel = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1])
        elif filter_type == "sharpen_3":
            kernel = np.array([[-1, -1, -1, -1, -1],
                               [-1, 2, 2, 2, -1],
                               [-1, 2, 8, 2, -1],
                               [-1, 2, 2, 2, -1],
                               [-1, -1, -1, -1, -1]]) / 8.0
        else:
            kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0])

        output = cv2.filter2D(img, -1, kernel)
        cv2.imshow('Filtered Image', output)
        selected_filter = filter_type  # Update the selected filter

def apply_effect(effect_type):
    global selected_filter
    if img is not None:
        if effect_type == "grayscale":
            output = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif effect_type == "invert_colors":
            output = cv2.bitwise_not(img)
        cv2.imshow('Filtered Image', output)
        selected_filter = effect_type  # Update the selected effect

def open_file():
    global img
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        cv2.imshow('Original', img)

# Create a tkinter window
root = tk.Tk()
root.title("Image Filters")

# Add buttons to apply filters
sharpen_1_button = tk.Button(root, text="Sharpen 1", command=lambda: apply_filter("sharpen_1"))
sharpen_2_button = tk.Button(root, text="Sharpen 2", command=lambda: apply_filter("sharpen_2"))
sharpen_3_button = tk.Button(root, text="Sharpen 3", command=lambda: apply_filter("sharpen_3"))
grayscale_button = tk.Button(root, text="Grayscale", command=lambda: apply_effect("grayscale"))
invert_colors_button = tk.Button(root, text="Invert Colors", command=lambda: apply_effect("invert_colors"))
open_file_button = tk.Button(root, text="Open Image", command=open_file)

sharpen_1_button.pack()
sharpen_2_button.pack()
sharpen_3_button.pack()
grayscale_button.pack()
invert_colors_button.pack()
open_file_button.pack()

root.mainloop()  # Start the tkinter main loop
