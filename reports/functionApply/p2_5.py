# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 10:49
# Software : PyCharm
# version： Python 3.7
# @File    : p2_5.py
# description : 定义一个函数完成两个字符串的减法，例如’abcabcde’-‘ab’表示从字符串
# ‘abcabcde’中删除全部的’ab’，结果为’ccde’。字符串的减法表达式从键盘输入。

def handle():
    str1 = input().split("-")
    s1 = str1[0]
    s2 = str1[1][1:-1]
    print(s1.replace(s2, ''))

handle()