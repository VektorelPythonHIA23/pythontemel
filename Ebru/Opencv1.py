import cv2    

img = cv2.imread(r"Ebru\OPENCV\resim.jpg")

print(img[50:150,50:150])
print(img.shape)
cv2.imshow("baslik",img)

gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gri[50:150,50:150])
print(gri.shape)
cv2.imshow("baslik2",gri)

cv2.waitKey(0)
cv2.destroyAllWindows()