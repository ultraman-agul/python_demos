# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 8:30
# Software : PyCharm
# version： Python 3.7
# @File    : p1_2.py
# description :

lst = input().split()
a = eval(lst[0])
b = eval(lst[1])
c = eval(lst[2])
if a == 0 and b ==0:
    print("无解")
elif a == 0 and b != 0:
    print("有一个实根：x={0}", -c/b)
else:
    deta = b**2 - 4*a*c
    if deta == 0:
        print("有两个相等的实根:x1=x2={0}".format(-b/(2*a)))
    elif deta > 0:
        print("有两个不等实根：{0}，{1}".format(-b/(2*a)+deta**(1/2)/(2*a), -b/(2*a)-deta**(1/2)/(2*a)))
    else:
        n = complex(-b/(2*a), deta**(1/2)/(2*a))
        m = complex(-b/(2*a), -deta**(1/2)/(2*a))
        print("有两个共轭复根：{0},{1}".format(n, m))
