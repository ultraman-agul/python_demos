# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/4 11:11
# Software : PyCharm
# version： Python 3.7
# @File    : p2_2.py
# description : 、根据输入字符串 s，输出一个宽度为 15 字符，字符串 s 居中显示，以 “=”填充的格式。如果输入字符串超过 15 个字符，则输出字符串前 15 个字符，最终输出其全小写形式

str = input()
if len(str) > 15:
    str1 = str[: 15]
    print(str1.lower())
else:
    print(str.center(15, '='))