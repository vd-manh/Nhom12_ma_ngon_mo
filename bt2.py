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

dimport numpy as np

A=np.array([["Sunny","Hot","High","Weak","No"],
            ["Sunny","Hot","High","Strong","No"],
            ["Overcast","Hot","High","Weak","Yes"],
            ["Rain","Mild","High","Weak","Yes"],
            ["Rain","Cool","Normal","Weak","Yes"],
            ["Rain","Cool","Normal","Strong","No"],
            ["Overcast","Cool","Normal","Strong","Yes"],
            ["Sunny","Mild","High","Weak","No"],
            ["Sunny","Cool","Normal","Weak","Yes"],
            ["Rain","Mild","Normal","Weak","Yes"],
            ["Sunny","Mild","Normal","Strong","Yes"],
            ["Overcast","Mild","High","Strong","Yes"]], dtype="object")

#nhap lieu
print("nhập dữ liệu test")
POutlook = input("Outlook: ");
while(POutlook!= "Sunny" and POutlook!= "Overcast" and POutlook!= "Rain"):
    POutlook = input("Outlook :");

PTemp = input('Temp: ')
while(PTemp!= "Hot" and PTemp!= "Mild" and PTemp!= "Cool"):
    PTemp = input('Temp: ')

PHum = input('Humidity: ')
while(PHum!= "High" and PHum!= "Normal"):
    PHum = input('HUmidity: ');

PWind = input('Wind: ')
while(PWind!= "Strong" and PWind!= "Weak"):
    PWind = input('Wind: ')

C=A.shape[0]
#tính tỉ lệ mẫu
print("tổng số mẫu=", C)
PYes=0
i=0
for i in range(C):
    if A[i][4]=="Yes":
        PYes = PYes+1
print("PYes= ", PYes, "tỉ lệ Yes= ",PYes/C)

PNo=0
i=0
for i in range(C):
    if A[i][4]=="No":
        PNo = PNo+1
print("PNo= ", PNo, "tỉ lệ No= ", PNo/C)

#tỉ lệ input1
POutlookbyYes=0
POutlookbyNo=0
i=0
for i in range(C):
    if A[i][4]=="Yes" and A[i][0]==POutlook:
        POutlookbyYes = POutlookbyYes+1;
    if A[i][4] == "No" and A[i][0] == POutlook:
         POutlookbyNo = POutlookbyNo+1;
print("Poutlook_by_Yes= ", POutlookbyYes/PYes)
print("Poutlook_by_No= ", POutlookbyNo/PNo)

#tỉ lệ input2
PTempbyYes=0
PTempbyNo=0
i=0
for i in range(C):
    if A[i][4]=="Yes" and A[i][1]==PTemp:
        PTempbyYes = PTempbyYes+1;
    if A[i][4] == "No" and A[i][1] == PTemp:
         PTempbyNo = PTempbyNo+1;
print("Ptemp_by_Yes= ", PTempbyYes/PYes)
print("Ptemp_by_No= ", PTempbyNo/PNo)

#tỉ lệ input3
PHumbyYes=0
PHumbyNo=0
i=0
for i in range(C):
    if A[i][4]=="Yes" and A[i][2]==PHum:
        PHumbyYes = PHumbyYes+1;
    if A[i][4] == "No" and A[i][2] == PHum:
         PHumbyNo = PHumbyNo+1;
print("PHumidity_by_Yes= ",  PHumbyYes/PYes)
print("PHumidity_by_No= ", PHumbyNo/PNo)
#tỉ lệ input4
PWindbyYes=0
PWindbyNo=0
i=0
for i in range(C):
    if A[i][4]=="Yes" and A[i][3]==PWind:
        PWindbyYes = PWindbyYes+1;
    if A[i][4] == "No" and A[i][3] == PWind:
         PWindbyNo = PWindbyNo+1;
print("PWind_by_Yes= ", PWindbyYes/PYes)
print("PWind_by_No= ", PWindbyNo/PNo)

Z1=(POutlookbyYes/PYes)*(PTempbyYes/PYes)*(PHumbyYes/PYes)*(PWindbyYes/PYes)
Z2=(POutlookbyNo/PNo)*(PTempbyNo/PNo)*(PHumbyNo/PNo)*(PWindbyNo/PNo)
print("Pz_by_Yes= ", Z1)
print("Pz_by_No= ", Z2)

#chuẩn hóa
ZYes=Z1/(Z1+Z2)
ZNo=Z2/(Z1+Z2)
print("Pz chuẩn hóa Yes= ", Z1/(Z1+Z2))
print("Pz chuẩn hóa No= ", Z2/(Z1+Z2))
#KL
if ZYes>ZNo:
    print("Có ra ngoài")
else:
    print("Không ra ngoài")

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
