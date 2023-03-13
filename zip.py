list1 = [4,6,9,10]
list2 = [2,5,6,8,]

list3 =[]

for i in range (len(list1)):
    list3.append(list1[i]+list2[i])

print(list3)

print('--------------------------------')

list4 = list(zip(list1,list2,list3))

print(list4)

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x + y for x, y in zip(L1, L2) if x > 10 and y < 5]

print(L3)
