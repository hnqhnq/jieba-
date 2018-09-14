""" 
@file: 制作词云.py
@Time: 2018/08/24
@Author:heningqiu
"""
import jieba
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
# from pyecharts import WordCloud

from wordcloud import WordCloud, STOPWORDS  # 词云

info=open('./pythonworkinfo.txt','r',encoding='utf-8',errors='ignore').read()
cutinfo=jieba.cut(info,cut_all=True)
info=' '.join(cutinfo)
# print(info)
bgcolor=np.array(Image.open('./pq.jpg'))
# print(bgcolor)
word_Cloud=WordCloud(font_path='simkai.ttf', width=400, height=200, margin=2,
                   mask=bgcolor, scale=1,max_words=200, min_font_size=4,
                 stopwords=STOPWORDS, random_state=None, background_color='white',
                 max_font_size=200, ).generate(info)
plt.figimage(word_Cloud)
plt.show()

