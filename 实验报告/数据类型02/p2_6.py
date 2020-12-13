# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/5 10:50
# Software : PyCharm
# version： Python 3.7
# @File    : p2_6.py
# description : 利用元组创建一个存储 Python 关键字的对象，并检测给定的单词是否是
# Python 关键字。（使用 help(“keywords”)查看系统所有关键字）
tuple1 = ("False", "class", "from", "or", "None", "continue", "global", "pass", "True", "def", "if",
          "raise", "and", "del", "import", "return", "as", "elif", "in", "try", "assert", "else", "is",
          "while", "async", "except", "lambda", "with", "await", "finally", "nonlocal", "yield", "break", "for", "not")
while True:
    print(input() in tuple1)
