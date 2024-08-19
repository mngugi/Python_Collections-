# Function to check divisibility and print checkmark
def check_divisibility(number):
    # Divisibility checks
    divisors = [2, 3, 4, 5, 6, 9, 10]
    results = {}

    for divisor in divisors:
        if number % divisor == 0:
            results[divisor] = "✔"
        else:
            results[divisor] = "✘"

    # Print results
    print(f"Number: {number}")
    for divisor in divisors:
        print(f"Divisible by {divisor}: {results[divisor]}")


# Example usage
number = int(input("Enter a number: "))
check_divisibility(number)
