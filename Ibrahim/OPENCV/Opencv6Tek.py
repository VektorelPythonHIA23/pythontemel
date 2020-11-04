
import cv2
import numpy as np

img = cv2.imread(r"Ibrahim\OPENCV\balon.png")

kernel = np.ones((15,15),np.float32)/225
smooth = cv2.filter2D(img,0,kernel)
blur = cv2.GaussianBlur(img,(25,25),-1)
cv2.imshow("Kamera",img)
cv2.imshow("Smooth",smooth)
cv2.imshow("blur",blur)
median = cv2.medianBlur(img,15)
cv2.imshow('Median Blur',median)
bilateral = cv2.bilateralFilter(img,15,75,75)
cv2.imshow('bilateral Blur',bilateral)



cv2.waitKey(0)
cv2.destroyAllWindows()