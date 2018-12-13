def triangles(max):
    n=2
    pre=[]
    while n<=3:
            pre=list(range(1,n))
            pre[-1]=1
            print(pre)
            n=n+1

    while n<max:
        new=list(range(1,n))
        new[-1]=1
        for i in range(n-1):
            if i>0 and i<n-2:
                new[i] = pre[i-1] + pre[i]
        print(new)
        pre=new
        n=n+1
    return new

triangles(11)