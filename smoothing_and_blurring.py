# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:03:41 2018

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

#Average Blur (take mean of neighboring pixels)
blured = np.hstack([cv2.blur(image, (3,3)),
                    cv2.blur(image, (5,5)),
                    cv2.blur(image, (7,7))])

#Displaying average blurred image
cv2.imshow("Average Blur", blured)

#Gaussian Blur (take weighted mean of neighboring pixels i.e more weight to near neighbours)
blured = np.hstack([cv2.GaussianBlur(image, (3,3), 0),
                    cv2.GaussianBlur(image, (5,5), 0),
                    cv2.GaussianBlur(image, (7,7), 0)])

#Displaying Gaussian blurred image
cv2.imshow("Gaussian Blur", blured)

#Medain Blur (take median of neighboring pixels, used to remove salt and pepper noise)
blured = np.hstack([cv2.medianBlur(image, 3),
                    cv2.medianBlur(image, 5),
                    cv2.medianBlur(image, 7)])

#Displaying Median blurred image
cv2.imshow("Median Blur", blured)

#Bilateral Blur (it is used to preserve the edges of the objectss)
blured = np.hstack([cv2.bilateralFilter(image, 3, 21, 21),
                    cv2.bilateralFilter(image, 5, 31, 31),
                    cv2.bilateralFilter(image, 7, 41, 41)])

#Displaying Bilateral blurred image
cv2.imshow("Bilateral Blur", blured)
cv2.waitKey(0)
