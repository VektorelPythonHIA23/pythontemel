import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dus = np.array([30,150,50])
    yuk = np.array([255,255,180])

    mask = cv2.inRange(hsv,dus,yuk)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    

    cv2.imshow("Kamera",frame)
    cv2.imshow("MAsk",mask)
    cv2.imshow("RESULT",res)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()