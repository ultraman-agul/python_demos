list = []
for item in range(0,3):
    list.append(input())
for i in range(0,3):
    for j in range(i,3):
        if(list[j]>list[i]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
for item in list:
    print(item)