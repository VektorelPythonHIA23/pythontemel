import cv2

import numpy as np

img = cv2.imread(r"Bulent\OPENCV\resim.jpg")


cv2.line(img,(0,0),(150,150),(215,140,34),6,cv2.LINE_8)
# px = img[50:50,100:100]
#px = img[50:50,100:100]
#img[50:150,50:150] = [0,0,0]
#img[150:250,150:250] = img[50:150,50:150]

cv2.rectangle(img,(0,0),(150,150),(255,255,10),2)
cv2.circle(img,(100,63),55,(0,255,0),-1)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Bulent",(10,200),font,2,(20,25,25),6)

# cv2.polylines(img,)


cv2.imshow("sonuc",img)
cv2.waitKey(0)
cv2.destroyAllWindows()