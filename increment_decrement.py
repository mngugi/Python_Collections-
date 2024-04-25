import numpy as np
import math
print ("\nArray of :\n")

def arr():
    arr = np.arange(5)
    print(arr)
    return arr
arr()

new_array = arr()
print("\nIncrement by 1\n")
new_array[0:5] +=1
print(new_array)


print("\nIncrement by 1\n")
new_array[0:5] -=1
print(new_array)



print("\nIncrement by 5\n")
new_array[0:5] +=5
print(new_array)


print("\nIncrement by multiplication of 1\n")
new_array[0:5] *=1
print(new_array)

