# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:42:47 2018

@author: Anuj Rohilla
"""
#importing the required modules
import cv2
import argparse
import imutils

#creating the command line argument
arg = argparse.ArgumentParser()
arg.add_argument("-i","--image",required = True, help = "Path of the image")
args = vars(arg.parse_args())

#loading the image
image = cv2.imread(args["image"])

#displaying the original image
cv2.imshow("Original Image", image)

#calculating the ratio of the fixed height to maintain the aspect ratio
r = 50.0/image.shape[0]

#calculating the new dimension
dim = (int(image.shape[1] * r), 50)

#resizing the image to new dimension
resize = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)

#displaying the resized image
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)

#resizing the image using imutils
resize = imutils.resize(image, width = 100)

#displaying the resized image
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)