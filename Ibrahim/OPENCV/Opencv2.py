import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,frame = cap.read()
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri,(15,15),0)
    cv2.imshow("Kamera",blur)
    # frame[150:250,150:250] = frame[50:150,50:150]
    # cv2.imshow("Kamera3",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()