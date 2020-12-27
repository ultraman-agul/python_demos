# -*- coding: utf-8 -*- 
# @Time : 2020/12/27 0027 17:55 
# @Author : agul
# @File : p1_1.py 
# @description:


def showContent(filename):
    with open(filename, 'r') as f:
        data = f.read()
        print(data)


def writeContent(filename, content):
    with open(filename, 'a') as f:
        f.write('\n' + content)



print('1.显示所有信息\n2.追加信息\n3.删除信息')
while True:
    try:
        choice = int(input('请输入数字1-3选择功能：'))
        if choice < 1 or choice > 3:
            print('请重新输入：')
        else:
            print('您选择了功能%d' % choice)
            if choice == 1:
                showContent('address.txt')
                break
            if choice == 2:
                appstr = input('请输入要插入的信息，用逗号隔开，示例：113,zz,34567812,tianjing:')
                writeContent('address.txt', appstr)
                showContent('address.txt')
                break
            if choice == 3:
                while True:
                    delno = input('请输入删除学生的学号：')
                    with open('address.txt', 'r') as f:
                        lines = f.readlines()
                        flag = False
                        for i in lines:
                            if delno in i:
                                flag = True
                        if flag:
                            with open('address.txt', 'w') as ad:
                                for i in lines:
                                    if delno not in i:
                                        ad.write(i)
                            with open('del_address.txt', 'w') as de:
                                for i in lines:
                                    if delno not in i:
                                        de.write(i)
                            showContent('address.txt')
                            break
                        else:
                            delno = input('当前学号不存在，请重新输入学号：')
    except:
        print('请重新输入')
