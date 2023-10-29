import cv2
import numpy as np
img = cv2.imread("F:\image\mai.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("aa",img)
ret, pic = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('result3',pic)
print(ret)
cv2.waitKey(0)
cv2.destroyAllWindows()
im = np.array(pic)
im.save("D:\\result3\\Otsu.jpg")