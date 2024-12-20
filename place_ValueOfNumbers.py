def read_positions(number):
    # Extract the digits
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10
    millions = (number // 1000000) % 10

    # Return the results
    return millions,thousands, hundreds, tens, ones


# Example usage:
number = int(input("Enter Number: "))
print("Number",number)
millions,thousands,hundreds, tens, ones = read_positions(number)
print(f"million: {millions},thousand: {thousands}, Hundreds: {hundreds}, Tens: {tens}, Ones: {ones}")

print('---------------------Round the numbers--------------------------')
roundedNumber = round(number, -1) #rounds the number to the nearest 10tenth
print("Rounded to nearest hundred:",roundedNumber)

