import cv2
img = cv2.imread(r"F:\image\333 .jpg", cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours, x = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    if area > 300:
        center_color = int(cv2.mean(img[y:y+h, x:x+w])[0])
        if center_color > 128:
            print('白底黑字')
            cv2.imshow("a",binary)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print('黑底白字')
            cv2.imshow("b", binary)
            cv2.waitKey(0)
            cv2.destroyAllWindows()