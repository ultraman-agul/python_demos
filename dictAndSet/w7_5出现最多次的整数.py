# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/3 15:16
# Software : PyCharm
# version： Python 3.7
# @File    : w7_5出现最多次的整数.py
# description : 输入一组无序的整数，编程输出其中出现次数最多的整数及其出现次数。
n = int(input())
lst1 = input().split()
set1 = {}
for i in lst1:
    set1[i] = lst1.count(i)
# print(set1)
lst2 = []
n = max(set1.values())
for key, value in set1.items():
    if(value == n):
        lst2.append(key)
lst2.sort()
for i in lst2:
    print(i+" "+str(n))