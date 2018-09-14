""" 
@file: py_spark.py
@Time: 2018/08/21
@Author:heningqiu
"""
import pyspark
from pyspark import SparkContext
import os
os.environ['JAVA_HOME']='D:\jdk'
sc=SparkContext('local')
old=sc.parallelize([1,2,3,4,5],2)
newMap=old.map(lambda x:(x,x**2))
newReduce=old.reduce(lambda a,b:a+b)
print(newMap.glom().collect())
print(newReduce)
