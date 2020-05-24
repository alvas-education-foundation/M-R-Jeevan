from time import time


def triangularseeries(n):
    ''' better if n > 999999 '''
    q = 1
    sum = 0
    print('The series are...')
    for i in range(n):
        sum += q
        q += 1
        print(sum)


def ts(n):
    ''' better if n < 999999 '''
    print('The series are...')
    for i in range(1,n+1):
        u = (i*(i+1))//2
        print(u)


n = int(input('Enter the number : '))
t1 = time()
triangularseeries(n)
t2 = time()
ts(n)
t3 = time()

print(f'\n\n time one :{t2-t1} \n time two :{t3-t2}')
