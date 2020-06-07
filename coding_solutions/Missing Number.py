"""
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing,
the missing number is to be found.
"""


def check(num, length):
    """ Check For Missing Number """
    for i in range(0, length):
        try:
            if i+1 != num[i]:
                print(i+1)
                break
        except:
            print(i+1)


testcases = int(input('Number Of Testcases : '))
while testcases > 0:
    length = int(input('Enter Length of array : '))
    num = list(map(int, input('Enter Array : ').split()))
    check(num, length)
    testcases -= 1
