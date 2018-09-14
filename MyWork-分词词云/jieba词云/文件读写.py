""" 
@file: 文件读写.py
@Time: 2018/08/24
@Author:heningqiu
"""

with open(file='./userdict.txt',mode='r',encoding='utf-8') as f:
    read=f.readlines()

for line in read:
    str=line.replace('\t',' ').rstrip()
    with open('./userdict.txt','a+',encoding='utf-8')as f1:
        # print(1)
        f1.write(str+'\n')

