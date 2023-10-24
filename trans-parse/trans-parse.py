import numpy as np
from PIL import Image
import os


# trans_dict = {76:2,126:5,95:5,60:9,29:13,140:14,179:15,194:16,226:18,210:17,176:19} #cp-vton
# trans_dict = {76:2,126:5,95:5,55:10,60:9,10:9,29:13,140:14,179:15,194:16,226:18,210:17,176:19} #vton-hd
trans_dict = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,11:11,12:12,13:13,14:14,15:15,16:16,17:17,18:18,19:19}
path = './trans-source/'
save_path = './trans-result/'


for i in os.listdir(path):
    img = Image.open(path+i)
    img = np.array(img)

    parsing_result = img
    output_arr = np.asarray(parsing_result, dtype=np.uint8)
    new_arr = np .full(output_arr .shape, 0)
    for old, new in trans_dict.items():
        new_arr = np.where(output_arr == old, new, new_arr)

    output_img = Image.fromarray(np.asarray(new_arr, dtype=np.uint8)) 
    output_img.save(save_path+i)

print("finished!!!")