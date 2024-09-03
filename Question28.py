num = 5


if (num == 5):
    num += 1
    print("1")

    if num == 6:
        print("2")

else:
    print("3")            


print('---------------')

i = 0
while i < 5:
    print(i, end= "")
    i += 1
    if i == 3:
        break
    else:
        print(0,'\n')    