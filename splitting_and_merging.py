# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:43:49 2018

@author: Anuj Rohilla
"""
#importing the required modules
import cv2
import argparse
import numpy as np

#creating the command line argument
arg = argparse.ArgumentParser()
arg.add_argument("-i","--image",required = True, help = "Path of the image")
args = vars(arg.parse_args())

#loading the image
image = cv2.imread(args["image"])

#displaying the original image
cv2.imshow("Original Image", image)

#Splitting the image into it's components
(B, G, R) = cv2.split(image)

#displaying the Blue components
cv2.imshow("Blue", B)

#displaying the Green components
cv2.imshow("Green", G)

#displaying the Red components
cv2.imshow("Red", R)

#Merging the components
merged = cv2.merge([B,G,R])

#displaying the merged image
cv2.imshow("Merged Image", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeroes = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Only Red", cv2.merge([zeroes,zeroes,R]))
cv2.imshow("Only Green", cv2.merge([zeroes,G,zeroes]))
cv2.imshow("Only Blue", cv2.merge([B,zeroes,zeroes]))
cv2.waitKey(0)