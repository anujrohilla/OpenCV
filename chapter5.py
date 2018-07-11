#importing modules required
import cv2
import numpy as np

#creating blank screen
canvas = np.zeros((300,300,3),dtype="uint8")

#logic for chessboard pattern
for (row, y) in enumerate(range(0,300,10)):
    for (col, x) in enumerate(range(0,300,10)):
        color = (0,0,255)
        
        if row % 2 == col % 2:
            color = (0,0,0)
        #creating rectangle    
        cv2.rectangle(canvas, (x,y),(x+10,y+10),color,-1)
 #creating circle       
cv2.circle(canvas,(300 // 2, 300 // 2),50,(0,255,0),-1)

#printing the final pattern
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)