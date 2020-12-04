# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/25 10:50
# Software : PyCharm
# version： Python 3.7
# @File    : hongbao.py
# description :拼手气红包，发红包时用户输入一个红包总金额total和待发红包总数num，
# 发布红包后，其它用户抢红包时可以随机得到不定金额的红包（前 num 个人中
# 每个人都能抢到红包），RP 好的可能抢到几块，RP 不好时可能只会抢到几毛，
# 甚至几分钱。请编程实现上面这一个过程，并输出每个人的红包金额数

import random


def hongbao(total, num):
    moneylist = []
    # 已发红包总金额
    doutotal = float(total * 100)
    for i in range(0, num - 1):
        money = random.randint(1, doutotal // num * 2)
        doutotal -= money
        num -= 1
        moneylist.append(money / 100)
    moneylist.append(doutotal / 100)
    return moneylist


def test(total, numb):
    each = hongbao(total, numb)
    print(*each, sep=', ')


if __name__ == '__main__':
    print('请输入红包总金额和红包个数：', end='')
    lst = input().split()
    test(float(lst[0]), int(lst[1]))
