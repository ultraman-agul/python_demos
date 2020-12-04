# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/2 15:40
# Software : PyCharm
# version： Python 3.7
# @File    : w7_4字母计数.py
# description : 输入字符串，输出字符串中出现次数最多的字母及其出现次数。如果有多个字母出现次数一样，则按字符从小到大顺序输出字母及其出现次数。

str1 = input()
set1 = {}
for i in str1:
    set1[i] = str1.count(i)
# print(set1)
lst1 = []
n = max(set1.values())
for key, value in set1.items():
    if(value == n):
        lst1.append(key)
lst1.sort()
for i in lst1:
    print(i+" "+str(n))