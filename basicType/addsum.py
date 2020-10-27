p = int(input())
q = int(input())
lists = []
n = 0
for i in range(1, p+1):
    if i % 2 != 0:
        lists.append(i)
        n += 1
    if sum(lists) >= q:
        break
print(sum(lists))
print(n)
print(max(lists))
