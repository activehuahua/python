import string
import keyword

alphas=string.ascii_letters+'_'
nums=string.digits

myInput=input('Please input a char').strip()

while True:
        if myInput.lower()=='q':
            break
        if len(myInput) <=1:
            print('Please input again')
            break

        if myInput in keyword.kwlist:
            print('Your input char is a keyword!')
        else:
            print('Your input is not a keyword!')

        myInput=input('Please input a char').strip()


