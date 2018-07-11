# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:05:18 2018

@author: Anuj Rohilla
"""
#importing the required modules
import cv2 
import numpy as np
import argparse

#creating the commandline argument
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required = True, help = "Path of image")
args = vars(arg.parse_args())

#loading the image
image = cv2.imread(args["image"])

#displaying the original image
cv2.imshow("Original Image", image)

#OpenCV arithmetic
print("max of 255 : {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))

print("min of 0 : {}".format(cv2.subtract(np.uint8([20]), np.uint8([100]))))

#numpy arithmetic
print("max of 255 : {}".format(np.uint8([200]) + np.uint8([100])))

print("min of 0 : {}".format(np.uint8([20]) - np.uint8([100])))

#creating matrix of every element of 150 value of same shape as that of image
ad = np.ones(image.shape, dtype = "uint8") * 150

#adding the matrix created above with the image
add = cv2.add(image,ad)

#displaying  the added image
cv2.imshow("Addition", add)

#creating matrix of every element of 50 value of same shape as that of image
sb = np.ones(image.shape, dtype = "uint8") * 50

#subtracting the matrix created above with the image
sub = cv2.subtract(image, sb)

#displaying  the subtracted image
cv2.imshow("Subtract", sub)
cv2.waitKey(0)