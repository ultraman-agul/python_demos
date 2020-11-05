# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/5 11:09
# Software : PyCharm
# version： Python 3.7
# @File    : p2_7.py
# description :

lst = [['张三', 15, '男', 7, 2, 3.8], ['李四', 16, '女', 8, 1, 4.3]]
lst.append(['王五', 15, '男', 8, 2, 4.2])
lst.insert(0, ['赵六', 17, '女', 8, 1, 3.9])
for i in lst:
    print('{}的信息是：\n{}岁，{}性，{}年级{}班，成绩：{}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))

lst2 = []
for i in lst:
    lst2.append(i[5])
lst2.sort()
for i in lst2:
    print(i, end=' ')