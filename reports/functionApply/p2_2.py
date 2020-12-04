# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 10:25
# Software : PyCharm
# version： Python 3.7
# @File    : p2_2.py
# description : 编写一个递归函数实现 Fibonacci 数列。
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("请输入一个数n="))
print('n={0},fib({0})={1}'.format(n, fib(n)))

# 1 1 2 3 5 8