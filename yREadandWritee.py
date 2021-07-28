import cv2
print(cv2.__version__)

cam=cv2.VideoCapture(0)
cam2=cv2.VideoCapture('/home/yavobalo/Desktop/TEz/goruntuler/goruntu1.jpg')
while True:
    ret, frame = cam.read()
    cv2.imshow('nanoCam',frame)

    ret, frame2 = cam2.read()
    cv2.imshow('nanoCam2',frame2)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cam2.release()
cv2.destroyAllWindows()