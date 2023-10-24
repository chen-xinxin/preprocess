### 一些处理数据的小程序

#### trans-parse：

`trans-parse.py`：去掉脖子标签，生成cp-vton可用的分析图

`trans-mask.py`：将mask转换为只有0和255

`processdata.py`：24位图片转8位

`all_label.py`：检查数据集出现过的所有标签

`check.py`：检查分析图，依次将各个标签变成全白，其他标签变成全黑，输出在check文件夹中

#### resized：

`resized.py`：

1. 缩放图片
2. 提取出名字为a_0_b_1.png(a==b)的图片，也就是paired结果
3. 将a_0_b_1.png的图片名字重命名为a_0.png
4. png图片转jpg

`get_test_image.py`：获取test_pairs_unpaired.txt中出现的人像图片，保存在`get_test_image`文件夹中

#### rename：

`rename.py`：生成N张相同的图片，命名为0001.jpg、0002.jpg……

#### remove_background：

`remove_background.py`：读取image文件夹的图片和parse文件夹对应的分析图，根据分析图提取人物和背景

#### merge：

`merge.py`：合并人物和背景