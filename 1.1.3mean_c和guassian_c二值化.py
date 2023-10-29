import cv2
import numpy as np
img = cv2.imread("F:\image\ice.jpg", cv2.IMREAD_GRAYSCALE)
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Original Image', img)
cv2.imshow('Mean Threshold', th1)
cv2.imshow('Gaussian Threshold', th2)
cv2.waitKey(0)
cv2.destroyAllWindows()