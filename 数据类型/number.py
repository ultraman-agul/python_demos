lists = []
sum1 = 0
sum2 = 0
sums = 0
while True:
    x = int(input())
    if x != 0:
        if x > 0:
            sum1 += 1
            lists.append(x)
        else:
            sum2 += 1
            lists.append(x)
    else:
        break
for item in lists:
    sums += item
avg = sums / len(lists)
print(avg)
print(sum1)
print(sum2)