def multiplication(a_list):
    new_list = []
    for any_value in a_list:
        new_element = 2 * any_value
        new_list.append(new_element)
    return  new_list

nums = [4,5,6,1,8]
print(nums)
print("Double the new list of number by  2:")
nums = multiplication(nums)
print(nums)

def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)

things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))
lst = [["hi", "bye"], "hello ", "Globa Warming! ", [9, 2], 4]

greeting_doubled = list(map(lambda x: x*2, lst))
print(greeting_doubled)

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def transformer(st):
    return st.upper()

abbrevs_upper = map(transformer, abbrevs)
abbrevs_upper = map(lambda st: st.upper(), abbrevs)
print(list(abbrevs_upper))
