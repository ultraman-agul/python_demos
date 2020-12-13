# -*- coding: utf-8 -*- 
# @Time : 2020/12/9 0009 10:55 
# @Author : agul
# @File : p6_5.py 
# @description:

import random


class GameAnimal:
    x = 0
    y = 0
    buchang = 0

    def initLocation(self, name):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        if name == 't':
            print('创建乌龟 初始位置：（{}，{}）'.format(self.x, self.y))
        else:
            print('创建第{}条 初始鱼位置({},{})'.format(name, self.x, self.y))

    def move(self, name):
        if name == 't':
            self.buchang = random.choice([-2, -1, 1, 2])
            xory = random.choice([1, 2])
            if xory == 1:
                self.x += self.buchang
            else:
                self.y += self.buchang
        else:
            buchang = random.choice([-1, 1])
            xory = random.choice([1, 2])
            if xory == 1:
                self.x += buchang
            else:
                self.y += buchang

        if self.x > 10:
            self.x = 10 - (self.x - 10)
        elif self.x < 0:
            self.x = -self.x

        if self.y > 10:
            self.y = 10 - (self.y - 10)
        elif self.y < 0:
            self.y = -self.y


class Tortoise(GameAnimal):
    def __init__(self):
        self.hp = 100
        self.name = 't'

    def eat(self, i):
        if self.x == i.x and self.y == i.y:
            self.hp += 20
            fish.remove(i)
            print('第{}条鱼被吃掉了，其位置（{}，{}），当前乌龟体力：{}'.format(i.name, i.x, i.y, self.hp))

    def show(self):
        print('当前乌龟步长{}，移动后的位置：（{}，{}），当前体力：{}'.format(abs(self.buchang), self.x, self.y, self.hp))


class Fish(GameAnimal):
    def __init__(self, name):
        self.name = name

    def show(self):
        print('第{}条鱼移动后的位置：（{}，{}）'.format(self.name, self.x, self.y))


tor = Tortoise()
tor.initLocation('t')
fish = []
for i in range(1, 11):
    f = Fish(i)
    f.initLocation(i)
    fish.append(f)
while tor.hp > 0 and len(fish) > 0:
    for i in fish:
        i.move(i)
        i.show()
        tor.eat(i)
    tor.move('t')
    tor.hp -= 1
    tor.show()
if tor.hp == 0:
    print('邪恶的大乌龟累死了')
else:
    print('大乌龟拍拍肚子：真不错~~')