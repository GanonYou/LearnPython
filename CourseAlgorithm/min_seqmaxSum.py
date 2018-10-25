#最小化子序列最大值之和,动态规划法实现

a = [2,2,2,8,1,8,2,1]
#a = [17,1,16]
B = 17
N = len(a)
dp = [0] * N
dp[0] = a[0]

for i in range(1,N):
    j = i
    myMax = a[j]
    tempSum = 0
    minSum = a[j] + dp[j - 1]
    #j向前迭代，myMax记录组内最大值，tempSum记录组内元素和，minSum记录总的最小和
    #组内元素依次为a[j],a[j+1]......a[i-1],a[i]
    while j >= 0 and tempSum + a[j] <= B:
        myMax = max(myMax,a[j])
        tempSum += a[j]
        if j == 0:
            #j=0 时不存在dp[j-1]，直接当作是0
            minSum = min(minSum,myMax)
            break
        minSum = min(minSum,dp[j - 1] + myMax)
        j = j - 1
    dp[i] = minSum

print(dp[N - 1])


