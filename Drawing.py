import cv2
print(cv2.__version__)

cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    frame=cv2.rectangle(frame,(200,50),(140,300),(255,200,100),4)
    frame=cv2.circle(frame,(200,50),100,(255,200,100),-1)
    frame=cv2.putText(frame,'YAVUZ BALI',(140,200),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,150),2)
    frame=cv2.line(frame,(10,10),(400,400),(4,4,4),4)
    cv2.imshow('nanoCam',frame)


    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()