import cv2 

img = cv2.imread(r"Ebru\OPENCV\resim.jpg")

cv2.line(img,(0,0),(150,150),(255,255,255),4)
cv2.rectangle(img,(0,0),(150,150),(20,50,100),2)
cv2.circle(img,(100,63),55,(0,255,0),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'ebru',(10,200),font,3,(255,255,255),6,cv2.LINE_8)



cv2.imshow("Sonuc",img)

cv2.waitkey(0)
cv2.destroyAllWindows()