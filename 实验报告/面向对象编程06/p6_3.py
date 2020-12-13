# -*- coding: utf-8 -*- 
# @Time : 2020/12/9 0009 10:19 
# @Author : agul
# @File : p6_3.py 
# @description:

class Student:
    def input(self, a, b, c):
        self.total = a + b + c
        self.avg = self.total / 3


    def output(self):
        print('总分：{},平均分：{}'.format(self.total, self.avg))


s1 = Student()
s1.input(93, 94, 95)
s1.output()