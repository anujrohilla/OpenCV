# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:40:36 2018

@author: Anuj Rohilla
"""
import cv2
from skimage.feature import canny

img = cv2.imread("ellipse.jpg")

cv2.imshow("Original Image", img)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = canny(img_gray, sigma=2.0,
              low_threshold=0.55, high_threshold=0.8)

cv2.imshow("Edges", edges)

cv2.waitKey(0)