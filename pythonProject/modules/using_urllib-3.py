from urllib import  request

def fetch_xml(url):
    req=request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:',f.status,f.reason)
        for k,v in f.getheaders():
            print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

#url=r'http://weather.yahooapis.com/forecastrss?u=c&w=2151330'
url=r'https://www.baidu.com'
print(fetch_xml(url))