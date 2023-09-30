n = 5

if n % 2 == 0:
    print ("n is an even number",n)
else:
    print("n is odd")

print ('First Example')

First = [1,2,3]

for i in range(len(First)):
    print(First[i], end = "\n")

print ("Second Example")

for j in range(0,5):
    print(j, end= "\n")
print('print question answer')
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
print("while loop")
m = 5
x = 0
while x < m :
    print(x, end = "")
    break




