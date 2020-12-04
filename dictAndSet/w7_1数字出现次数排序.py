# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/30 14:59
# Software : PyCharm
# version： Python 3.7
# @File    : w7_1数字出现次数排序.py
# description : 给定n个整数，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出。
# 【输入形式】
# 第一行包含一个整数n，表示给定数字的个数; 第二行包含n个整数，相邻的整数之间用一个空格分隔，表示所给定的整数。
# 【输出形式】
# 输出有多行，每行包含两个整数，分别表示一个给定的整数和它出现的次数。按出现次数递减的顺序输出。如果两个整数出现的次数一样多，则先输出值较小的，然后输出值较大的。

n = int(input())
list1 = list(map(int, input().split()))
set1 = set(list1)
list2 = list(set1)
dict1 = dict()
for i in range(len(list2)):
    dict1[(list2[i])] = (list1.count(list2[i]))
dict2 = dict(sorted(dict1.items(),key=lambda d: (-d[1], d[0]),reverse = False))
for i in dict2.keys():
    print(str(i) + " " + str(dict2[i]))

