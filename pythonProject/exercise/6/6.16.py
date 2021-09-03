import  string
import  copy

def matrx(tuple1,tuple2):
    weidu_x=len(tuple1)
    weidu_y=len(tuple2[0])
    cell_len=len(tuple2)
    aaList=[]
    aList=[]
    #初始化单位元素
    for i in range(weidu_x):
        aList.append(0)
    # 初始化最终结果元素
    for i in range(weidu_x):
         bList=copy.deepcopy(aList)
         aaList.append(bList)
    print(aList,aaList)
    a=0

    for i in range(weidu_x):
        for j in range(weidu_y):
            for m in range(cell_len):
                a+=tuple1[i][m]*tuple2[m][j]
            aaList[i][j]=a
            a=0
    print(aaList)

if __name__=='__main__':
    tuple1=([1,2,3],[4,5,6])
    tuple2=([1,2,3,4],[4,5,6,8])
    tuple3=([1,4],[2,5],[3,6])
    tuple4=([1,4],[2,5],[3,6],[4,8])
    tuple5=([100,10],[10,100],[1,1000])
    tuple6=([1,2,3],[4,5,6],[7,8,9])
    tuple7=([100,10,1],[10,100,1],[1,1000,1])

    matrx(tuple1,tuple3)
    matrx(tuple2,tuple4)
    matrx(tuple1,tuple5)
    matrx(tuple6,tuple7)