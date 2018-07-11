# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:38:55 2018

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

#pyramid mean shift for better thresholding results
shifted = cv2.pyrMeanShiftFiltering(image, 15, 40)
cv2.imshow("shifted", shifted)

gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

(T, thresh) = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)

cv2.imshow("Thresh",thresh)

#using open morphological transformation
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, (5,5))

cv2.imshow("opening",opening)

#using close morphological transformation
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, (5,5))

cv2.imshow("closing",closing)

#using top hat morphological transformation
top_hat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, (5,5))

cv2.imshow("top_hat",top_hat)

#My own Top Hat implementation
ope_comp = cv2.bitwise_not(opening)

top_and = cv2.bitwise_and(thresh, ope_comp)

cv2.imshow("Top_And", top_and)

cv2.waitKey(0)