""" 
Find Second Largest Element in Given Array. 
"""

array = [int(x) for x in input('Enter Array : ').split()]


def short(array):
    """ Return Sorted Unique Elements Array """
    unique = set(array)
    unique = list(unique)
    unique.sort()
    return unique


def long(array):
    """ Return Sorted Unique Elements Array """
    unique = []
    for i in array:
        if i not in unique:
            unique.append(i)
    print(unique)
    unique.sort()
    return unique


print(f'Second largest Element is : {long(array)[-2]}')
print(f'Second Largest Element is : {short(array)[-2]}')
