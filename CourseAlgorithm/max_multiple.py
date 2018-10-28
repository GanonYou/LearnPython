## --------- 不带 K 的最大数乘 ---------
# import numpy as np

# def findMax(start,end):
#     if start == end:
#         m[start][end] = v[start]
#         return v[start]
#     if m[start][end] != 0:
#         return m[start][end]
#     for k in range(start,end):
#         a = findMax(start,k)
#         b = findMax(k + 1,end)
#         if (a + b) < (a * b):
#             m[start][end] = max(m[start][end],a * b)
#         else:
#             m[start][end] = max(m[start][end],a + b)
#     return m[start][end]

# #v = [1,2,3,4,5]
# v = [4,1,3,5]
# N = len(v)
# m = np.zeros([N,N])
# print(findMax(0,N - 1))
# print(m)

# --------- 带 K 的最大数乘 ---------
import numpy as np

v = [1,2,3,4,5]
N = len(v)
K = 2

sum = [0] * (N + 1)
f = np.zeros([N + 1,N])

for i in range(1,N + 1):
    sum[i] = sum[i - 1] + v[i - 1]
for i in range(1,N + 1):
    f[i][0] = sum[i]

#f[i][j]代表前 i 个数有 j 个乘号的最大值
#按行逐步完成 f 矩阵
for i in range(2,N + 1):
    #当有 i 个数的时候，最多只能存在 i-1 个乘号
    t = min(i - 1,K)
    #遍历 1 到 t 个乘号的情况
    for j in range(1,t + 1):
        #用 l 遍历新增一个乘号的所有位置
        for l in range(2,i + 1):
            f[i][j] = max(f[i][j],f[l - 1][j - 1] * (sum[i] - sum[l - 1]))

print(f)
print(f[N][K])
