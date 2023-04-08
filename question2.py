def tricky_list(lst):
    return lst[:-1] and lst[:-2] \
        if len(lst[1]) == len(lst[-1])\
        else lst[1:]

names = ["Ben", "Ken", "Len"]
print(tricky_list(names))
