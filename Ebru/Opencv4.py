
import cv2
import numpy as np

img = cv2.imread(r"Ebru\OPENCV\bookpage.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# retval,threshold = cv2.thresold(img,10,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gri,255,ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)

cv2.imshow("Sonuc",img)
cv2.imshow("Sonuc2",threshold)


cv2.waitKey(0)
cv2.destroyAllWindows()