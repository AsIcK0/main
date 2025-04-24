list1 = []
for i in range(14):
    list1.append(int(input()))
sumlist = sum(list1)
list1.append(sumlist)
for i in range(15):
    print(list1[i])