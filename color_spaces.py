# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:16:50 2018

@author: Anuj Rohilla
"""
#importing the required modules
import cv2
import argparse

#creating the command line argument
arg = argparse.ArgumentParser()
arg.add_argument("-i","--image",required = True, help = "Path of the image")
args = vars(arg.parse_args())

#loading the image
image = cv2.imread(args["image"])

#displaying the original image
cv2.imshow("Original Image", image)

#converting BGR to Gray color space
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#displaying the gray color space image
cv2.imshow("Gray", gray)

#converting BGR to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#displaying the HSV color space image
cv2.imshow("HSV", hsv)

#converting BGR to L*A*B* color space
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

#displaying the L*A*B* color space image
cv2.imshow("L*A*B*",lab)
cv2.waitKey(0)
