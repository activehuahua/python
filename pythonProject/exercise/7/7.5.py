import  time
db={}
dbTime={}

def newuser():
    prompt='login desired:'
    while True:
        name=input(prompt)
        if db.get(name):
            prompt='name taken, try another:'
            continue
        else:
            break
    pwd=input('password:')
    db[name]=pwd
    dbTime[name]=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

def olduser():
    name=input('login:')
    pwd=input('password:')
    passwd=db.get(name)
    if passwd==pwd:
        dbTime[name]=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print('welcome back',name)
        print('last time is ',dbTime[name])

    else:
        print('login incorrect')

def showmenu():
    prompt='''
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    Enter Choice: '''

    done=False
    while not done:
        chosen=False
        while not chosen:
            try:
                choice=input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice='q'
            print('\n You picked:[%s]' %choice)
            if choice not in 'neq':
                print('Invalid option, try again')
            else:
                chosen=True

        if choice=='q' : done=True
        if choice=='n':newuser()
        if choice=='e' :olduser()

if __name__=='__main__':
    showmenu()
