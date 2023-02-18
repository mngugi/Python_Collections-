data = [2,3,5,7,11,13,17,19,23,29,31]
# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print(nines)
x_values = [i for i in range(12)]
print('code uses a list comprehension to generate the list of x values that\n' 
      'satisfy the equation 9x = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99].',x_values)
