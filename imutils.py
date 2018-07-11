# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:50:08 2018

@author: Anuj Rohilla
"""
#importing required modules
import cv2
import numpy as np

#function for translation, which takes input the image, tx and ty
def translate(image, tx, ty):
   """This function is for translating the image""" 
    #creating translation matrix
   M = np.float32([[1,0,tx],[0,1,ty]])
    
    #translating the image
   shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
    
   return shifted

#function for rotation, which takes input the image, point of rotation, angle of rotation and scaling factor
def rotate(image, angle, point = None, scale=1.0):
    """This function is for rotating the image""" 
    
    #reading shape of the image
    (h, w) = image.shape[:2]
    
    #if point of rotation is not specified then take it as center of image
    if point == None:
        point = (w//2, h//2)
    
    #creating the rotation matrix    
    M = cv2.getRotationMatrix2D(point, angle, scale)
    
    #rotating the images
    rotated = cv2.warpAffine(image, M, (w, h))
    
    #returning the rotated image
    return rotated

#function for resizing, which takes input the image, width, height and interpolation method
def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    """This function is for resizing the image"""
    
    #if width is not set then calculate the aspect ratio using height
    if width is None:
        r = height/image.shape[0]
        dim = (int(r * image.shape[1]), height)
        
    #else calculate the aspect ratio using the width
    else:
        r = width/image.shape[1]
        dim = (width, int(r * image.shape[0]))
    
    #resizing the image
    resize = cv2.resize(image, dim, interpolation = inter)
    
    #return the resized image
    return resize
    
