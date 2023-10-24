import numpy as np
from PIL import Image
import os


trans_dict = {0:255}

path = './mask-source/'
save_path = './mask-result/'


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