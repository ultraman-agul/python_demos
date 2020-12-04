# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/24 14:54
# Software : PyCharm
# version： Python 3.7
# @File    : classUse.py
# description :

# class Animal:
#     data = 100
#
# cat = Animal()
# print(cat.data)



# class test:
#    __x=1
# a=test()
#
# # a.__x=100
# # test.__x=100
# # print(test.__x)
# print(test._test__x)

# class test:
#   def mul(c, a, b):
#      return a+b
# x=test()
# print(x.mul(2, 3))

# class test:
#    x=0
# a=test()
# test.x=10
# print(a.x)


# class A:
#   def fun1(self):
#     print("fun1 A")
#   def fun2(self):
#     print("fun2 A")
# class B(A):
#   def fun1(self):
#     print("fun1 B")
#   def fun3(self):
#     print("fun2 B")
# b=B()
# b.fun1()
# b.fun2()
# a=A()
# a.fun1()
# a.fun2()


# class t1: a=0
# class t2(t1):pass
# t1.a=10
# x=t1()
# x.a=20
# y=t2()
# print(y.a)

# class A, B: pass
#
# class SuperStar(): pass


# class test:
#     __data = 0
#
#
# a = test()
# a.__data = 10
# a._test__data = 20
# test.__data = 30
# print(test._test__data)

# class test:
#     def __init__(self):
#         self.name = "None"
#         self.age = 0
#
# x=test()
# print(x.name, x.age)

# class test:
#     @classmethod
#     def mul(self, a, b):
#         return a * b
# x=test()
# print(x.mul(2, 3), test.mul(4, 5))


class test:
    def show(self):
        print(self.data)

x=test()
x.data=input()
x.show()