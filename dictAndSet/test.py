# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/10/30 14:34
# Software : PyCharm
# version： Python 3.7
# @File    : test.py
# description :

x = [1, 2, 3]
y = x[:]
print(y) #[1, 2, 3]
print(y is x) #False

# x = [1, 2, 3, 4, 5]
# del x[:3]
# print(x)

# print(list(str([1, 2, 3])) == [1, 2, 3]) # False
# print(list(set([1, 2, 3])) == [1, 2, 3])  #True

# x = [[]] * 3
# x[0].append(1)
# print(x)  # [[1], [1], [1]]

# print(True * 3) # 3

# x = '1'
# y = '1'
# print(x+y) # 11

# x = [1, 2]
# x[0:1] = [0,1,2]
# print(x) #[0, 1, 2, 2]
# print(3 not in{(1), (2), (3)}) # False
# print({1,2,3}=={3,2,1})  True