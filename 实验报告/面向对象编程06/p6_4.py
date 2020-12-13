# -*- coding: utf-8 -*- 
# @Time : 2020/12/9 0009 10:42 
# @Author : agul
# @File : p6_4.py 
# @description:

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDistance(self, p):
        return ((self.x - p.getX()) ** 2 + (self.y - p.getY()) ** 2) ** (1 / 2)


point1 = MyPoint(1, 1)
point2 = MyPoint(2, 2)
print(point2.getDistance(point1))