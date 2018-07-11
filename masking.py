# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:22:15 2018

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

#creating the blank space in 2D of same shape as that of image
mask = np.zeros(image.shape[:2], dtype = "uint8")

#creating the mask
cv2.rectangle(mask, (110,110), (200,200), 255, -1)

#masking the image
masking = cv2.bitwise_and(image,image, mask = mask)

#displaying the image
cv2.imshow("Masked Image", masking)
cv2.waitKey(0)