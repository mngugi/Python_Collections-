
from  itertools import compress

numbers = [1,2,-3,4,5]
selector = [True, False, True, False, True]

filtered = compress(numbers, selector)

print(list(filtered))


