# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 19:12:56 2023

@author: AMIT
"""

import cv2

img = cv2.imread('E:/OpenCV/parrot.jpg')
# opencv - reads images in BGR Format
print(img)

# convert BGR image to Grayscale
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert BGR to HSV (hue saturation value)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('frame1', img)
cv2.imshow('frame2', img_g)
cv2.imshow('frame3', img_hsv)

# press any to close of frame
cv2.waitKey(0)
# Close all windows
cv2.destroyAllWindows()
