
import cv2
import numpy as np

img = cv2.imread(r"Ibrahim\OPENCV\balon.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask= mask)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(mask,kernel,iterations = 1)
dilation = cv2.dilate(mask,kernel,iterations = 1)

cv2.imshow("Kamera",img)
cv2.imshow('Mask',mask)
cv2.imshow('Erosion',erosion)
cv2.imshow('Dilation',dilation)
cv2.imshow("Kamera",img)




cv2.waitKey(0)
cv2.destroyAllWindows()