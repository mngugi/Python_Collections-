nums = [2, 7, 11, 15, 9]
nums2 = [1, 2, 3, 4, 6,5]

# Find the target value by adding the first elements of both lists
target = nums[0] + nums2[2]
print("Target value:", target)

# Check if the target value is present in the nums list
if target not in nums:
    print("Target value not found in nums")
else:
    # Find the index position of the target value in the nums list
    index = nums.index(target)
    print("Index position of target value:", index)

    # Iterate over all pairs of elements in the nums list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Check if the sum of the pair is equal to the target value
            if nums[i] + nums[j] == target:
                # Print the index positions of the pair
                print("Index positions of pair:", i, j)
'''
nums = [2, 7, 11, 15]
target = nums[0] + nums[1]
print(target)

# Find the index position of target value in the nums list
index = nums.index(target)
print(index)

my_list = [1, 2, 3, 4, 5]

# Iterate over all pairs of elements in the list
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        # Check if the sum of the pair is equal to 6
        if my_list[i] + my_list[j] == 6:
            # Print the index positions of the pair
            print("Index positions:", i, j)




'''