# -*- coding: utf-8 -*- 
# @Time : 2020/12/8 0008 19:15 
# @Author : agul
# @File : p6_1.py 
# @description:

class Dog:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def bark(self):
        print('wang！wang!')

    def show(self):
        print('一只重{}的{}{}在wang！wang！叫'.format(self.weight, self.color, self.name))


dog = Dog('旺财', '黄色', 10)
dog.show()