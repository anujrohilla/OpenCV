# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 18:41:47 2018

@author: Dell
"""
#importing the required modules
import cv2
import argparse
import numpy as np
import mahotas

#creating the command line argument
arg = argparse.ArgumentParser()
arg.add_argument("-i","--image",required = True, help = "Path of the image")
args = vars(arg.parse_args())

#loading the image
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.bilateralFilter(image, 9, 51, 51)

T = mahotas.thresholding.otsu(image)

print(f"Vallue of Otsu Threshold {T}")

thresh_o = image.copy()
thresh_o[thresh_o > T] = 255
thresh_o[thresh_o < T] = 0

T = mahotas.thresholding.rc(image)

print(f"Vallue of Riddler Threshold {T}")

thresh_r = image.copy()
thresh_r[thresh_r < T] = 0
thresh_r[thresh_r > T] = 255

images = np.hstack([image, thresh_o, thresh_r])

cv2.imshow("Images",images)
cv2.waitKey(0)