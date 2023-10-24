# 获取test_pairs_unpaired.txt中出现的人像图片
import os
import shutil

# 获取当前文件夹路径
current_dir = os.getcwd()

# 定义输入文件路径
input_file = os.path.join(current_dir, 'test_pairs_unpaired.txt')

# 定义输出文件夹路径
output_folder = os.path.join(current_dir, 'get_test_image')

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 读取输入文件
with open(input_file, 'r') as file:
    lines = file.readlines()

# 遍历输入文件中的每一行
for line in lines:
    # 获取文件名
    filename = line.strip().split()[0]
    
    # 在当前文件夹及其子文件夹中查找同名图片
    for root, dirs, files in os.walk(current_dir):
        if filename.replace('jpg','png') in files:
            # 获取图片路径
            image_path = os.path.join(root, filename.replace('jpg','png'))
            # 复制图片到输出文件夹
            try:
                shutil.copy(image_path, output_folder)
            except shutil.SameFileError:
                pass
print("Finished")