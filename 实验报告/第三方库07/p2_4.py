# -*- coding: utf-8 -*- 
# @Time : 2020/12/13 0013 13:38 
# @Author : agul
# @File : p2_4.py 
# @description:
from turtle import *

lst = ['blue', 'black', 'red', 'yellow', 'green']
width(5)
penup()
fd(-200)
pendown()
for i in range(5):
    pencolor(lst[i])
    if i== 3:
        penup()
        fd(-275)
        right(90)
        fd(55)
        left(90)
        pendown()
    circle(50)
    penup()
    fd(110)
    pendown()
done()
