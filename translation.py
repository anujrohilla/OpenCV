#importing the required modules
import cv2
import numpy as np
import argparse
import imutils

#creating the mandatory command line argument of image path 
arg = argparse.ArgumentParser()
arg.add_argument("-i","--image",required = True, help = "Path of the image")
#converting the command line arguments into dictionary
args = vars(arg.parse_args())

#reading the image from the command line 
image = cv2.imread(args["image"])

#displaying the original image
cv2.imshow("Original Image",image)
cv2.waitKey(0)

#creating the shift matrix
M = np.float32([[1,0,25],[0,1,35]])


shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))

#displaying the shifted image
cv2.imshow("Shifted Image right and down",shifted)
cv2.waitKey(0)

#creating the shift matrix
M = np.float32([[1,0,-25],[0,1,-35]])

#shifting the image by using the matrix 
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))

#displaying the shifted image
cv2.imshow("Shifted Image left and up",shifted)
cv2.waitKey(0)

#using imutils module for translation
shifted = imutils.translate(image,30,10)

#displaying the shifted image
cv2.imshow("Shifted",shifted)
cv2.waitKey(0)