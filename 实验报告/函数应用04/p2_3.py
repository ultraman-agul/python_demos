# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 10:40
# Software : PyCharm
# version： Python 3.7
# @File    : p2_3.py
# description :

# 笨方法
def maxnum1(*nums):
    temp = nums[1]
    for i in nums:
        if temp < i:
            temp = i
    return temp
print(maxnum1(-1, 34, -9, 56))
print(maxnum1(1, 4, 6, 95, 3, 78))

# good
def maxnum(*nums):
    return max(nums)
print(maxnum(-1, 34, -9, 56))
print(maxnum(1, 4, 6, 95, 3, 78))