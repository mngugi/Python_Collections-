def sum(bum):
    if bum == 1 :
        return 1

    return bum + sum(bum - 1 )
print(bum(4))
