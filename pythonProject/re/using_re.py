import  re

# if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
#     print('OK')
# else:
#     print('FAIL')
#
# if re.match(r'^\d{3}\-\d{3,8}$', '010 12345'):
#     print('OK')
# else:
#     print('FAIL')
#
# print(re.split('[\s\,\:]+','a ,b:c:d'))
#
# m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
#
# t = '19:5:30'
# m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0-9]+)\:([0-9]+)$', t)
# print(m.groups())
#
# m=re.match(r'^(\d+?)(0*)$', '102300')
# print(m.groups())
#
# email=r'someon@microsoft.com'
# if re.match(r'[\w+.]+@[\w+.]+',email):
#     print('OK')
# else:
#     print('FAIL')

#email=r'<Tom Paris> tom@voyager.org'
#email=r'<Tom Paris>'
#m= re.match(r'(^<[\w+\s+]+>$)([\w+.]+@[\w+.]+)',email)
#m= re.match(r'(^<[\w+\s+]+>\s)([\w+.]+@[\w+.]+)',email)
#print(m.groups())

#
# regex=r'(^<\w+\s+]+>\s)?([\w+.]+@[\w+]+\.+)'
#
# m=re.compile(regex)
#
# if m.match('someone@gmailcom'):
#     print('match someone@gmail.com')
# if m.match('bill.gates@microsoft.com'):
#     print('match bill.gates@microsoft.com')
# if m.match('<Tom Paris> tom@voyager.org'):
#     print('match <Tom Paris> tom@voyager.org')
#
# m_email=m.match('<Tom Paris> tom@voyager.org').group(2)
# print(m_email)


m = re.match(r'([a-z]+)([\d]+)([a-z]+)', 'asdf2342sdf')
# if m:
#     print('Match')
# else:
#     print('Fail')
print(m.group(2))