from io import StringIO

f=StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')
print(f.getvalue())


f=StringIO('Hello!\nHi!\nGoodbye!')

for line in f.readlines():
    print(line.strip())

# while True:
#     s=f.readline()
#     if s=='':
#         break
#     print(s.strip())