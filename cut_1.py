INF = 10000000

def cut_1(p,n,r):
    r[0] = 0
    for x in range(1,n + 1):
        temp = -INF
        for i in range(1,x + 1):
            temp = max(temp,p[i] + r[x - i])
        r[x] = temp

price = [0,1,5,8,9]
length = 4
result = [0] * (length + 1)
cut_1(price,length,result)
print(result)