import numpy as np

def create_array():
    return np.arange(5)

def print_array(array):
    print("Array:", array)

# Create and print the original array
original_array = create_array()
print_array(original_array)

# Increment each element by 1
print("\nIncrement by 1")
original_array[0:5] += 1
print_array(original_array)

# Decrement each element by 1
print("\nDecrement by 1")
original_array[0:5] -= 1
print_array(original_array)

# Increment each element by 5
print("\nIncrement by 5")
original_array[0:5] += 5
print_array(original_array)

# Multiply each element by 1 (no change)
print("\nMultiply by 1")
original_array[0:5] *= 1
print_array(original_array)
