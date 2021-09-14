total=0
def move(n,a,b,c):
    global total
    total += 1
    if n==1:
        print('move',a,'-->',c)
        return
    move(n-1,a,c,b)

    print('move',a,'-->',c)
    move(n-1,b,a,c)

move(100,'A','B','C')
print(total)