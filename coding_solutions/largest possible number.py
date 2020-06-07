"""
largest possible number
"""

def lpn(num):
    """ find largest possible number """
    n2 = []
    num3 = str(num)
    n2 = [int(x) for x in num3]
    n2.sort(reverse=True)
    num3 = 0
    for i in n2:
        num3 = num3*10 + i
    print(f'org : {num} , mod {num3}')
    return num == num3

num = int(input('Enter your number :'))
print(lpn(num))
