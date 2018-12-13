def prints(message, times=1):
    print(message * times)
prints('*', 10)

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count
print(total(10, 1, 2, 3, vegetables=50, fruits=100))

def printMax(x, y):
    '''Prints the maximum of two numbers.
   The two values must be integers.'''
    x = int(x)  # convert to integers, if possible
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
printMax(3, 5)
print(printMax.__doc__)
