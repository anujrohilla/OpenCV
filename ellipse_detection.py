# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:52:01 2018

@author: Anuj Rohilla
"""
import cv2
from PIL import Image
import math

def detectEllipse(filePath, minR, maxR, minAmountOfEdges):
    print("Loaded the image")
    image = cv2.imread(filePath) # proceed with lower res.
    w, h = image.shape[1], image.shape[0]

    # Ellipse Detection
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray",gray)
    cv2.waitKey(0)
    EdgePixel = []

    # Step 1 - Save all Edge-Pixels in an array
    for x in range(gray.shape[0]):
        for y in range(gray.shape[1]):
            if gray[x, y] == 0:
                EdgePixel.append([x,y])
    
    print("Loaded the EdgePixel array")
    
    print(EdgePixel)

    # Step 2 - Initialize AccumulatorArray and EllipsesFound-Array
    AccumulatorArray = []
    EllipsesFound = []

    # Step 3 - Loop through all pixels
    ignore_indices = set()
    for i in range(len(EdgePixel)):
        if i in ignore_indices:
            continue
        # Step 4 - Loop through all pixels a second time
        print("Inside First loop")
        for j in range(len(EdgePixel)):
            if j in ignore_indices:
                continue
            if i != j:
                xAverage, yAverage, aAverage, bAverage, orientationAverage = 0, 0, 0, 0, 0
            # (Step 12, clear Accumulator-Array)
            print("Inside second loop")
            AccumulatorArray = []

            tmp = math.sqrt(abs(math.pow(EdgePixel[i][0]-EdgePixel[j][0], 2)) + 
                  abs(math.pow(EdgePixel[i][1]-EdgePixel[j][1], 2)))
            distance = int(tmp)
            # Step 4.1 - Check if the distance is "ok"
            if(distance / 2 > minR and distance / 2 < maxR):
                print("Inside distance of second loop")
                # Step 5 - Calculate 4 parameters of the ellipse
                xMiddle     = (EdgePixel[i][0] + EdgePixel[j][0]) / 2
                yMiddle     = (EdgePixel[i][1] + EdgePixel[j][1]) / 2
                a           = tmp / 2
                if(EdgePixel[j][0] != EdgePixel[i][0]): # To prevent division by 0
                    orientation = math.atan((EdgePixel[j][1]-EdgePixel[i][1])/
                                            (EdgePixel[j][0]-EdgePixel[i][0]))
                else:
                    orientation = 0

                # Step 6 - Lop through all pixels a third time
                for k in range(len(EdgePixel)):
                    if k in ignore_indices:
                        continue
                    if len(AccumulatorArray) > minAmountOfEdges:
                        continue
                    if k != i and k != j:
                        # Distance from x,y to the middlepoint
                        innerDistance = math.sqrt(abs(math.pow((xMiddle - EdgePixel[k][0]),2)) + 
                                        abs(math.pow((yMiddle - EdgePixel[k][1]),2)))
                        # Distance from x,y to x2,y2
                        tmp2 = math.sqrt(abs(math.pow((EdgePixel[i][0] - EdgePixel[j][0]),2)) + 
                                         abs(math.pow((EdgePixel[i][1] - EdgePixel[j][1]),2)))

                        # Distance from x,y and x0,y0 has to be smaller then the distance from x1,y1 to x0,y0
                        if(innerDistance < a and innerDistance > minR and innerDistance < maxR):
                            # Step 7 - Calculate length of minor axis

                            # calculate cos^2(tau):
                            tau = math.pow(((math.pow(a,2)+math.pow(innerDistance,2)-math.pow(tmp2,2))/(2*a*innerDistance)),2)  
                            bSquared = (math.pow(a, 2)*math.pow(innerDistance, 2)*(1-tau))/(math.pow(a, 2)-math.pow(innerDistance, 2)*tau)
                            # It follows:
                            b = math.sqrt(bSquared) # this is the minor axis length

                            # Step 8 - Add the parameters to the AccumulatorArray
                            Data = [xMiddle, yMiddle, a, b, orientation]
                            AccumulatorArray.append(Data)
                # Step 9 (repeat from Step 6 till here)
                # Step 10 - Check if the algorithm has detected enough Edge-Points and then average the results
                if len(AccumulatorArray) > minAmountOfEdges: 
                    # Averageing
                    for k in range(len(AccumulatorArray)):
                        tmpData = AccumulatorArray[k]
                        xAverage            += tmpData[0]
                        yAverage            += tmpData[1]
                        aAverage            += tmpData[2]
                        bAverage            += tmpData[3]
                        orientationAverage  += tmpData[4]
                    xAverage            = int(xAverage / len(AccumulatorArray))
                    yAverage            = int(yAverage / len(AccumulatorArray))
                    aAverage            = int(aAverage / len(AccumulatorArray))
                    bAverage            = int(bAverage / len(AccumulatorArray))
                    orientationAverage  = int(orientationAverage / len(AccumulatorArray))

                    # Step 11 - Save the found Ellipse-Parameters
                    EllipsesFound.append([xAverage, yAverage, aAverage, bAverage, orientationAverage])
                    print(EllipsesFound)
                    # Step 12 - Remove the Pixels on the detected ellipse from the Edge-Array
                    for k in range(len(EdgePixel)):
                        if ((math.pow(EdgePixel[k][0] - xAverage, 2) / math.pow((aAverage+5), 2)) + 
                               ((math.pow(EdgePixel[k][1] - yAverage, 2) / math.pow((bAverage+5), 2)))) <= 1:
                            ignore_indices.add(k)
    return

detectEllipse("ellipse.jpg", 1, 100, 100)
