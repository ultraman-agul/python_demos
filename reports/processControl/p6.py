# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 9:36
# Software : PyCharm
# version： Python 3.7
# @File    : p6.py
# description : 任意输入两个正整数，计算其最大公约数和最小公倍数。
lst = input().split()
n = int(lst[0])
m = int(lst[1])
yue = bei = 0
for i in range(2, n+1):
    if n % i == 0 and m % i == 0:
        yue = i
j = m
while j > 0:
    if j % n == 0 and j % m == 0:
        bei = j
        break
    j += 1
print(yue, bei)
