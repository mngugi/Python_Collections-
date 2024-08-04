
user_input = input("Eneter Two Numbers: ")

def add_TwoNumbers(i,j):
    return i + j

# split the numbers into 2 parts
numbers = user_input.split()
num1 = int(numbers[0])
num2 = int(numbers[1])


print(add_TwoNumbers(i = num1, j=num2))
