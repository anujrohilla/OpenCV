# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:35:25 2018

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

#cropping the image
crop = image[10:100,15:100]

#displaying the cropped image
cv2.imshow("Cropped Image", crop)
cv2.waitKey(0)