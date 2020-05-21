def triangle(n):
    while n > 0:
        for j in range(n, 0, -1):
            print(j, end=' ')
        print('\n')
        n -= 1


n = int(input('Enter the number :'))
triangle(n)
