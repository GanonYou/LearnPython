#直线上黑点与白点连线问题，贪心法解决
P = [1,1,0,1,0,0,0,1]
#P = [0,1,1,0,0,1]
N = len(P)
totalLength = 0

for i in range(N):
    if P[i] != 0:
        continue

    flag = False
    j = i - 1
    #先向左找最近的黑点
    while j >= 0:
        if P[j] == 1:
            totalLength += i - j
            #用过的黑点就将P[j]置为-1
            P[j] = -1
            flag = True
            break
        j = j - 1
    
    if flag == True:
        continue
    
    j = i + 1
    #再向右找
    while j < N:
        if P[j] == 1:
            totalLength += j - i
            #用过的黑点就将P[j]置为-1
            P[j] = -1
            break
        j = j + 1


print(totalLength)
