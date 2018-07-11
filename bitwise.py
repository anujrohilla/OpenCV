# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 15:25:22 2018

@author: Anuj Rohilla
"""
#importing the required modules
import cv2
import numpy as np

#creating a blank screen
rect = np.zeros((300,300), dtype = "uint8")

#creating rectangle in the previously created blank screen
cv2.rectangle(rect, (25,25),(275,275), (255,255,255), -1)

#creating another blank screen
circle = np.zeros((300,300), dtype = "uint8")

#creating a cricle in the blank screen
cv2.circle(circle, (150,150), 150, (150,150,150),-1)

#Bitwise AND between circle and rect screen
bit_and = cv2.bitwise_and(circle, rect)

#displaying the ANDED image
cv2.imshow("Bitwise AND", bit_and)

#Bitwise AND between circle and rect screen
bit_or = cv2.bitwise_or(circle, rect)

#displaying the ORED image
cv2.imshow("Bitwise OR", bit_or)

#Bitwise AND between circle and rect screen
bit_xor = cv2.bitwise_xor(circle, rect)

#displaying the XORED image
cv2.imshow("Bitwise XOR", bit_xor)

#taking NOT of rect screen
bit_not = cv2.bitwise_not(rect)

#displaying the NOT image
cv2.imshow("Bitwise NOT", bit_not)
cv2.waitKey(0)
