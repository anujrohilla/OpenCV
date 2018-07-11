# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:50:45 2018

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

#converting the colored image into grascale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#calculating the laplacian gradiant in 64 bit float type
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

#converting the 64bit float type into uint8
laplacian = np.uint8(np.absolute(laplacian))

#stacking the images
images = np.hstack([gray, laplacian])

#displaying the laplacian edge detected image
cv2.imshow("Laplacian",images)

#Claculating the Sobel gradiant in X nad Y direction in 64 bit float type
sobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

#converting the 64bit float type into uint8
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#combining the gradiants of X and Y direction
sobelCombine = cv2.bitwise_or(sobelX, sobelY)

#displaying Sobel edge detected image
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combine", sobelCombine)

cv2.waitKey(0)