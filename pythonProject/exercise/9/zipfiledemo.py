import  zipfile

f=zipfile.ZipFile('zipfile.zip','w',zipfile.ZIP_DEFLATED)
f.write('test.txt')
f.close()