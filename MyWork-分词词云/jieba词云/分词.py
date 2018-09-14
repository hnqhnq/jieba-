""" 
@file: 分词.py
@Time: 2018/08/24
@Author:heningqiu
"""

import jieba

# b="到MI京研大厦"
# c=jieba.cut(b,cut_all=False)
# d=jieba.cut(b,cut_all=False,HMM=False)
# print("/".join(c))
# print("/".join(d))
a="我是云计算的工作人员，是中华人民共和国党员，还是一个非常优秀的程序猿！"
jieba.load_userdict('userdict.txt')
cut=jieba.cut(a,cut_all=False,HMM=True)
print(" ".join(cut))
# for i in cut:
#     print(i)

serchCut = jieba.cut_for_search(a) # 搜索引擎切割方式,带上标点符号
print('/'.join(serchCut))