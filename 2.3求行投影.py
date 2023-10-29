# import cv2
# import numpy as np
# from PIL import Image
# img=cv2.imread(r"F:\\image\\human.jpg",0)
# ret,pic=cv2.threshold(img,128,255,cv2.THRESH_BINARY)
# pic_array=np.array(pic)
# h=pic.shape[1]
# w=pic.shape[0]
# print(h)
# print(w)
# lst=[]
#
# img_pil=Image.fromarray(pic_array)
# for i in range (1,h+1):
#     t=0
#     for j in range (1,w+1):
#         if pic_array[i][j]==0:
#            t=t+1
#     lst.append(t)
# for i in range(h):
#     for n in range (lst[i-1]):
#         img_pil.putpixel( (i,n), 0)   # 在(x, y)处打印一个黑色像素点
# result_array = np.array(img_pil)

import cv2
import numpy as np
from PIL import Image

img = cv2.imread(r"F:\2task\dataset\dataset\train\image\image_2.jpg", 0)
ret, pic = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
pic_array = np.array(pic)
h = pic.shape[0]  # 修正：获取图像的高度
w = pic.shape[1]  # 修正：获取图像的宽度
print(h)
print(w)
lst = []
img_pil = Image.fromarray(pic_array)
for i in range(h):
    t = 0
    for j in range(w):
        if pic_array[i][j] == 0:
            t += 1
    lst.append(t)
for i in range(h):
    for n in range(lst[i] - 1):
        img_pil.putpixel((n, i), 0)  # 修正：调整坐标顺序，将 (i, n) 修改为 (n, i)
result_array = np.array(img_pil)
cv2.imshow("result",result_array)
cv2.waitKey(0)
cv2.destroyAllWindows()