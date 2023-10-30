import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

filters = {
    "sharpen_1": np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]),
    "sharpen_2": np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]]),
    "sharpen_3": np.array([[-1, -1, -1, -1, -1],
                           [-1, 2, 2, 2, -1],
                           [-1, 2, 8, 2, -1],
                           [-1, 2, 2, 2, -1],
                           [-1, -1, -1, -1, -1]]) / 8.0,
}

selected_filters = []

def apply_filters():
    global img
    if img is not None:
        output = img.copy()
        for filter_name in selected_filters:
            kernel = filters.get(filter_name)
            if kernel is not None:
                output = cv2.filter2D(output, -1, kernel)
        cv2.imshow('Filtered Image', output)

def save_image():
    global img
    if img is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if file_path:
            cv2.imwrite(file_path, img)
            print("Image saved successfully.")

def open_image():
    global img
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tif")])
    if file_path:
        img = cv2.imread(file_path)
        if img is not None:
            cv2.imshow('Original', img)
    root.after(1, update)

def toggle_filter(filter_name):
    if filter_name in selected_filters:
        selected_filters.remove(filter_name)
    else:
        selected_filters.append(filter_name)

def update():
    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()
    root.after(1, update)

root = tk.Tk()
root.title("Image Filters")

cv2.namedWindow('Original')
cv2.namedWindow('Filtered Image')

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

sharpen_1_button = tk.Button(root, text="Sharpen 1", command=lambda: toggle_filter("sharpen_1"))
sharpen_1_button.pack()

sharpen_2_button = tk.Button(root, text="Sharpen 2", command=lambda: toggle_filter("sharpen_2"))
sharpen_2_button.pack()

sharpen_3_button = tk.Button(root, text="Sharpen 3", command=lambda: toggle_filter("sharpen_3"))
sharpen_3_button.pack()

apply_filters_button = tk.Button(root, text="Apply Filters", command=apply_filters)
apply_filters_button.pack()

save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack()

img = None
update()

root.mainloop()
