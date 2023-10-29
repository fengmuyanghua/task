import os

import cv2
import numpy as np
# lst_b=[]
lst_w=[]
image=cv2.imread(r"F:\2task\A2.1\tahiti.png",0)
_,img=cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
pic=np.array(img)
h,w=pic.shape
flag=True
print(h,w)

for i in range(h):
    if all(pixel==0 for pixel in pic[i]):
        flag=False
    elif flag==False:
        lst_w.append(i)
        flag=True

print("len(lst_w):",len(lst_w))
# print(len(lst_b))
print("lst_w:",lst_w)
# print(lst_b)
x=len(lst_w)
# for n in range(x):
#     roi=img[lst_w[n]:lst_b[n],0:w]
for n in range(0,x-1):
    roi=img[lst_w[n]:lst_w[n+1],0:w]
    print(roi)
    # cv2.imshow("roi",roi)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    filename=f'cartoon+{n+1}.jpg'
    path=r"F:\image_result\A2.2\111"
    # cv2.imwrite(os.pardir.join(path,filename),roi[0])
    file_path = os.path.join( path, filename )
    cv2.imwrite( file_path, roi )
roi=img[lst_w[x-1]:h,0:w]
print(roi)
q=len(lst_w)
filename=f'cartoon+{q}.jpg'
path=r"F:\image_result\A2.2\111"
file_path = os.path.join( path, filename )
cv2.imwrite( file_path, roi )