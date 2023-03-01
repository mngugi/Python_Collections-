a = {1,2,3,4}
b = {1,3,5,6}

c, *d, e = a | b

print(d)

# a python program that adds two number lists in reverser order 

l1 = [2,4,3]
l2 = [5,6,4]

# reverse the list

l1.reverse()
l2.reverse()


#result = [l1[i]+l2[i] for i in range(len(l1))]
result = [x+y for x,y in zip(l1,l2)]

print(result)