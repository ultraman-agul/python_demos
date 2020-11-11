# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/11 10:34
# Software : PyCharm
# version： Python 3.7
# @File    : w8_2.py
# description :  求整数n以内（含n）的全部亲密数。
# 说明：如果正整数A的全部因子(包括1，不包括A本身)之和
# 等于B；且正整数B的全部因子(包括1，不包括B本身)
# 之和等于A，则将正整数A和B称为亲密数。
# 1不和其他数形成亲密数。

#  统计各个数的因子之和
def everyFactorSum(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total

#  遍历数组，查找因子和相同的数
def compareNum(number):
    a = [0]
    for i in range(1, number):
        a.append(everyFactorSum(i))
    for i in range(1, number):
        for j in range(i + 1, number):
            if a[i] == j and a[j] == i:
                print(i, j)

compareNum(int(input()))