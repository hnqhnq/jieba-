""" 
@file: 构建词袋空间VSM.py
@Time: 2018/08/27
@Author:heningqiu
"""
import os

import numpy as np
from numpy import random

from 文本分析.文本聚类.去除停用词 import del_stop_words

def get_all_vector(file_path,stop_words_set):
    names = [ os.path.join(file_path,f) for f in os.listdir(file_path) ]
    # print('names',names)
    posts = [ open(name,encoding='utf-8').read() for name in names ]
    docs = []
    word_set = set()
    for post in posts:
        doc = del_stop_words(post,stop_words_set)
        docs.append(doc)
        word_set |= set(doc)
        #print len(doc),len(word_set)

    word_set = list(word_set)
    docs_vsm = []
    #for word in word_set[:30]:
        #print word.encode("utf-8"),
    for doc in docs:
        temp_vector = []
        for word in word_set:
            temp_vector.append(doc.count(word) * 1.0)
        #print temp_vector[-30:-1]
        docs_vsm.append(temp_vector)

    docs_matrix = np.array(docs_vsm)
    # print(docs_matrix)

# 将单词出现的次数转化为权值（TF-IDF）--------------------------------
    column_sum = [float(len(np.nonzero(docs_matrix[:, i])[0])) for i in range(docs_matrix.shape[1])]
    column_sum = np.array(column_sum)
    column_sum = docs_matrix.shape[0] / column_sum
    idf = np.log(column_sum)
    idf = np.diag(idf)
    # 请仔细想想，根绝IDF的定义，计算词的IDF并不依赖于某个文档，所以我们提前计算好。
    # 注意一下计算都是矩阵运算，不是单个变量的运算。
    for doc_v in docs_matrix:
        if doc_v.sum() == 0:
            doc_v = doc_v / 1
        else:
            doc_v = doc_v / (doc_v.sum())
        tfidf = np.dot(docs_matrix, idf)
        # print('names--\n',names)
        # print('tfidf--\n',tfidf)
        return names, tfidf

#使用K-Means算法进行聚类-----------------
def gen_sim(A,B):
    num = float(np.dot(A,B.T))
    denum = np.linalg.norm(A) * np.linalg.norm(B)
    if denum == 0:
        denum = 1
    cosn = num / denum
    sim = 0.5 + 0.5 * cosn
    return sim
def randCent(dataSet, k):
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k, n)))#create centroid mat
    for j in range(n):#create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = np.mat(minJ + rangeJ * random.rand(k, 1))
    return centroids

def kMeans(dataSet, k, distMeas=gen_sim, createCent=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m, 2)))#create mat to assign data points
                                      #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    counter = 0
    while counter <= 50:
        counter += 1
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        #print centroids
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0].A == cent)[0]]#get all the point in this cluster
            centroids[cent,:] = np.mean(ptsInClust, axis=0) #assign centroid to mean
    return centroids, clusterAssment


if __name__ == '__main__':
    file_path = './pos/'
    stop_words_set = './stop_words'
    print(get_all_vector(file_path,stop_words_set)[1])
    tf_idf=get_all_vector(file_path,stop_words_set)[1]

    # gen_sim()
    # randCent()
    print("**********************")
    print(kMeans(dataSet=tf_idf,k=2,distMeas=gen_sim,createCent=randCent)[0])
    print("**********************")
    print(kMeans(dataSet=tf_idf,k=2,distMeas=gen_sim,createCent=randCent)[1])
