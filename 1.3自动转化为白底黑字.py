import cv2
import numpy as np
from PIL import Image
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()

img=cv2.imread(r"F:\\image\\333.jpg")
cv_show('dd',img)
t1,change=cv2.threshold(img,25,255,cv2.THRESH_BINARY)
# cv_show('change',change)
img_array=np.array(change)
h=img.shape[0]
w=img.shape[1]
for i in range(h):
    for j in range(w):
        if img_array[i][j].all()==0:
             img_array[i][j]=255
        else:
            img_array[i][j]=0
img_change = Image.fromarray(change)
img_change.save(r"F:\\image_result\\change.jpg")
cv_show('ss',img_array)