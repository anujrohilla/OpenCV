# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:56:27 2018

@author: Anuj Rohilla
"""
#importing the required modules
import cv2
import argparse
from matplotlib import pyplot as plt
import numpy as np

#function to plot color histogram with mask
def hist_plot(image, title, mask = None):
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("Number of Pixels")
    
    for (channel, color) in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], mask, [256], [0,256])
        plt.plot(hist, color = color)
        plt.xlim([0,256])
    
    plt.show()

#creating the command line argument
arg = argparse.ArgumentParser()
arg.add_argument("-i","--image",required = True, help = "Path of the image")
args = vars(arg.parse_args())

#loading the image
image = cv2.imread(args["image"])

#displaying original image
cv2.imshow("Original Image", image)

#calling the hit_plot function to plot histogram for original image
hist_plot(image, "Original Image")

#creating the blank mask 
mask = np.zeros(image.shape[:2], dtype = "uint8")

#creating the mask
cv2.rectangle(mask, (10,100), (90, 150), 255, -1)

#calling the hit_plot function to plot histogram for original image
hist_plot(image, "Masked Image", mask)
