import cv2
import numpy as np

image=cv2.imread(r"C:\Users\fengmu\Desktop\f89085d7dc207831902b9003bdc5a26.png",0)
thresh,img=cv2.threshold(image,0,255,cv2.THRESH_OTSU,None)

#腐蚀
pic1=cv2.erode(img,(1,1),iterations=1)
#膨胀
pic2=cv2.dilate(img,(1,1),iterations=200)
cv2.imshow("image",image)
cv2.imshow("pic2",pic2)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours,hierarchy=cv2.findContours(pic2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
mask=np.zeros((pic2.shape[0],pic2.shape[1],3),dtype=np.uint8)

cv2.drawContours(mask,contours,-1,(0,125,135),3)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

