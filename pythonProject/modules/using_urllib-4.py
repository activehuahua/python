from urllib import request,parse


req = request.Request(r'http://wap.fc.igemi.cn/pwap/zdyllb/?smi=442211&st=WEIXIN&buildingInfo=false&guide=false')
req.add_header('User-Agent', 'Mozilla/5.0 Linux')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read())