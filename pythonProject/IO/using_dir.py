import  os,sys


command=''
DIR=sys.path[2]
while True:
    command=input('Please input command:')
    if command=='exit':
        break
    if command=='dir -l':
        for x in os.listdir(DIR):
            print(x)
            dir=DIR+os.sep+x
            for f in os.listdir(dir):
                if os.path.isfile(dir+os.sep+f):
                     print('\t-------',f)