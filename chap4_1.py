import numpy as np

def findMax(start,end):
    if start == end:
        m[start][end] = v[start]
        return v[start]
    if m[start][end] != 0:
        return m[start][end]
    for k in range(start,end):
        a = findMax(start,k)
        b = findMax(k + 1,end)
        if (a + b) < (a * b):
            m[start][end] = max(m[start][end],a * b)
        else:
            m[start][end] = max(m[start][end],a + b)
    return m[start][end]

#v = [1,2,3,4,5]
v = [4,1,3,5]
N = len(v)
m = np.zeros([N,N])
print(findMax(0,N - 1))
print(m)
