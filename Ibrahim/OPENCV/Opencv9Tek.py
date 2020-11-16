
import cv2
import numpy as np

img = cv2.imread(r"Ibrahim\OPENCV\corner1.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gri = np.float32(gri)
koseler = cv2.goodFeaturesToTrack(gri,100,0.1,10)
koseler = np.int0(koseler)
for kose in koseler:
    x,y = kose.ravel()
    cv2.circle(img,(x,y),3,255,-1)


cv2.imshow("Kamera",img)




cv2.waitKey(0)
cv2.destroyAllWindows()