""" 
@file: test.py
@Time: 2018/08/27
@Author:heningqiu
"""
import os

corpus_path = "语料/train/"  # 未分词分类预料库路径
seg_path = "语料/train_seg/"  # 分词后分类语料库路径
catelist = os.listdir(corpus_path)
print(catelist) # 获取未分词目录下所有子目录

for mydir in catelist:
    class_path = corpus_path + mydir + "/"  # 拼出分类子目录的路径
    seg_dir = seg_path + mydir + "/"  # 拼出分词后预料分类目录
    if not os.path.exists(seg_dir):
        print("没有")
        os.makedirs(seg_dir)
    else:
        print("You")
print(class_path)
print(seg_dir)