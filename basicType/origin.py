import math
lists = input().split()
a = eval(lists[0])
b = eval(lists[1])
c = eval(lists[2])
temp = b**2 - 4 * a * c
if temp >= 0:
    x1 = (-b + math.sqrt(temp)) / 2 * a
    x2 = (-b - math.sqrt(temp)) / 2 * a
    if x1 < x2:
        print("%.2f" % x2, end=" ")
        print("%.2f" % x1)
    else:
        print("%.2f" % x1, end=" ")
        print("%.2f" % x2)
else:
    print("No")