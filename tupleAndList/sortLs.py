n = int(input())
ls = input().split()
lsls = []
for i in ls:
    lsls.append(int(i))
lsls.sort()
for i in lsls:
    print(i, end=" ")