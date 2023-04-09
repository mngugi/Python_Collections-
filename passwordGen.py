import  random

lower = "abcdefghijklmnopqrst"
UPPER = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"
symbols = "[]{}()@#$%&,.-_*"

all = lower+UPPER+numbers+symbols

length = 16

password = "".join(random.sample(all , length))
print(password)
