# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/28 10:56
# Software : PyCharm
# version： Python 3.7
# @File    : p1_1.py
# description : 输入三角形的三条边，用海伦公式计算三角形的面积s

import math
a = eval(input("请输入a边长:"))
b = eval(input("请输入b边长:"))
c = eval(input("请输入c边长:"))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("三角形的面积是：{:.2f}".format(s))
