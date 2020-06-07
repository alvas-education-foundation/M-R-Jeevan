"""
A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a 
single-digit number is produced. This is only applicable to the natural numbers.
"""
def digitalroot(num):
    """ Return Digital Root Of A Number """
    if num < 0:
        raise ValueError
    if num < 10:
        return num
    else:
        num1 = 0
        while num > 0:
            num1 = num1 + num%10
            num = num//10
        # print(f'debug num = {num} num1 = {num1}')
        if num1 < 10 :
            return num1
        else:
            return digitalroot(num1)


num = int(input('Enter Number : '))
print(digitalroot(num))
