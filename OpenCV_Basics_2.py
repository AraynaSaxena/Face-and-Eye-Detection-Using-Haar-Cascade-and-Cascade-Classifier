# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 19:35:48 2023

@author: AMIT
"""

# Edge Detection using OpenCV

import cv2

# Read Image
img = cv2.imread('E:/OpenCV/parrot.jpg')

# Convert BGR image to Grayscale
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame1', img)

# Canny(image, threshold1, threshold2)
# Computing Edge Gradient with canny thresholds
# The edge Gradients that are greater than threshold2 -> considered as edges
# The edge Gradients that are below than threshold1 -> considered not as an edges
edges_low = cv2.Canny(img_g, 60, 150)
cv2.imshow('Edge Detection', edges_low)

edges_high = cv2.Canny(img_g, 140, 230)
cv2.imshow('Edge Detection', edges_high)

# press any to close of frame
cv2.waitKey(0)
# Close all windows
cv2.destroyAllWindows()