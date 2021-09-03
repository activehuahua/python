import os

for tmpdir in ('\tmp',r'd:\temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print('no temp directory available')
        tmpdir=''

if tmpdir:
    os.chdir(tmpdir)
    cwd=os.getcwd()
    print('current directory is %s'%(cwd))

    if 'example' in os.listdir(cwd):
        pass
    else:
        os.mkdir('example')
    os.chdir('example')
    cwd=os.getcwd()
    print('new working directory is %s'%(cwd))
    print(os.listdir(cwd))

    fobj=open('test.txt','w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print(os.listdir(cwd))

    # 显示文件或目录全路径
    path=os.path.join(cwd,os.listdir(cwd)[0])
    print('path is ',path)
    #分隔路径和文件名称
    print(os.path.split(path))
    print(os.path.splitext(os.path.basename(path)))

    os.remove(path)
    os.listdir(cwd)
    os.chdir(os.pardir)
    os.rmdir('example')
    print('Done!')