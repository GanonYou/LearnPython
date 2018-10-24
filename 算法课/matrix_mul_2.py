import numpy
INF = 10000000

def MatrixChain(i,j):
    if i == j:
        m[i][j] = 0
        return
    m[i][j] = INF
    for k in range(i,j):
        a = m[i][k]
        b = m[k + 1][j]
        if a == -1:
            MatrixChain(i,k)
        if b == -1:
            MatrixChain(k + 1,j)
        q = a + b + r[i - 1] * r[k] * r[j]
        if q < m[i][j]:
            m[i][j] = q
            s[i][j] = k

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

#r = [10,100,5,50,10]
r = [30,35,15,5,10,20,25]
N = len(r)
m = numpy.full((N,N),-1)
s = numpy.full((N,N),-1)
MatrixChain(1,len(r) - 1)
print(m)
print(s)
printResult(1,len(r) - 1,0,s)
print()