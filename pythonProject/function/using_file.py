poem='''\
  Programming is fun
  When the work is done
  A Byte of Python 第13 章输入输出
  if you wanna make your work also fun:
  use Python!
  '''



f=open('poem.txt','a')
f.write(poem)
f.close()

f=open('poem.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end=' ')
f.close()