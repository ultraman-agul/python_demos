numList = input().split()
rightList = []
for item in numList:
    for i in range(0, len(item)):
        if item[i] != item[len(item) - i - 1]:
            break
    else:
        rightList.append(item)
for items in rightList:
    print(items, end=" ")
print(len(rightList))