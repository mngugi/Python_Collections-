def read_positions(number):
    # Extract the digits
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10

    # Return the results
    return hundreds, tens, ones


# Example usage:
number = 1234
hundreds, tens, ones = read_positions(number)
print(f"Hundreds: {hundreds}, Tens: {tens}, Ones: {ones}")
