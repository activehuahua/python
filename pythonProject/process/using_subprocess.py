# -*- coding: utf-8 -*-
import subprocess,sys
from subprocess import Popen,PIPE
import os

cmd = "nslookup www.python.org"
print('$nslookup www.python.org')

data = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
data.wait()
pout=data.stdout.read()
output=pout.decode('cp936').encode('gbk')
print(output)

