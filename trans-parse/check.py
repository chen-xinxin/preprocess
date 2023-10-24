import numpy as np
from PIL import Image
import json

# trans_dict = {7:0,5:2,2:5,3:9,6:13,1:14,0:15}
# trans_dict = {0:0,10:0,1:1,2:1,4:2,13:2,5:3,6:3,7:3,9:4,12:4,14:5,15:6,16:7,17:8,18:9,19:10,8:11 ,3:12,11:12}
# trans_dict = {2:2,4:4,5:5,9:9,13:13,14:14,15:15}
# img = Image.open('./2.png')
# img = Image.open('./result/000003_0.png')
# img = np.array(img)
# img = Image.fromarray(np.uint8(img))
# img.save('b.png')
# print(img.shape)
# print(np.max(img))
# print(np.unique(img))
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict.items():
#     new_arr = np.where(output_arr == old, new, new_arr)

# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# print(np.unique(output_img))
# output_img.save('a.png')
#输出numpy数组到文件
# with open('output2.txt', 'w') as file:
#     for row in img:
#         for value in row:
#             file.write(str(value) + ' ')
#         file.write('\n')
# img1 = Image.open('b.png')
# img1 = np.array(img1)
# if np.array_equal(img, img1):
#     print('equal!')



#分析所有标签
img = Image.open('./0020.png')
img = np.array(img)
print(np.unique(img))

trans_dict0 = {0:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict0.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/0.png')

trans_dict2 = {2:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict2.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/2.png')

trans_dict3 = {3:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict3.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/3.png')

trans_dict5 = {5:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict5.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/5.png')

trans_dict6 = {6:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict6.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/6.png')

trans_dict7 = {7:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict7.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/7.png')

trans_dict8 = {8:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict8.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/8.png')

trans_dict9 = {9:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict9.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/9.png')

trans_dict10 = {10:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict10.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/10.png')

trans_dict11 = {11:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict11.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/11.png')

trans_dict12 = {12:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict12.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/12.png')

trans_dict13 = {13:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict13.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/13.png')

trans_dict14 = {14:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict14.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/14.png')

trans_dict15 = {15:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict15.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/15.png')

trans_dict16 = {16:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict16.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/16.png')

trans_dict17 = {17:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict17.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/17.png')

trans_dict18 = {18:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict18.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/18.png')

trans_dict19 = {19:255}
parsing_result = img
output_arr = np.asarray(parsing_result, dtype=np.uint8)
new_arr = np .full(output_arr .shape, 0)
for old, new in trans_dict19.items():
    new_arr = np.where(output_arr == old, new, new_arr)
output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
output_img.save('./check/19.png')


# #分析所有标签
# img = Image.open('./000001_0.png')
# img = np.array(img)
# print(np.unique(img))

# trans_dict0 = {0:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict0.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/0.png')

# trans_dict194 = {194:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict194.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/194.png')

# trans_dict226 = {226:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict226.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/226.png')

# trans_dict38 = {38:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict38.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/38.png')

# trans_dict10 = {10:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict10.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/10.png')

# trans_dict75 = {75:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict75.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/75.png')

# trans_dict76 = {76:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict76.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/76.png')

# trans_dict140 = {140:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict140.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/140.png')

# trans_dict176 = {176:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict176.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/176.png')

# trans_dict81 = {81:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict81.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/81.png')

# trans_dict210 = {210:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict210.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/210.png')

# trans_dict179 = {179:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict179.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/179.png')

# trans_dict55 = {55:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict55.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/55.png')

# trans_dict60 = {60:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict60.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/60.png')

# trans_dict29 = {29:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict29.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/29.png')

# trans_dict126 = {126:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict126.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/126.png')

# trans_dict95 = {95:255}
# parsing_result = img
# output_arr = np.asarray(parsing_result, dtype=np.uint8)
# new_arr = np .full(output_arr .shape, 0)
# for old, new in trans_dict95.items():
#     new_arr = np.where(output_arr == old, new, new_arr)
# output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8))
# output_img.save('./check/95.png')
