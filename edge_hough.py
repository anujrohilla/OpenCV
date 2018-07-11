# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:10:57 2018

@author: Anuj Rohilla
"""
import cv2
import argparse
import numpy as np

arg = argparse.ArgumentParser()
arg.add_argument("-i","--image", required = True, help = "Path of the image")
args = vars(arg.parse_args())

image = cv2.imread(args["image"])

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.bilateralFilter(image, 7, 41, 41)

canny = cv2.Canny(blur, 50, 150)

cv2.imshow("Canny",canny)

circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 2, 50)

output = np.copy(image) 

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    
    for (x, y, r) in circles:
        cv2.circle(output, (x,y), r, (255,0,0), 2)
        
        
cv2.imshow("Output", output)
cv2.waitKey(0)
