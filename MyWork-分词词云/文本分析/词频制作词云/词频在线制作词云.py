""" 
@file: 词频.py
@Time: 2018/08/27
@Author:heningqiu
"""
import jieba.analyse
# 在线制作词云  https://wordart.com/create
path = './数据挖掘测试文本.txt'
file_in = open(path, 'r',encoding='utf-8')
content = file_in.read()

try:
    jieba.analyse.set_stop_words('./stop_words.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for v, n in tags:
        #权重是小数，为了凑整，乘了一万
        # 中间使用 制表符\t 是为了在线录入数据时候 选择csv格式自动添加词
        out_words=v + '\t' + str(int(n * 10000))
        print(out_words)
        with open('./out_词频.txt','a+',encoding='utf-8')as f:
            f.write(out_words+'\n')
finally:
    file_in.close()

