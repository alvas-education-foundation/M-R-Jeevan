'''
Given a list of numbers, write a Python program to count Even and Odd numbers in a List.
'''

O = []
E = []
l1 = [int(x) for x in input('Enter list : ').split()]
print(l1)
garbage = [E.append(x) if x%2 == 0 else O.append(x) for x in l1]
print(f'Even = {len(E)}, odd = {len(O)}')
