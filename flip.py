# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:25:58 2018

@author: Anuj Rohilla
"""
import cv2
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required = True, help = "Path of the image")
args = vars(arg.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Original Image",image)

flip_h = cv2.flip(image, 1)

cv2.imshow("Horizontal Flip", flip_h)

flip_v = cv2.flip(image, 0)

cv2.imshow("Vertical Flip", flip_v)

flip_vh = cv2.flip(image, -1)

cv2.imshow("Horizontal-Vertical Flip", flip_vh)
cv2.waitKey(0)