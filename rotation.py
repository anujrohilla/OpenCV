#importing the required modules
import cv2
import argparse
import imutils

#creating the commandline argument
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(arg.parse_args())

#loading the image
image = cv2.imread(args["image"])

#displaying the original image
cv2.imshow("Original Image", image)

#reading the height and width of the image
(h,w) = image.shape[:2]

#generating the rotation matrix : paramaeters - point for rotation, angle in degree(+ve means anticloackwise, -vs means cloackwise), scaling factor
M = cv2.getRotationMatrix2D((w // 2, h // 2), 90, 1.0)

#rotating the image
rotated = cv2.warpAffine(image, M, (w,h))

#displaying the rotated image
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)

#using the imutils module for rotation
rotated = imutils.rotate(image,-45)

#displaying the rotated image
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)