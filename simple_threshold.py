# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 16:58:38 2018

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
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", image)

image = cv2.bilateralFilter(image, 9, 51, 51)
#image = cv2.GaussianBlur(image, (5,5), 0)

(T, thresh) = cv2.threshold(image, 58, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Threshold", thresh)

(T, thresh_inv) = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Binary Threshold Inverse", thresh_inv)

cv2.imshow("AND", cv2.bitwise_and(image, thresh_inv))
cv2.waitKey(0)