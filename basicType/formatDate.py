s = input()
num = int(input())
strList = input().split('/')

for i in range(0, num):
    print(s, end='')

print('\n')
print(strList[0] + '年' + strList[1] + '月' + strList[2] + '日')
print()
for i in range(0, num):
    print(s, end='')
