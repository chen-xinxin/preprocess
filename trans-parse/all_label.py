import os
import numpy as np
from PIL import Image

# 源文件夹路径
source_folder = 'trans-source'

# 获取源文件夹下的所有文件
file_list = os.listdir(source_folder)

# 存储所有标签的集合
all_labels = set()

# 遍历每张分析图像
for file_name in file_list:
    # 构建分析图像文件的完整路径
    file_path = os.path.join(source_folder, file_name)
    
    # 读取分析图像
    img = np.array(Image.open(file_path))
    
    # 获取分析图像中的唯一标签
    labels = np.unique(img)
    if 11 in labels:
        print(file_path)
    # 将当前图像的标签添加到所有标签的集合中
    all_labels.update(labels)

# 打印所有出现过的标签
print("所有出现过的标签：")
for label in all_labels:
    print(label)