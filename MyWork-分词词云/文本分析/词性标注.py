""" 
@file: 词性标注.py
@Time: 2018/08/27
@Author:heningqiu
"""
import jieba.posseg as pesg
text='我爱北京天安门'
words=pesg.cut(text)
for w,flag in words:
    print(w,flag)

