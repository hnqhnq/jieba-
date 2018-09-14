""" 
@file: tokenize.py
@Time: 2018/08/27
@Author:heningqiu
"""
import jieba
'''Tokenize：返回词语在原文的起始位置'''
# 默认模式
res=jieba.tokenize('我是中华人民共和国公民，我是人民教师，我的未来的希望')
for tk in res:
    print(tk)

print("**************************************************************")
#搜索模式
result = jieba.tokenize(u'永和服装饰品有限公司',mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))