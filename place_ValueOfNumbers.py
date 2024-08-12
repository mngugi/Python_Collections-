def read_positions(number):
    # Extract the digits
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    thousands = (number // 1000) % 10

    # Return the results
    return thousands, hundreds, tens, ones


# Example usage:
number = 1234
thousands,hundreds, tens, ones = read_positions(number)
print(f"thousand: {thousands},Hundreds: {hundreds}, Tens: {tens}, Ones: {ones}")
