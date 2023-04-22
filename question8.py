def function(*args, b=2):
    results = (all(args),b)
    return  sum(results) == b

print(function(7,9,8,0,12, b=8))