# 输出标准错误输出
import  sys
print('This is alex',file=sys.stderr)

print("fatal error", file=sys.stderr)

print(5/2)

print(-2*4+3**2)

n1=10
n2=11.1
print(int(n1*n2))

n1= 0o101
print(n1,n2)