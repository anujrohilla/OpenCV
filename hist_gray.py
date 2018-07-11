# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:14:34 2018

@author: Anuj Rohilla
"""
#importing the required modules
import cv2
import argparse
from matplotlib import pyplot as plt

#creating the command line argument
arg = argparse.ArgumentParser()
arg.add_argument("-i","--image",required = True, help = "Path of the image")
args = vars(arg.parse_args())

#loading the image
image = cv2.imread(args["image"])

#converting the image from BGR to Gray
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#displaying the original gray image
cv2.imshow("Original Image", image_gray)

#calculating the histogram for grayscale image with no masking and 256 bins
hist = cv2.calcHist([image_gray], [0], None, [256],[0,256])

#plotting the histograph
plt.figure()
plt.title("Grayscale Image Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)