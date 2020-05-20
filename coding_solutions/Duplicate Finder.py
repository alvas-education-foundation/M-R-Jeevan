'''
Given an array a[] of size n which contains elements from 0 to n-1, write a program which prints the duplicate elements of the given array. 
If no duplicate element is found print -1.
Input:
The first line of input must contains an integer n which denotes number of elements of Array. 
Second line contains n space separated integers denoting elements of array a[].
Output:
Print the duplicate elements from the given array.
'''
def duplicatefinder(n,a):
    if not len(a) == n:
        print('Length of array dose not match')
        exit(0)

    unique = []
    duplicate = []
    for e in a:
        if e in unique:
            duplicate.append(e)
        else:
            unique.append(e)

    if len(duplicate) == 0:
        print(-1)
    else:
        for e in duplicate:
            print(e, end=' ')


n = input()
a = [x for x in input().split()]
# print(len(a), n)
duplicatefinder(int(n), a)
