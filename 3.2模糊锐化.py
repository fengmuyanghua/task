import cv2
import numpy as np
from PIL import Image

image = cv2.imread(r"F:\3task\A3\001.3-bin.png", 0)
# image=cv2.GaussianBlur(image,(3,3),1)
# 1. 模糊锐化
# cv2.blur()、cv2.filter2D()
#模糊
dst1 = cv2.blur(image, (1, 1))
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # 自定义锐化核
#锐化
dst2 = cv2.filter2D(image, -1, (1,1))

# 2. 膨胀腐蚀
# 膨胀(dilate)与腐蚀(erode)接口

# image=cv2.GaussianBlur(image,(3,3),)
# 膨胀图像
dilated = cv2.dilate(image, (50,50), iterations=3)
# 腐蚀图像
erosion = cv2.erode(dilated , (1,  1), iterations=1)
image=cv2.resize(image,(0,0), fx=0.2, fy=0.2)
dst1 = cv2.resize(dst1, (0, 0), fx=0.2, fy=0.2)
dst2 = cv2.resize(dst2, (0, 0), fx=0.2, fy=0.2)
erosion = cv2.resize(erosion, (0, 0), fx=0.2, fy=0.2)

#第二个参数用于指定缩放后图像的大小，（0,0）表示自动计算缩放后图像的大小
# cv2.imshow("dst1", dst1)
cv2.imshow("image",image)
cv2.imshow("blur_filter", dst2)
cv2.imshow("erosion_dilated1", erosion)
# cv2.imshow("erosion_dilated2", dilated)
# cv2.imshow("dilated", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()