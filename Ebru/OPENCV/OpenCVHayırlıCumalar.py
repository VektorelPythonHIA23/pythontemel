
import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
yuz_cas = cv2.CascadeClassifier(r"Ibrahim\OPENCV\cascades\haarcascade_frontalface_default.xml")
while True:
    ret,frame = cap.read()
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    detect = yuz_cas.detectMultiScale(gri,1.3,5)
    for x,y,w,h in detect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        

    cv2.imshow("Kamera",frame)

  
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()