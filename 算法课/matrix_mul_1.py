import numpy
INF = float("inf")

def MatrixChainOrder(r):
    n = len(r)
    m = numpy.zeros([n,n])
    s = numpy.zeros([n,n])
    for i in range(n):
        m[i][i] = 0
    for x in range(1,n-1):
        for i in range(1,n-x):
            j = i + x
            m[i][j] = INF
            for k in range(i,j):
                q = m[i][k] + m[k + 1][j] + r[i - 1] * r[k] * r[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s

def printResult(i,j,flag,s):
    if i == j:
        print('M' + str(i),end = '')
    else:
        if flag != 0:
            print('(',end = '')
        printResult(i,int(s[i][j]),flag + 1,s)
        print('*',end = '')
        printResult(int(s[i][j]) + 1,j,flag + 1,s)
        if flag != 0:
            print(')',end = '')


r = [10,300]        #应当输出M1
#r = [10,100,5,50,10]    #应当输出(M1*M2)*(M3*M4)
#r = [30,35,15,5,10,20,25]   #应当输出(M1*(M2*M3))*((M4*M5)*M6)
m,s = MatrixChainOrder(r)
print(s)
printResult(1,len(r) - 1,0,s)
print()