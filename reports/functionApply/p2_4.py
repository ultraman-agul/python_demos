# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 10:43
# Software : PyCharm
# version： Python 3.7
# @File    : p2_4.py
# description :
def isPrime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag:
        print(n, end=" ")

for i in range(1, 101):
    isPrime(i)