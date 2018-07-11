# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:29:01 2018

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

#converting the image from BGR to Gray
image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#equalizing the histogram
equ = cv2.equalizeHist(image)

#displaying the images
cv2.imshow("Images", np.hstack([image, equ]))
cv2.waitKey(0)