# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/29 10:11
# Software : PyCharm
# version： Python 3.7
# @File    : day09.py
# description : @property装饰器

class Person(object):
    __slots__ = ('_name', '_age')
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 getter方法
    @property
    def name(self):
        return self._name

    # 访问器 getter方法
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, newage):
        self._age = newage

    def play(self):
        if(self._age < 18):
            print('%s 正在玩石头' % self._name)
        else:
            print('%s 正在看片' % self._name)

def main():
    person1 = Person('金华', 15)
    person1.play()
    person1.age = 22
    person1.play()
    print(person1.name)


if  __name__ == '__main__':
    main()