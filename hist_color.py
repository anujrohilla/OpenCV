# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:30:28 2018

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

#displaying the original image
cv2.imshow("Original Image", image)

#splitting the channels from the image
channels = cv2.split(image)

colors = ("b", "g", "r")

#Setting up PyPlot figure
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")

#creating histogram for ifferent channels
for (channel, color) in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
    plt.xlim([0,256])

#displaying the plot
plt.show()

#Plotting a 2-D histogram 

fig = plt.figure()

sp = fig.add_subplot(131)

hist = cv2.calcHist([[channels[1],channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256]])
p = sp.imshow(hist, interpolation = "nearest")
sp.set_title("2D Color Histogram of Green and Blue")
plt.colorbar(p)

sp = fig.add_subplot(132)

hist = cv2.calcHist([[channels[1],channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256]])
p = sp.imshow(hist, interpolation = "nearest")
sp.set_title("2D Color Histogram of Green and Red")
plt.colorbar(p)

sp = fig.add_subplot(133)

hist = cv2.calcHist([[channels[2],channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256]])
p = sp.imshow(hist, interpolation = "nearest")
sp.set_title("2D Color Histogram of Red and Blue")
plt.colorbar(p)

