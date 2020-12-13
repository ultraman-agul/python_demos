# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/5 15:25
# Software : PyCharm
# version： Python 3.7
# @File    : p2_8.py
# description :（1） 输出表 2.2 和表 2.3 均包含的商品信息
# （2） 输出属于表 2.2，但不属于表 2.3 的商品信息
# （3） 输出属于表 2.2 但不属于表 2.3，或者属于表 2.3 但不属于表 2.2 的商
# 品信息
# （4） 输入商品名称，查询其价格。

dict1 = {
    '苹果': 5.5,
    '香蕉': 4.8,
    '山竹': 12.5,
    '西瓜': 5.6,
    '梨': 4.5
}

dict2 = {
    '山竹': 12.5,
    '梨': 4.5,
    '冬枣': 8.5
}

print(dict1.items() & dict2.items())
print(dict1.items() - dict2.items())
print((dict1.items() | dict2.items()) - (dict1.items() & dict2.items()))
dict3 = dict1.items() | dict2.items()
dict4 = dict(dict3)
print(dict4[input()])
