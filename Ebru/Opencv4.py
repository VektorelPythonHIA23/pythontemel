
import cv2
import numpy as np

img = cv2.imread(r"Ibrahim\OPENCV\bookpage.jpg")

retval,threshold = cv2.thresold(img,10,255,cv2.THRESH_BINARY)


cv2.imshow("Sonuc",img)
cv2.imshow("Sonuc2",threshold)


cv2.waitKey(0)
cv2.destroyAllWindows()