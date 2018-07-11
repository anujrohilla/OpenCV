#importing the modules required
import cv2
import numpy as np

#creating the blank area in black color for drawing the shapes
blank = np.zeros((400,400,3), dtype="uint8")

#drawing the line from top left corner to bottom right corner
cv2.line(blank,(0,0),(400,400),(0,100,100))

#displaying the line
cv2.imshow("Line 1",blank)
cv2.waitKey(0)

#drawing the line from bottom left corner to top right corner with width of 4 pixels
cv2.line(blank,(400,0),(0,400),(100,100,0),4)

#displaying the line
cv2.imshow("Line 2",blank)
cv2.waitKey(0)

#drawing a rectangle from (100,100) [top left corner of rectangle] to (125,130) [bottom right corner of rectangle]
cv2.rectangle(blank,(100,100),(125,130),(150,150,150))

#displaying the rectangle
cv2.imshow("Rectangle 1",blank)
cv2.waitKey(0)

#drawing a rectangle from (250,100) [top left corner of rectangle] to (195,180) [bottom right corner of rectangle] with width of 10 pixels
cv2.rectangle(blank,(250,100),(195,180),(150,150,150), 10)

#displaying the rectangle
cv2.imshow("Rectangle 2",blank)
cv2.waitKey(0)

#drawing a rectangle from (50,10) [top left corner of rectangle] to (95,80) [bottom right corner of rectangle] with fully filled
cv2.rectangle(blank,(50,10),(95,80),(250,250,250), -10)

#displaying the rectangle
cv2.imshow("Rectangle 3",blank)
cv2.waitKey(0)

#Creating new blank area for drawing circles
new_blank = np.zeros((400,400,3),dtype="uint8")

#Taking center of the blank area 
(center_x,center_y) = (new_blank.shape[1] // 2, new_blank.shape[0] // 2)

#drawing circles with center as the center of the blank area nad radius from 0 to 200 with the gap of 10
for radius in range(0,200,10):
    cv2.circle(new_blank, (center_x,center_y), radius, (90,90,90))
    
#displaying the circles
cv2.imshow("Circles", new_blank)
cv2.waitKey(0)

#drawing circles filled with random colors, with random centers and random radius
for i in range(5):
    radius = np.random.randint(2,high=110)
    center = np.random.randint(0,high=65,size=(2,))
    color = np.random.randint(0,high=256,size=(3,)).tolist()
    
    cv2.circle(new_blank,tuple(center),radius,color,-1)

#displaying the filled circles    
cv2.imshow("Filled Circles",new_blank)
cv2.waitKey(0)
