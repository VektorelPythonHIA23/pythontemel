
import cv2
import numpy as np

img = cv2.imread(r"Ibrahim\OPENCV\bookpage.jpg")

cv2.imshow("Sonuc",img)

cv2.waitKey(0)
cv2.destroyAllWindows()