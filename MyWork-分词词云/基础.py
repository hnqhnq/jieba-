""" 
@file: 面试题2.py
@Time: 2018/08/23
@Author:heningqiu
"""
# print(sum([1,2,3]))
a=[1,3,2,4,33]
for i in range(0,len(a),2):
    # print(a[i]**2)
    pass

print(sum([a[i]**2 for i in range(0,len(a),2)]))

print("*"*10)
# print([i for i in filter(lambda x:x%2,a)])
# # print([i for i in map(lambda x:x%2,a)])
# print([i for i in map(lambda x:x**2,filter(lambda x:x%2,a))])
# print(sum([i for i in map(lambda x:x**2,filter(lambda x:x%2,a))]))
# print(sum(map(lambda x: x ** 2, filter(lambda x: x % 2, a))))
# print([i%2 for i in a])

print(sum([i**2 for i in filter(lambda x:x%2,a)]))
print(sum(map(lambda x:x**2,filter(lambda x:x%2,a))))

maxtric=[[0]*10 for _ in range(10)]
for i in range(10):
    maxtric[i][i]=1
print(maxtric)

print("*"*10)
for k,v in enumerate(a):
    print(k,v)

# ifor index,v in enumerate(a)
# print(sum([a[i]**2 for i in range(1,len(a),2)]))
# print(sum([val ** 2 for index, val in enumerate(a) if index % 2]))
s=0
for i in range(1,101):
    s+=i
print(s)