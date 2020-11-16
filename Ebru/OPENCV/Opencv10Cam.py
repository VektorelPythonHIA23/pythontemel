
import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fgbg = cv2.createBackgroundSubtractorKNN()
# cap = cv2.VideoCapture(r"Ibrahim\OPENCV\people-walking.mp4")
while True:
    ret,frame = cap.read()
    fgMask = fgbg.apply(frame)
    
    cv2.imshow("Kamera",frame)
    cv2.imshow("Kamera2",fgMask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()