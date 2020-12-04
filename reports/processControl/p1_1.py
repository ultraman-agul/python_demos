# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 8:15
# Software : PyCharm
# version： Python 3.7
# @File    : p1_1.py
# description :
# 一句单分支
# x = eval(input())
# if x < 0:
#     print(-x / (x**2 + 1))
#     exit()
# print(x ** (1/2))

# 两句单分支
# x = eval(input())
# if x < 0:
#     print(-x / (x**2 + 1))
# if x >= 0:
#     print(x ** (1/2))

# 双分支结构
# x = eval(input())
# if x < 0:
#     print(-x / (x**2 + 1))
# else:
#     print(x ** (1/2))

# 条件运算符
x = eval(input())
print(-x / (x**2 + 1)) if x < 0 else print(x ** (1/2))