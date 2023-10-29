import os
dir_path = r'F:\语言通\2019年互联网+创新创业大赛辅导材料'
suffix = '.pdf'  # 替换为实际的后缀
file_paths=[]
def get_paths_from_dir(dir_path, suffix='*'):
    for root, dirs, files in os.walk(dir_path):#root：表示正在遍历的目录路径（字符串）dirs：表示当前目录下的子目录列表（字符串列表）files：表示当前目录下的文件列表（字符串列表
        for file in files:
            if file.endswith(suffix):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)

    return file_paths
file_paths = get_paths_from_dir(dir_path, suffix)

for i in file_paths:
    print(i)
