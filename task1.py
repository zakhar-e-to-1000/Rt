from math import cos, tan, sin, log


def get_table3(f, g, d):
    scale = 10
    table = dict()
    for num in range(20, 31, 1):
        x = num/scale
        if (num < 23):
            table[x] = f(x)
        elif (num < 27):
            table[x] = g(x)
        else:
            table[x] = d(x)
    return table

def first(e):
    return cos(e)+tan(e)

def second(e):
    return (1/tan(e)) + sin(e)

def third(e):
    return (e*log(e))**3

table = get_table3(first, second, third)
print(table)