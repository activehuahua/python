def printStar(n):
    arr = [([' '] *(2*n-1)) for i in range(n)]
    # print(arr)
    for i in range (0 , n):
        for j in range (0 , 2*i+1):
            arr[i][n-1-i+j] = '*'

    for i in range (0 , n):
         for j in range (0 , 2*n-1):
             print(arr[i][j],end=' ')
         print('')

printStar(6)
