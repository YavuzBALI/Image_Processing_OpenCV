import numpy as np
import cv2 as cv
import time

cam=cv.VideoCapture('goruntuler/deneme.avi')
prev_frame_time=0
new_frame_time=0
while True:
    ret, img = cam.read()
#   img = cv.imread('goruntuler/Red_Robot.jpeg')
    gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    gray = cv.medianBlur(gray,5)
    cimg = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,30,
                                param1=50,param2=30,minRadius=15,maxRadius=35)
    if np.any(circles):#burada np.any ile arrayin bos mu dolu mu oldugunu kontrol ettik
        circles = np.uint16(np.around(circles))
        x = circles[0,:]
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv.rectangle(img,(i[0]-45,i[1]-45),(i[0]+45,i[1]+45),(255,0,0),2)
            # draw the center of the circle
            #cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
    
    new_frame_time=time.time()
    fps=1/(new_frame_time-prev_frame_time)
    second=new_frame_time-prev_frame_time
    prev_frame_time=new_frame_time
    fps=int(fps)
    fps_1=str(fps)
    second_1=str(round(second,4))
    cv.putText(img,'Time :'+ second_1,(10,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv.putText(img,'FPS :'+fps_1,(10,25),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv.imshow('detected circles',img)
    if cv.waitKey(1)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()