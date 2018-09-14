""" 
@file: 去除停用词.py
@Time: 2018/08/27
@Author:heningqiu
"""
import jieba
def read_from_file(file_name):
    with open(file_name,"r") as fp:
        words = fp.read()
    return words
def stop_words(stop_word_file):
    words = read_from_file(stop_word_file)
    result = jieba.cut(words)
    new_words = []
    for r in result:
        new_words.append(r)
    return set(new_words)
def del_stop_words(words,stop_words_set):
#   words是已经切词但是没有去除停用词的文档。
#   返回的会是去除停用词后的文档
    result = jieba.cut(words)
    new_words = []
    for r in result:
        if r not in stop_words_set:
            new_words.append(r)
    return new_words