import cv2
print(cv2.__version__)
#Capture frame from camera
cam=cv2.VideoCapture(0)
while True:
    #Assign frame to variable
    ret, frame = cam.read()
    #Resize frame to 320 width 240 height
    frame2=cv2.resize(frame,(320,240))
    cv2.imshow('nanoCam',frame2)
    cv2.moveWindow('nanoCam',0,0)

    #To exit, input is taken from the keyboard.
    if cv2.waitKey(1)==ord('q'):
        break
        
cam.release()
cv2.destroyAllWindows()
