# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/28 10:29
# Software : PyCharm
# version： Python 3.7
# @File    : p1_6.py
# description : 将温度从华氏温度转换为摄氏温度。转换公式为 C=5/9*(F-32)

F = eval(input())
C = 5 / 9 * (F - 32)
print("摄氏温度为：%.2f" % C)