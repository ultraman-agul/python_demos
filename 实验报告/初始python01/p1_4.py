# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/28 10:24
# Software : PyCharm
# version： Python 3.7
# @File    : p1_4.py
# description : 输入一个自然数，输出它的二进制、八进制、十六进制表示形式。
while True:
    n = input()
    if not n:
        break
    n = int(n)
    print("二进制：" + format(n, 'b'), "八进制：" + format(n, 'o'), "十六进制：" + format(n, 'x'))