import cv2

def overlap_tile(img, h, w, stride_h, stride_w):
    rows=(img[0]-h)//stride_h
    if (img[0]-h)%stride_h!=0:
        rows=rows+1
    cols=(img[1]-w)//stride_w
    if(img[1]-w)%stride_w!=0:
        cols=cols+1
    lst = []
    for i in rows:
        for j in cols:
            roi=img[i*stride_h:i*stride_h+h,j*stride_w:j*stride_w+w]
            lst.append(roi)
    return lst

img=cv2.imread(r"F:\image\flower.jpg",0)
h=500
w=500
stride_h=300
stride_w=300
result=overlap_tile(img,h,w,stride_h,stride_w)
for i,roi in enumerate(result):
    cv2.imwrite(f"F:\\image_result\\task3\\task3_2\\2_2\\result{i}".jpg,roi)