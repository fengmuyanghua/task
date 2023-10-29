import os
import numpy as np
from PIL import Image
import cv2
dir_path = r'F:\2task\dataset\dataset\train\image'
suffix = '.jpg'  # 替换为实际的后缀
file_paths=[]
def get_paths_from_dir(dir_path, suffix='*'):
    for root, dirs, files in os.walk(dir_path):#root：表示正在遍历的目录路径（字符串）dirs：表示当前目录下的子目录列表（字符串列表）files：表示当前目录下的文件列表（字符串列表
        for file in files:
            if file.endswith(suffix):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    return file_paths
# file_paths = get_paths_from_dir(dir_path, suffix)
# for i in file_paths:
#     print(i)
# def cv_show(name,img):
#     cv2.imshow(name,img)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
t=0
lst=[]
if __name__ == "__main__":
    file_paths = get_paths_from_dir( dir_path, suffix )
    for path in file_paths:
        print(path)
        img=cv2.imread(path,0)
        # if img is None:
        #     print( "Failed to read image:", path )
        #     continue
        # cv_show( 'dd', img )

        t1, change =cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # cv2.imshow('change',change)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        img_array = np.array( change )
        h = change.shape[0]
        w = change.shape[1]
        for i in range( h ):
            for j in range( w ):
                if img_array[i][j].all() == 0:
                    img_array[i][j] = 255
                else:
                    img_array[i][j] = 0
        img_change = Image.fromarray( change )
        t=t+1
        img_change.save( r"F:\image_result\white\change{}.jpg".format( t ) )
#         lst.append(img_change)
# for pic in range (lst):
#     pic.save( r"F:\\image_result\\change{}.jpg".format(i) )
            # cv_show( 'ss', img_array )

