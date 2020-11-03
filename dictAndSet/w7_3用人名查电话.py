# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/30 15:57
# Software : PyCharm
# version： Python 3.7
# @File    : w7_3用人名查电话.py
# description :现在输入人名，查询他的号码。
teltext = {
    'mayun': '13309283335',

    'zhaolong': '18989227822',

    'zhangmin': '13382398921',

    'Gorge': '19833824743',

    'Jordan': '18807317878',

    'Curry': '15093488129',

    'Wade': '19282937665'
}

test = input()
print(teltext.setdefault(test, "not found"))