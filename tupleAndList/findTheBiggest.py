print("How  many numbers are there?", end=" ")
n = int(input())
ls = []
for i in range(0, n):
    print("Enter  a  number  >>", end=" ")
    ls.append(eval(input()))
print("The  largest  value  is %d" % max(ls))