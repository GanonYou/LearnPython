INF = 10000000

#自顶向下递归
def cut_2(p,n,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        r[n] = 0
        return r[n]
    temp = -INF
    for i in range(1,n + 1):
        temp = max(temp,p[i] + cut_2(p,n - i,r))
    r[n] = temp
    return r[n]

price = [0,1,5,8,9]
length = 4
result = [-INF] * (length + 1)
cut_2(price,length,result)
print(result)