ls = []
while True:
    print("Enter a number (<Enter> to quit):", end="")
    n = input()
    if not n:
        break
    ls.append(float(n))
print("The mean is %.6f" % (sum(ls)/len(ls)))
if len(ls) % 2 == 0:
    index = int(len(ls) / 2)
    zhong = (ls[index] + ls[index-1]) / 2
else:
    zhong = ls[len(ls) // 2]
print("The median is %.6f" % zhong)