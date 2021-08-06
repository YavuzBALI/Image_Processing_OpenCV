import numpy as np
import cv2 as cv
import time

while True:
    #Read .jpeg file
    img = cv.imread('goruntuler/Red_Robot.jpeg')
    #Convert gray to image 
    gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    #Add blur to image
    gray = cv.medianBlur(gray,5)

    #The Hough Circle function is called.
    circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,30,
                                param1=50,param2=30,minRadius=15,maxRadius=35)
    if np.any(circles):#Here we checked with np.any if the array is empty or full
        circles = np.uint16(np.around(circles))
        x = circles[0,:]
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv.rectangle(img,(i[0]-45,i[1]-45),(i[0]+45,i[1]+45),(255,0,0),2)
            # draw the center of the circle
            cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
    #The image is printed on the screen
    cv.imshow('detected circles',img)
    #Checking the 'q' key to turn it off
    if cv.waitKey(1)==ord('q'):
        break
