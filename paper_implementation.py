# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:19:33 2018

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

cv2.imshow("image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, (3,3))

cv2.imshow("tophat", tophat)

(T, thresh) = cv2.threshold(tophat, 10, 255, cv2.THRESH_BINARY)

cv2.imshow("thresh", thresh)

dilation = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, (3,3))

cv2.imshow("dilate", dilation)

pyr = cv2.pyrMeanShiftFiltering(image, 15, 40)
cv2.imshow("pyr", pyr)

(T, thresh) = cv2.threshold(pyr, 40, 255, cv2.THRESH_BINARY)

cv2.imshow("threshold", thresh)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, (5,5))

cv2.imshow("open", opening)

cv2.waitKey(0)