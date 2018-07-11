# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:51:25 2018

@author: Anuj Rohilla
"""
import cv2
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-i","--image", required = True, help = "Path of the image")
args = vars(arg.parse_args())

image = cv2.imread(args["image"])

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.bilateralFilter(image, 7, 41, 41)

canny = cv2.Canny(blur, 50, 150)

cv2.imshow("Canny",canny)

img_copy = image.copy()

(img, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

max = 0
big = []

for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area > max:
        max = area
        big.append(cnt)
        
cv2.drawContours(img_copy, big, len(big)-1, (255, 0, 0), 2)

cv2.imshow("Image_Copy by max area", img_copy)
cv2.waitKey(0)
