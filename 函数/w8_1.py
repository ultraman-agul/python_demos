# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/11 9:58
# Software : PyCharm
# version： Python 3.7
# @File    : w8_1.py
# description : 编写函数itob(n,b),用于把整数n转换成以b为基底的字符串并返回.

def itob(n, b, s):
    flag = False
    if n < 0:
        n = -n
        flag = True
    while (n/b):
        i = n % b
        n = n // b
        if i > 9:
            i = chr(i + 97 - 10)  # 获取对应的字母
        s.append(i)
    return flag

lst = input().split(" ")
lst[0] = int(lst[0])
lst[1] = int(lst[1])
s = []
result = itob(lst[0], lst[1], s)
if result:
    s.append("-")
for item in range(len(s) - 1, -1, -1):
    print(s[item], end="")