from math import cos
#general method
def get_table_1(f):
    scale = 10
    table = dict()
    for num in range(1, 11, 1):
        x = num/scale
        table[x] = f(x)
    return table

#going more optimized using task indo
def get_table_2():
    #use the biggest value to ensure
    # that error won't be larger than has to for smaller cases
    scale = 10
    table = dict()
    computed = fsum_x(1)
    for num in range(1, 11, 1):
        x = num/scale
        table[x] = x*computed
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

table = get_table_1(fsum_x)
print(table)

