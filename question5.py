x = 5
y = 10

x= (x > 10 or y > 5)
y = not (x > 10 or y > 5)
z = (x and y)

print(z.__or__(y))
