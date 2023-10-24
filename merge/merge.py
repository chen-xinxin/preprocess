import os
from PIL import Image

# 设置人物和背景文件夹路径
human_folder = 'human'
background_folder = 'background'
merge_output_folder = 'merge_output'

# 创建输出文件夹
os.makedirs(merge_output_folder, exist_ok=True)

# 遍历人物文件夹
for filename in os.listdir(human_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 读取人物和背景图像
        human_path = os.path.join(human_folder, filename)
        background_path = os.path.join(background_folder, filename)

        human_image = Image.open(human_path).convert('RGB')
        background_image = Image.open(background_path).convert('RGB')

        # 创建空白图像
        merge_image = Image.new('RGB', background_image.size)

        # 粘贴背景
        merge_image.paste(background_image, (0, 0))

        # 遍历像素，用人物像素替换背景上的白色像素
        for x in range(background_image.width):
            for y in range(background_image.height):
                bg_pixel = background_image.getpixel((x, y))
                human_pixel = human_image.getpixel((x, y))
                if bg_pixel == (255, 255, 255) or human_pixel != (255,255,255): 
                    merge_image.putpixel((x, y), human_pixel)


        # 保存拼接后的图片
        output_path = os.path.join(merge_output_folder, filename)
        merge_image.save(output_path)

        print("Merged:", filename)