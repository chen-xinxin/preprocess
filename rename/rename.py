import os
import shutil

folder_path = "cloth"  # 文件夹路径
image_file = "12137_00.jpg"  # 图片文件名
extension = ".jpg"  # 图片扩展名
new_name_prefix = "00"  # 新名称的前缀

# 构建完整的旧文件路径
old_path = os.path.join(folder_path, image_file)

# 复制并重命名图片
for i in range(1, 39):
    # 构建新的文件名
    new_name = f"{i}_{new_name_prefix}{extension}"
    # 构建完整的新文件路径
    new_path = os.path.join(folder_path, new_name)
    # 复制图片
    shutil.copyfile(old_path, new_path)

print('finish!!!')