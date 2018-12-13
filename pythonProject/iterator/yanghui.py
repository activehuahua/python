def triangles(max):
    n=2
    pre=list(range(1,n))
    print(pre)
    n=n+1
    pre=list(range(1,n))
    pre[-1]=1
    print(pre)
    while n<max:
        new=list(range(1,n+1))
        new[-1]=1
        for i in range(n):
            if i>0 and i<n-1:
                new[i] = pre[i-1] + pre[i]
        print(new)
        pre=new
        n=n+1
    return new

triangles(11)