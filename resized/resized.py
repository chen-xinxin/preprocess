# 缩放图片
import os
import torch
from PIL import Image
import torchvision.transforms.functional as TF
import torch.nn.functional as F

# 获取当前文件夹路径
current_dir = os.getcwd()

# 定义输入和输出文件夹路径
source_folder = os.path.join(current_dir, 'source')
output_folder = os.path.join(current_dir, 'output')

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 遍历source文件夹及其子文件夹
for root, dirs, files in os.walk(source_folder):
    # 遍历当前文件夹下的所有文件
    for file in files:
        # 获取文件路径
        file_path = os.path.join(root, file)
        # 获取相对于source文件夹的子文件夹路径
        relative_folder = os.path.relpath(root, source_folder)
        # 创建输出子文件夹路径
        output_subfolder = os.path.join(output_folder, relative_folder)
        # 创建输出子文件夹（如果不存在）
        os.makedirs(output_subfolder, exist_ok=True)
        # 读取输入图片
        input_image = Image.open(file_path)
        # 将输入图片转换为张量
        input_tensor = TF.to_tensor(input_image)
        # 缩小图片尺寸
        output_tensor = F.interpolate(input_tensor.unsqueeze(0), scale_factor=0.5, mode='bilinear')
        # 将输出张量转换为图片
        output_image = TF.to_pil_image(output_tensor.squeeze(0))
        # 保存输出图片
        output_image_path = os.path.join(output_subfolder, file)
        output_image.save(output_image_path)

print("resize finished!!!")

# 提取出名字为a_0_b_1.png(a==b)的图片，也就是paired结果
# import os
# import shutil

# source_folder = "source"  # 源文件夹路径
# result_folder = "result"  # 结果文件夹路径

# # 创建结果文件夹
# os.makedirs(result_folder, exist_ok=True)

# # 获取源文件夹中的所有文件
# files = os.listdir(source_folder)

# # 移动相同 a 和 b 的图片到结果文件夹
# for image_file in files:
#     # 仅处理以 ".png" 结尾的文件
#     if not image_file.endswith(".png"):
#         continue

#     # 解析文件名
#     parts = image_file.split("_")
#     a = parts[0]
#     b = parts[2]

#     # 检查 a 和 b 是否相同
#     if a == b:
#         # 构建完整的旧文件路径
#         old_path = os.path.join(source_folder, image_file)
#         # 构建完整的新文件路径
#         new_path = os.path.join(result_folder, image_file)
#         # 移动图片文件
#         shutil.move(old_path, new_path)


# 将a_0_b_1.png的图片名字重命名为a_0.png
# import os
# import shutil

# source_folder = "source"  # 源文件夹路径
# output_folder = "output"  # 输出文件夹路径

# # 创建输出文件夹
# os.makedirs(output_folder, exist_ok=True)

# # 获取源文件夹中的所有文件
# files = os.listdir(source_folder)

# # 重命名并保存图片
# for image_file in files:
#     # 仅处理以 ".png" 结尾的文件
#     if not image_file.endswith(".png"):
#         continue

#     # 解析文件名
#     parts = image_file.split("_")
#     a = parts[0]
#     b = parts[2]

#     # 构建新的文件名
#     new_file_name = f"{a}_0.png"

#     # 构建完整的旧文件路径
#     old_path = os.path.join(source_folder, image_file)
#     # 构建完整的新文件路径
#     new_path = os.path.join(output_folder, new_file_name)

#     # 重命名并保存图片
#     shutil.copyfile(old_path, new_path)

# png图片转jpg
# import os
# from PIL import Image

# source_folder = "source"  # 源文件夹路径
# output_folder = "output"  # 输出文件夹路径

# # 创建输出文件夹
# os.makedirs(output_folder, exist_ok=True)

# # 获取源文件夹中的所有文件
# files = os.listdir(source_folder)

# # 转换并保存图片
# for file_name in files:
#     # 仅处理以 ".png" 结尾的文件
#     if not file_name.endswith(".png"):
#         continue

#     # 构建完整的文件路径
#     file_path = os.path.join(source_folder, file_name)

#     # 打开 PNG 图片并转换为 JPG 格式
#     image = Image.open(file_path)
#     jpg_file_name = os.path.splitext(file_name)[0] + ".jpg"
#     jpg_file_path = os.path.join(output_folder, jpg_file_name)
#     image.save(jpg_file_path, "JPEG")

#     # 关闭图片
#     image.close()