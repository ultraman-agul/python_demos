list1 = []
str = input()
list2 = str.split(' ')
for item in list2:
    list1.append(item.capitalize())
print(' '.join(list1))
