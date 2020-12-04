# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 9:13
# Software : PyCharm
# version： Python 3.7
# @File    : p4.py
# description :
n = int(input())
if n % 2 != 0:
    str = "*"
    print(str.center(n, ' '))
    for i in range(1, int(n/2)+1):
        str = str + "**"
        print(str.center(n, ' '))
    for j in range(int(n/2), 0, -1):
        str = str[0:-2]
        print(str.center(n, ' '))
else:
    print("请输入奇数")