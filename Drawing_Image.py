import cv2
print(cv2.__version__)
#Capture frame from camera
cam=cv2.VideoCapture(0)
while True:
    #Assign frame to variable
    ret, frame = cam.read()
    #Drive rectangle to image
    frame=cv2.rectangle(frame,(200,50),(140,300),(255,200,100),4)
    #Drive circle to image
    frame=cv2.circle(frame,(200,50),100,(255,200,100),-1)
    #Add text to image
    frame=cv2.putText(frame,'YAVUZ BALI',(140,200),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,150),2)
    #Drive line to image
    frame=cv2.line(frame,(10,10),(400,400),(4,4,4),4)
    #Printing the image to the screen
    cv2.imshow('nanoCam',frame)

    #Take input from keyboard
    if cv2.waitKey(1)==ord('q'):
        break
        
cam.release()
cv2.destroyAllWindows()
