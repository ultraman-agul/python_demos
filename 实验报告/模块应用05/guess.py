# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/12/2 11:13
# Software : PyCharm
# version： Python 3.7
# @File    : guess.py
# description :猜数字游戏。在程序中预设一个 0-9 之间的整数，让用户通过键盘输入
# 所猜的数，如果大于预设的数，显示“你猜的数字大于正确答案”；小于预设的
# 数，显示“你猜的数字小于正确答案”，如此循环，直至猜中该数，显示“你猜
# 了 N 次，猜对了，真厉害”,其中 N 是用户输入数字的次数。
guess = 0
times = 0
secret = 7
print("—————————————————————欢迎参加猜字游戏——————————————————")
while guess != secret:
    times += 1
    guess = int(input("请输入1~9之间的一个整数："))
    print("你输入的数字是{}".format(guess))
    if guess == secret:
        print("你猜对了，总共猜了{}次".format(times))
    elif guess < secret:
        print("你猜的数字小于正确答案")
    elif guess > secret:
        print("你猜的数字大于正确答案")
print("game over")
