"""
A program rotate an array by N positions
"""

array = [x for x in input('Enter array : ').split()]
n = int(input('Enter Number of positions : '))


def move(array, n):
    """ n is < than len(array)"""
    return array[n::] + array[0:n:]


def move2(array, n):
    """ n is > len(array)"""
    g = move(array, 1)
    for i in range(n-1):
        g = move(g, 1)
    return g


newarray = []
if n > len(array):
    newarray = move2(array, n)
else:
    newarray = move2(array, n)
# print(f'Moved Array is : {newarray}')
print('Moved Array is ')
for i in newarray:
    print(i, end=' ')
