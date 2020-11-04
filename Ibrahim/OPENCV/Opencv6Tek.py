
import cv2
import numpy as np

img = cv2.imread(r"Ibrahim\OPENCV\balon.png")



cv2.imshow("Kamera",img)

cv2.waitKey(0)
cv2.destroyAllWindows()