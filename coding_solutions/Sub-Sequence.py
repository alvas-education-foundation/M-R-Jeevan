  
'''
"A subsequence is a sequence that can be derived from another sequence by deleting some elements 
without changing the order of the remaining elements"

Q.A user will input two strings, and we find if one of the strings is a sub sequence of the other. 
Program prints “yes” if either the first string is a sub sequence of the second string or the 
second string is a sub sequence of the first string.

Assume that, the length of the first string is smaller than or equal to the length of the second string.

Expected output :

Input the first string : tree
Input the second string : Computer science is awesome
YES
'''

def subsequebce(a,b):
    i = 0
    for s in a:
        if s in b[i::]:
            i = b.index(s)
        else:
            return False
    return True


str1 = input('Enter String 1 :')
str2 = input('Enter String 2 : ')

if subsequebce(str1,str2) or subsequebce(str2,str1):
    print('True')
else:
    print('False')


