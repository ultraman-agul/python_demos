# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/28 10:32
# Software : PyCharm
# version： Python 3.7
# @File    : p1_7.py
# description : 计算圆锥体体积
from math import pi
while True:
    print("输入半径和高（空格间隔）")
    lst = input().split()
    r = eval(lst[0])
    h = eval(lst[1])
    if r <= 0 or h <= 0:
        print("半径和高不能小于等于0")
        break
    V = pi*r*r*h/3
    print("圆锥体体积为：%.2f" % V)
