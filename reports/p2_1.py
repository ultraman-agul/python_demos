# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/4 10:28
# Software : PyCharm
# version： Python 3.7
# @File    : p2_1.py
# description :

# # （1）元组创建、删除与排序操作；
# tup = ('hello', 'boy', 12, 'man')
# tup1 = ()  # 空元组
# tup2 = (21,)  # 一个元素的元组需要加上逗号
# tup3 = (12, 4, 25, 2, 5)
# print(type(tup))  # <class 'tuple'>
# print(tup)   # ('hello', 'boy', 12, 'man')
# del tup
# # print(tup)  # NameError: name 'tup' is not defined
# L = list(tup3)
# L.sort()
# T = tuple(L)
# print(T)  # (2, 4, 5, 12, 25)


# （2）序列的创建、增加、删除、计数、排序操作；
# lst1 = ['hello', 'boy', 12, 'man']
# lst2 = [2, 4, 51, 25, 46, 23, 2]
# lst1.append(12)
# lst1.extend(['user', 24])
# lst1.remove('boy')
# print(lst1.pop())  # 24
# del lst1[2]
# print(lst1)   # ['hello', 12, 12, 'user']
# print(lst2.count(2))  # 2
# lst2.sort()
# print(lst2)  # [2, 2, 4, 23, 25, 46, 51]


# # （3）字典的创建、删除、读取、修改操作；
# dict1 = {
#     'name': "潘金华",
#     'sex': '男',
#     'age': 18
# }
# print(dict1['age'])  # 18
# dict1['age'] = 20
# print(dict1)  # {'name': '潘金华', 'sex': '男', 'age': 20}
# del dict1['name']
# print(dict1)  # {'sex': '男', 'age': 20}
# dict1.clear()
# print(dict1)  # {}
# del dict1
# print(dict1)   #  NameError: name 'dict1' is not defined


# （4）集合的创建、删除、操作；
colorSet = {'red', 'blue', 'pink', 'orange', 'black', 'pink'}
print(colorSet)  # 去重 {'red', 'orange', 'black', 'blue', 'pink'}
colorSet.add('white')
print(colorSet)  # {'red', 'orange', 'white', 'black', 'blue', 'pink'}
colorSet.remove('blue')
colorSet.discard('pink')
print(colorSet)  # {'red', 'orange', 'white', 'black'}