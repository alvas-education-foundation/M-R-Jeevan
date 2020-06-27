'''
Given start and end of a range, write a Python program to 
print all negative numbers in given range.
'''

def negetivePrinter(a,b):
    if a < 0 and b < 0:
        for i in range(a, b, 1):
            print(i)
    else:
        for i in range(a, 0, 1):
            print(i)


print('*********************')
negetivePrinter(-5, 0)
print('*********************')
negetivePrinter(-34, -7)
print('*********************')
negetivePrinter(-56, 90)
print('*********************')
negetivePrinter(0, 67)
print('*********************')
