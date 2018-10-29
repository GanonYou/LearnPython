#贪心法求解背包问题，物品可部分装入
P = [12,8,1,6,5]
W = [4,6,2,3,5]
M = 4
P_perWeight = []

#因为是可部分装入，所以求出每个物体的单位价值
for i in range(len(P)):
    P_perWeight.append(P[i] / W[i])

print(P_perWeight)
result = 0
while M > 0:
    #每次都选择单位价值最大的物体尽可能的多装
    maxPos = P_perWeight.index(max(P_perWeight))
    if M - W[maxPos] >= 0:
        M -= W[maxPos]
        result += W[maxPos] * P_perWeight[maxPos]
        W[maxPos] = 0
        P_perWeight[maxPos] = -1
    else:
        result += M * P_perWeight[maxPos]
        M = 0

print(result)