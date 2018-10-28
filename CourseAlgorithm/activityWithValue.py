#activity = [[0,2,2],[0,3,3],[2,4,2],[2,5,4],[3,5,2],[4,6,1],[5,7,3]]
activity = [[0,1,2],[1,3,2],[2,4,3],[3,6,2],[5,7,5],[7,8,1]]
N = len(activity)
T = [0] * (N + 1)

#T[i]记录了前 i 个活动的最优权重和
#从T[1]开始直到T[N]，对应的是activity[0][...]到activity[N-1][...]
for i in range(0,N):
    j = i - 1
    temp = activity[i][2]
    while j >= 0:
        #找到 第一个 结束时间在当前活动开始之前的活动
        if activity[j][1] <= activity[i][0]:
            temp = max(temp,temp + T[j + 1])
            break
        j = j - 1
    T[i + 1] = max(T[i],temp)
    
print(T[N])