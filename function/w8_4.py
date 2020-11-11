# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/11 10:53
# Software : PyCharm
# version： Python 3.7
# @File    : w8_4.py
# description :编写与字符串对象的find方法功能相似的函数find(srcString, substring, start, end)，
# 作用是在srcString串的下标start到下标end之间的片段中寻找subString串的所有出现。
# 如果有多处出现，各下标位置用西文逗号','隔开。如果一次都没有出现，则输出"none"。
str1 = input().split(" ")
srcString = str1[0]
subString = str1[1]
start = int(str1[2])
end = int(str1[3])

def f1(srcString, subString, start, end):
    srcString = srcString[start:end]
    if subString not in srcString:
        print("none")
    else:
        lst = []
        for i in range(len(srcString)):
            if srcString[i:i+len(subString)] == subString:
                lst.append(i)
        print(",".join(str(i) for i in lst))

f1(srcString, subString, start, end)
