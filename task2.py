from math import cos
def get_table(f):
    scale = 10
    table = dict()
    for num in range(1, 11, 1):
        x = num/scale
        table[x] = f(x)
    return table

def fsum_x(x):
    df = 0.001
    result = 0; k = 0
    while True:
        term = x*cos(2*k+1)/(2*k-1)/(2*k+3)
        if abs(term)<df:
            break
        result += term
        k += 1
    return result

table = get_table(fsum_x)
print(table)