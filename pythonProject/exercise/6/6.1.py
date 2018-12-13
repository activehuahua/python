import  string

str1='alex'
str2='fdfd'
str_source='Alexander'

if str_source.lower().find(str1.lower())>=0:
    print(str1+' is substr of the '+str_source)
else:
    print(str1+' is NOT substr of the '+str_source)

try:
    if str_source.index(str2,0)>=0:
        print(str2+' is substr of the '+str_source)
except:
    print(str2+' is NOT substr of the '+str_source)
