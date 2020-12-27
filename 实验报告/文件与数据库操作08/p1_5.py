# -*- coding: utf-8 -*- 
# @Time : 2020/12/27 0027 20:37 
# @Author : agul
# @File : p1_5.py 
# @description:

import sqlite3


conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('create table Student(sno, name, phone, address)')
with open('address.txt', 'r') as f:
    lines = f.readlines()
for i in lines:
    lst = i.replace('\n', '').split(',')
    cur.execute('insert into Student values(?,?,?,?)', (int(lst[0]), lst[1], int(lst[2]), lst[3]))
cur.execute('select * from Student')
print(cur.fetchall())




print('1.显示所有信息\n2.追加信息\n3.删除信息')
while True:
    try:
        choice = int(input('请输入数字1-3选择功能：'))
        if choice < 1 or choice > 3:
            print('请重新输入：')
        else:
            print('您选择了功能%d' % choice)
            if choice == 1:
                cur.execute('select * from Student')
                content = cur.fetchall()
                for i in content:
                    print(i)
            if choice == 2:
                appstr = input('请输入要插入的信息，用逗号隔开，示例：113,zz,34567812,tianjing:')
                lst1 = appstr.split(',')
                cur.execute('insert into Student values(?,?,?,?)', (int(lst1[0]), lst1[1], int(lst1[2]), lst1[3]))
            if choice == 3:
                while True:
                    delno = input('请输入删除学生的学号：')
                    cur.execute('select * from Student where sno = ' + delno)
                    delitem = cur.fetchone()
                    if delitem == None:
                        continue
                    cur.execute('delete from Student where sno = ' + delno)
                    break

    except:
        print('请重新输入')