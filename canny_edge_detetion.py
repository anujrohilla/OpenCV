# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:21:18 2018

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

#blurring the image
blur = cv2.GaussianBlur(gray, (3,3), 0)

#applying the canny edge detection
canny = cv2.Canny(blur, 50, 150)

#stacking the images
imgs = np.hstack([blur, canny])

#displaying the images
cv2.imshow("Images",imgs)

cv2.waitKey(0)
