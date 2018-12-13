import  hashlib

db={'alex':'5d0fe6657d6083bfc40a5339e9736bdb'}
def get_md5(name,password):
    md5=hashlib.md5()
    md5.update((password+name+'the-salt').encode('utf-8'))

    return md5.hexdigest()

def register_md5(name,password):
    db[name]=get_md5(name,password)
    print('%s,%s,%s'%(name,password,db[name]))

def login(name, password):
    if name not in db:
        register_md5(name,password)
        login(name,password)
    elif db[name]==get_md5(name,password):
        print('Login Successful!')
    else:
        print('Wrong Password!')

if __name__=='__main__':
    login('alex','1234567')
    login('zhaojianghua','123456')