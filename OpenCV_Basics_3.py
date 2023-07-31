# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 19:56:13 2023

@author: AMIT
"""
# Smoothening of Images - Apply Blur
import cv2
import numpy as np

img = cv2.imread('E:/OpenCV/child.jpg')
# kernel matrix used for smoothening of images - (3,3),(5,5),(7,7),(9,9)
kernel = np.ones((7,7), np.float32) / 49
print(kernel)

# Filter 2D
smoothed = cv2.filter2D(img, -1, kernel)

# Gaussian Blur
# kernel shape - (3,3),(5,5),(7,7),(9,9)
# sigmaX = std. deviation 
g_blur = cv2.GaussianBlur(img, (5,5), 1)

# Median Blur
m_blur = cv2.medianBlur(img, 9)

# Average Blur
avg_blur = cv2.blur(img, (7,7))

cv2.imshow('Image', img)
cv2.imshow('blur', smoothed)
cv2.imshow('g_blur', g_blur)
cv2.imshow('avg_blur', avg_blur)
cv2.imshow('m_blur', m_blur)

# press any to close of frame
cv2.waitKey(0)
# Close all windows
cv2.destroyAllWindows()


