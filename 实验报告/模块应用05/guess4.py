# -*- coding: utf-8 -*- 
# @Time : 2020/12/4 0004 20:39 
# @Author : agul
# @File : guess4.py 
# @description:

import random

def GuessSecret(maxtimes):
    times = 0
    secret = random.randint(0, 100)
    print("———————————————————————————————————————————————————")
    print("————                欢迎参加猜字游戏              ————")
    print("————————————————————————————————————————————————————")
    for i in range(maxts, 0, -1):
        times += 1
        guess = int(input("请输入0~100之间的一个整数："))
        print("你输入的数字是{}".format(guess))
        if guess == secret:
            print("你猜对了，总共猜了{}次".format(times))
            break
        elif guess < secret:
            print("你猜的数字小于正确答案,还有{}次机会".format(i - 1))
        elif guess > secret:
            print("你猜的数字大于正确答案,还有{}次机会".format(i - 1))
    print("game over")

maxts = eval(input('请输入猜数字的最大次数：'))
GuessSecret(maxts)
