n = int(input())
sums = 0
geshu = 0
if(n >= 0):
    ls = []
    for i in range(0, n):
        ls.append(int(input()))
    for i in ls:
        sums += i
    for i in ls:
        if i >= sums / n:
            geshu += 1
    print(geshu)
else:
    print("illegal input")
