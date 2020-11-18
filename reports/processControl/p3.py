# -*- coding: utf-8 -*-
# @Author  : agul
# @Date    : 2020/11/18 8:50
# Software : PyCharm
# version： Python 3.7
# @File    : p3.py
# description :
print("请输入身高（米）和体重（公斤）【逗号隔开】：")
lst = input().split()
h = eval(lst[0])
w = eval(lst[1])
bmi = w/(h**2)
print("BMI指数为：%.2f" % bmi)
if bmi < 18.5:
    s1 = s2 = "偏瘦"
elif 18.5 < bmi < 25:
    s1 = "正常"
elif 25 < bmi < 30:
    s1 = "偏胖"
else:
    s1 = "肥胖"

if 18.5 < bmi < 24:
    s2 = "正常"
elif 24 < bmi < 28:
    s2 = "偏胖"
elif bmi > 28:
    s2 = "肥胖"
print("BMI指标为：{}，{}".format(s1, s2))