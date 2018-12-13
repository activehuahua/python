age = 25
name = 'Swaroop'
print('{0} is {1} years old'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
print('{0:.3}'.format(1 / 4))
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
print('%s  is %s  years old' % (name, age))
print(5 | 3)


def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


printMax(1, 2)
printMax(2, 2)
printMax(3, 1)

number = 23
running = True
while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('Congratulation, you guessed it .')
        running = False
    elif guess < number:
        print('No, it is lower than that .')
    else:
        print('No, it is larger than that.')
else:
    print("the while loop is over.")
