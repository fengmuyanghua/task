import cv2
import numpy as np

import os
dir_path = r"F:\2task\dataset\dataset\train\image"
suffix = '.jpg'  # 替换为实际的后缀
file_paths=[]

def get_paths_from_dir(dir_path, suffix='*'):
    for root, dirs, files in os.walk(dir_path):
        #root：表示正在遍历的目录路径（字符串）dirs：表示当前目录下的子目录列表（字符串列表）files：表示当前目录下的文件列表（字符串列表
        for file in files:
            if file.endswith(suffix):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
                # print(root,":",dirs,":",file)
                # print(dirs)

    return file_paths
file_paths = get_paths_from_dir(dir_path, suffix)
mean_value=0
variance=0
std=0
for file_path in file_paths:
# 加载图像
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    mean_value =+ np.mean(image)#该函数接受一个图像作为输入，并返回每个通道的均值。

# 计算图像的方差
    variance =+ np.var(image)
    std=+np.std(image)
print("长度：",len(file_paths))
print( "均值:", mean_value)
print("方差:", variance)
print( "标准差:", std)
print( "平均均值:", mean_value / len( file_paths ) )
print("平均方差:", variance/len(file_paths))
print("平均标准差:", std/len(file_paths))
#图像的均值表示图像整体的亮暗程度，图像的均值越大图像整体越亮。
# 标准方差表示图像中明暗变化的对比程度，标准差越大表示图像中明暗变化越明显。
# 计算方差的方法是对每个像素的值与平均值之差的平方进行求和，然后除以像素总数。
#标准差是方差的平方根
#方差和标准差是统计量，用于衡量数据的分散程度。在图像处理中，可以使用它们来描述图像像素值的变化程度。