def sort_column(matrix: list[list[int]], c: int):
    lent = len(matrix)
    boo = True
    while boo:
        boo = False
        for i in range(0, lent-1):
            if matrix[i][c]>matrix[i+1][c]:
                boo = True
                matrix[i][c], matrix[i+1][c] = matrix[i+1][c], matrix[i][c]

def buble_sort(matrix: list[list[int]]):
    for c in range(len(matrix[0])):
        sort_column(matrix, c)

def super_quality_NASA_str(matrix):
    c_max = [0]*len(matrix[0])
    for row in matrix:
        for index, num in enumerate(row):
            c_max[index] = max(c_max[index], len(str(num)))
    result = ''
    for row in matrix:
        line = ''
        for index, num in enumerate(row):
            line += str(num).rjust(c_max[index])+' '
        result += line.rstrip()+'\n'
    return result.rstrip()

def f(matrix, i):
    row_len = len(matrix[i])
    # r + c = row_len - 1
    f_c = row_len-1-i
    res = 1
    for num in matrix[i][f_c+1 : row_len]:
        res *= num
    return res


def main():
    matrix = [[-1, -5, -47, -8,  -1],
              [-4, -98, -90, -45, -78],
              [-3, -2,  -5,  -9,  -4],
              [-8, -67, -33, -91, -40],
              [-2, -58, -11, -65, -77]]
    buble_sort(matrix)
    print(super_quality_NASA_str(matrix))
    print()
    frr = [[f(matrix, i)]*len(matrix[i]) for i in range(len(matrix))]
    F = sum([f(matrix, i) for i in range(len(matrix))])/len(matrix)
    print(super_quality_NASA_str(frr))
    print(F)


if __name__ == '__main__':
    main()

