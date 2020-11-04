import cv2
img = cv2.imread(r"Zehra\resim.jpg")
cv2.line(img,(0,0),(150,150),(255,255,255),4)    #çizgi çizme başlama,bitiş ,renkve renk kalınlığı
cv2.rectangle(img,(0,0),(150,150),(255,150,150),8) #kare çizme
cv2.circle(img,(200,200),55,(0,255,0),-1)   #55 çap, -1 içi dolu
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img,"Zehra",(10,200),font,3,(255,0,0),3,cv2.LINE_4)
cv2.imshow("sonuc",img)
cv2.waitKey(0)
cv2.destroyAllWindows()