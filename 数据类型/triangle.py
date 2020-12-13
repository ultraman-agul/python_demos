n = int(input())
str = "*"
for i in range(0, n):
    print(str.center(2*n-1, " "))
    str = str + "**"