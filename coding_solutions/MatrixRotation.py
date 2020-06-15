def print_matrix(m):
    for row in m:
        for ele in row:
            print(ele, end=' ')
        print('\n')


def ip():
    r = int(input('Row : '))
    c = int(input('Column : '))
    m = []
    for i in range(r):
        a = []
        for j in range(c):
            a.append(input(f'[{i}][{j}] : '))
        m.append(a)
    return m, r, c


def rotate(mat, r, c):
    mat2 = []
    for row in mat:
        a = []
        for i in range(1, c):
            a.append(row[i])
        a.append(row[0])
        mat2.append(a)
    return mat2


matrix, row, col = ip()
print('\n---i/p---')
print_matrix(matrix)
print(f'row:{row}  col:{col}\n--------')
n = int(input('Number times to rotate : '))

r = rotate(matrix, row, col)
n -= 1
while n > 0:
    r = rotate(r, row, col)
    n -= 1
print('\n---o/p---')
print_matrix(r)
