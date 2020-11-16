import cv2
import numpy as np

img = cv2.imread(r"Hamit/OPENCV/cinar.jpg")

cv2.line(img,(0,0),(150,150),(255,255,255),4)
cv2.rectangle(img,(0,0),(150,150),(20,50,100),2)
cv2.circle(img,(100,63),55,(0,255,0),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'cinar',(10,200),font,3,(255,0,0),6,cv2.LINE_8)

pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)


cv2.imshow("Sonuc",img)

cv2.waitKey(0)
cv2.destroyAllWindows()