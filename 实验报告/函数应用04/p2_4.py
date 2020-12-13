# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 10:43
# Software : PyCharm
# version： Python 3.7
# @File    : p2_4.py
# description : 定义一个素数判断函数 isPrime(n)，利用该函数输出 100 以内的所有素数。
def isPrime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag:
        print(n, end=" ")

for i in range(1, 100):
    isPrime(i)