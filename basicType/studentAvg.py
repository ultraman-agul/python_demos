n = int(input())
if n <= 0:
    print("illegal input")
else:
    sums = 0
    for i in range(0, n):
        num = eval(input())
        if 0 < num < 100:
            sums += num
            if i == n-1:
                stuavg = sums / n
                print("%.2f" % stuavg)
        else:
            print("illegal input")
            break