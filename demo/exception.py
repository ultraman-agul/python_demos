# -*- coding: utf-8 -*-
# @Time : 2020/12/8 0008 15:09 
# @Author : agul
# @File : exception.py 
# @description:\\

# class A:
#     def __init__(self, id):
#         self.id = id
#         id = 800
#
# a = A(100)
# print(a.id)

# try:
#     n=0
#     n=input("请输入")
#     def mut(n):
#         return n*2
# except:
#     print("cuowu")

# x = 3
# def f():
#     # print(x)
#     x = 5
#     print(x)
# f()

# chs = "|'\'-'|"
# for i in range(6):
#     for ch in chs[i]:
#         print(ch,end='')

# sum = 0
# count = 1
# score = 0
# while True:
#     try:
#         score = input()
#         i = eval(score)
#         sum += i
#     except:
#         print('"{}" is illegal score.'.format(score))
#         count -= 1
#     finally:
#         flag = input()
#         if flag == "n" or flag == "N":
#             print('The average score is {:.2f}.'.format(sum/count))
#             break
#         else:
#             count += 1

# while True:
#     try:
#         n = eval(input())
#         result = 10 / n
#         print(result)
#     except NameError:
#         print("Value Error!")
#     except ZeroDivisionError:
#         print("other exception!")
#     else:
#         print("else is executed!")
#     finally:
#         print("finally is executed!")

