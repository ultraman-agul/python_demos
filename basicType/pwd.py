pwd = input()
if pwd.isdigit:
    i = 1
    while i < len(pwd):
        if (int(pwd[i-1]) + 1)**3 % 10 != int(pwd[i]):
            print("wrong")
            break
        if i == len(pwd) - 1:
            print("right")
        i += 1
else:
    print("wrong")
