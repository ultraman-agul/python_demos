# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/5 10:38
# Software : PyCharm
# version： Python 3.7
# @File    : p2_5.py
# description : （1）建立字典 dict，包含内容是："数学":81, "语文":95, "英语":78, "物理":84,
# "生物":96。 （2）向字典中添加键值对"化学":85。 （3）修改"数学"对应的值为 90。 （4）删除"生物"对应的键值对。
# （5）按顺序打印字典 dict 全部信息，

dict1 = {"数学": 81, "语文": 95, "英语": 78, "物理": 84, "生物": 96}
dict1['化学'] = 85
dict1['数学'] = 90
del dict1['生物']
print(dict1)
for key, value in dict1.items():
    print(key + ": " + str(value))
