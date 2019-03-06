import cv2
import numpy as np
import sys
import pytesseract


img = cv2.imread('bookpage.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Gaussian
threshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
# Clahe
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(gray)
# Gamma
new_image = np.zeros(img.shape, img.dtype)
alpha = 1.5 # Simple contrast control
beta = 45   # Brightness control
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            new_image[y,x,c] = np.clip(alpha*img[y,x,c] + beta, 0, 255)
cl1_str=pytesseract.image_to_string(cl1)
threshold_str=pytesseract.image_to_string(threshold)
gamma_str=pytesseract.image_to_string(new_image)
c1=cl1_str.split()
t1=threshold_str.split()
g1=gamma_str.split()
L2=[cl1_str,threshold_str,gamma_str]
L=[c1,t1,g1]
# cv2.imshow('Clahe',cl1)
# cv2.imshow('Threshold',threshold)
# cv2.imshow('Gamma',new_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
loc=0
for i in L:
    if loc < len(i):
        loc=L.index(i)
print(loc)
print(L2[loc])
# print(cl1_str)