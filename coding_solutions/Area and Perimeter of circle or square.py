def cc():
    r = int(input('Enter radius of circle : '))
    print('Circle Circumference is : '+str(2*(22/7)*r))


def ca():
    r = int(input('Enter radius of circle : '))
    print('Circle Area is : '+str((22/7)*r*r))


def sp():
    l = int(input('Enter side length : '))
    print('Square Perimeter is : '+str(l*4))


def sa():
    l = int(input('Enter side length : '))
    print('Square Area is : '+str(l*l))


def switch(n):
    if n == '1':
        cc()
    elif n == '2':
        ca()
    elif n == '3':
        sp()
    elif n == '4':
        sa()
    else:
        print('Invalid option ! ')
        # raise ValueError


while True:
    print('\tMenu\n1.Circle Circumference  \n2.Circle Area\n3.Square Perimeter\n4.Square Area\n Type exit to quit\n '
          'Enter an option : ')
    n = input()
    if n == 'exit':
        exit(0)
    else:
        switch(n)
