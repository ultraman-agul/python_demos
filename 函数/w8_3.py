# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/11 10:43
# Software : PyCharm
# version： Python 3.7
# @File    : w8_3.py
# description :【问题描述】有一个定义在自然数上的函数 f(x) 定义如下：
#                 若 x <5 , 则 f(x) = x;
#                 若 5<=x<15, 则 f(x) = x+6;
#                 若 x>=15, 则 f(x) = x-6。
#             试编写该函数，输入x值，返回相应的f(x)值。
# 【输入形式】输入的一行表示自然数x。
# 【输出形式】输出的一行表示计算结果f(x)，若输入的数据不合法（如：负整数），输出“illegal input”。
# 【样例输入】4
# 【样例输出】4


def f(x):
    if x < 15:
        if x < 5:
            print(x, end=" ")
        else:
            print(x + 6, end=" ")
    else:
        print(x - 6, end=" ")

s = input().split(" ")
for i in s:
    if int(i) < 0:
        print("illegal input")
        break
    f(int(i))
