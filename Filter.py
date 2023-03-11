def keep_events(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


print(keep_events([2,3,6,4,0,8,7,9,10,11,13,15,17]))

print("------------------------------")
def keepEvent(numbers):
    new_seq = filter(lambda numbers:  num % 2 ==0, numbers)
    return  list(new_seq)
print(keep_events([2,3,6,4,0,8,7,9,10,11,13,15,17]))

print("------------------------------")
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = filter(lambda word: "w" in word, lst_check)
filtered_words = list(filter_testing)

print(filtered_words)
print("------------------------------")

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = filter(lambda word: "o" in word, lst)
filtered_lists = list(lst2)
print(filtered_lists)

