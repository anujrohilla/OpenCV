# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 16:27:50 2018

@author: Anuj Rohilla
"""
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

#Bilateral Blur
blured = cv2.bilateralFilter(image, 11, 51, 51)

#Displaying Bilateral blurred image
cv2.imshow("Bilateral Blur", blured)

(T, thresh) = cv2.threshold(blured, 61, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)