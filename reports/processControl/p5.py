# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 9:27
# Software : PyCharm
# version： Python 3.7
# @File    : p5.py
# description :
lst = input().split()
n = int(lst[0])
a = int(lst[1])
sums = 0
t = 0
for i in range(n):
    t = t*10 + a
    sums = sums + t
print(sums)