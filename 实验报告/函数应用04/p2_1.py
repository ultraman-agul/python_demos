# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 10:18
# Software : PyCharm
# version： Python 3.7
# @File    : p2_1.py
# description :实现一个函数，可计算 n!，并依次计算 1~20 的阶乘
def factorial(n):
    totalnum = 1
    for i in range(2, n+1):
        totalnum = totalnum * i
    return totalnum
for n in range(1, 21):
    print('{:>2}={}'.format(n, factorial(n)))