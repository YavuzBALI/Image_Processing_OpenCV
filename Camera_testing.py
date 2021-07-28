import cv2
print(cv2.__version__)

#Capture frame from camera
cam=cv2.VideoCapture(0)
while True:
    #Assign frame to variable
    ret, frame = cam.read()
    #Printing the image on the screen 
    cv2.imshow('nanoCam',frame)
    #Positioning your image on the screen 
    cv2.moveWindow('nanoCam',0,200)
    
    #Getting input from the keyboard so exit the code
    if cv2.waitKey(1)==ord('q'):
        break
#Release the camera
cam.release()
#Erase the screen
cv2.destroyAllWindows()
