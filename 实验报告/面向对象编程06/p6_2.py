# -*- coding: utf-8 -*- 
# @Time : 2020/12/8 0008 19:35 
# @Author : agul
# @File : p6_2.py 
# @description:

class Animal:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def show(self):
        print('我是一只{}的{}'.format(self.type, self.name))
        print('今年{}岁了!'.format(self.age))


class Bird(Animal):
    pass


class Fish(Animal):
    pass


benbird = Bird('鸟', '红色', 2)
benfish = Fish('鱼', '3斤重', 4)
benbird.show()
benfish.show()