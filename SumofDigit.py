def number_sum(number):
    total = 0
    number = abs(number)

    while number > 0:
        total += number % 10
        number //= 10

    return total
number = int(input("Enter a number: "))
result = number_sum(number)

print(f" The Sum of the digits of {number} is {result}.")
