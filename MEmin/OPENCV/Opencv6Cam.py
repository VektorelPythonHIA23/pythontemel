
import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,frame = cap.read()
    
    kernel = np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(frame,0,kernel)
    blur = cv2.GaussianBlur(frame,(25,25),-1)
    cv2.imshow("Kamera",frame)
    cv2.imshow("Smooth",smooth)
    cv2.imshow("blur",blur)
    median = cv2.medianBlur(frame,15)
    cv2.imshow('Median Blur',median)
    bilateral = cv2.bilateralFilter(frame,15,75,75)
    cv2.imshow('bilateral Blur',bilateral)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()