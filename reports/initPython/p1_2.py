# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/28 11:06
# Software : PyCharm
# version： Python 3.7
# @File    : p1_2.py
# description : 输入三角形的三条边，用海伦公式计算三角形的面积，并且对输入数据进行异常处理

import math
try:
    a = eval(input("请输入a的边长："))
    b = eval(input("请输入b的边长："))
    c = eval(input("请输入c的边长："))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("三角形的面积是：{:.2f}".format(s))
except NameError:
    print("请输入正数数值")
