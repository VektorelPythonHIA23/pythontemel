
import cv2
import numpy as np

img = cv2.imread(r"Ibrahim\OPENCV\resim2.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread(r"Ibrahim\OPENCV\template.jpg",0)
w,h = template.shape[::-1]
res = cv2.matchTemplate(gri,template,cv2.TM_CCOEFF_NORMED)
thresh = 0.7
loc = np.where(res>=thresh)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),1)


cv2.imshow("Kamera",img)




cv2.waitKey(0)
cv2.destroyAllWindows()