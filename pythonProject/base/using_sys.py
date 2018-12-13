import sys
import  os
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe pythonpath is ',sys.path,'\n')
print(os.getcwd())

if __name__== '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
