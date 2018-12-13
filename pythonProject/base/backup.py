import os
import time

source = 'e:\\pythonProject\\'

target_dir = 'e:\\pythonProject'

today = target_dir +os.sep+ time.strftime('%Y%m%d')
print(today)
now=time.strftime('%H%M%S')

comment=input('Please input comments--->')

if len(comment)<0:
    target=today+os.sep+now+'.zip'
else:
    target=today+os.sep+now+'_'+comment.replace(' ','_')+'.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory ', today)


print(target)
zip_command = r'"C:\Program Files\WinRAR\WinRAR.exe" a -r %s %s' %(target,source)
print(zip_command)
#zip_command =r'"C:\Program Files\WinRAR\WinRAR.exe" a -r e:\pythonProject\ssss.zip e:\pythonProject\\'
os.system(zip_command)
# print(zip_command)
# if os.system(zip_command) == 0:
#     print('Successful backup to', target)
# else:
#     print('Backup FAILED')
