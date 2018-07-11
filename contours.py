# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:18:36 2018

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

#converting the colored image into grascale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blurring the image
blur = cv2.GaussianBlur(gray, (3,3), 0)
pyr = cv2.pyrMeanShiftFiltering(image, 20, 51)
bi_blur = cv2.bilateralFilter(gray, 7, 41, 41)

#applying the canny edge detection
canny = cv2.Canny(blur, 50, 150)
canny_pyr = cv2.Canny(pyr, 50, 150)
canny_bi = cv2.Canny(bi_blur, 50, 150)

#displaying the edge detected image
cv2.imshow("Canny", canny)
cv2.imshow("Canny_pyr", canny_pyr)
cv2.imshow("Canny_bi", canny_bi)

#finding contours in the 
(img, cnts, _) = cv2.findContours(canny_bi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(f"Number of countours {len(cnts)}")

#copying the image for drawing the contour on it
img_copy = image.copy()

#filtering the contour by an area threshold
for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area > 100:
        cv2.drawContours(img_copy, cnt, -1, (0, 0, 255), 2)
        
#displaying the contour
cv2.imshow("Image_Copy by area threshold", img_copy)
cv2.waitKey(0)

#filtering the contour by seecting maximum area contour
max = 0
big = []

for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area > max:
        max = area
        big.append(cnt)
        
cv2.drawContours(img_copy, big, len(big)-1, (0, 0, 255), 2)

#displaying the contour
cv2.imshow("Image_Copy by max area", img_copy)
cv2.waitKey(0)