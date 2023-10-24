import os
from PIL import Image
import numpy as np

# 设置文件夹路径
image_folder = 'image'
parse_folder = 'parse'
output_folder = 'output'

# 创建输出文件夹
output_human_folder = os.path.join(output_folder, 'background')
output_background_folder = os.path.join(output_folder, 'human')
os.makedirs(output_human_folder, exist_ok=True)
os.makedirs(output_background_folder, exist_ok=True)

# 遍历图像文件夹
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 读取人像图片和对应分析图
        image_path = os.path.join(image_folder, filename)
        parse_path = os.path.join(parse_folder, filename.replace("jpg","png"))

        image = Image.open(image_path)
        parse = Image.open(parse_path)

        # 将图像和分析图转换为 NumPy 数组
        image_array = np.array(image)
        parse_array = np.array(parse)

        # 创建空白图像
        human_image = Image.new('RGB', image.size, (255, 255, 255))
        background_image = Image.new('RGB', image.size, (255, 255, 255))

        # 提取人物和背景
        human_pixels = np.where(parse_array != 0)
        background_pixels = np.where(parse_array == 0)

        # 将标签为0的像素变成全白
        human_image_array = np.array(human_image)
        human_image_array[background_pixels] = image_array[background_pixels]
        human_image = Image.fromarray(human_image_array)

        # 将标签不为0的像素变成全白
        background_image_array = np.array(background_image)
        background_image_array[human_pixels] = image_array[human_pixels]
        background_image = Image.fromarray(background_image_array)

        # 保存提取后的图像
        human_output_path = os.path.join(output_human_folder, filename)
        background_output_path = os.path.join(output_background_folder, filename)
        human_image.save(human_output_path)
        background_image.save(background_output_path)

        print("Processed:", filename)

print("finished!!!")