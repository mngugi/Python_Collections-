from string import Template

def strange_func(n):
    template = Template('$x is not the $y letter')
    result = []

    for i in range(n):
        result.append(lambda x: template.substitute(x=x, y=i))
    return result

funcs = strange_func(4)

for f in funcs:
    print(f('A'))
