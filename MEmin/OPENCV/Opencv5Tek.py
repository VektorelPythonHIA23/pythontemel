
import cv2
import numpy as np

img = cv2.imread(r"Ibrahim\OPENCV\balon.png")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

dus = np.array([30,150,50])
yuk = np.array([255,255,180])

mask = cv2.inRange(hsv,dus,yuk)
res = cv2.bitwise_and(img,img,mask=mask)


cv2.imshow("Kamera",img)
cv2.imshow("MAsk",mask)
cv2.imshow("RESULT",res)

cv2.imshow("Sonuc",img)

cv2.waitKey(0)
cv2.destroyAllWindows()