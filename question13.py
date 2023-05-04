i = lambda i: (i, print('x'))
j = lambda i: i

w = lambda n: (n(0), n(1))

result = f"{(j(1) in i(1))}, {(w(i) == w(j))}"
print(result)
