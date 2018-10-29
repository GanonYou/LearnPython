#工厂生产问题，贪心算法实现
C = [2,3,5,9,4]
Y = [2,2,1,3,5]
store = 1
n = len(C)
X = [0] * n
cost = 0
last = 100000
myPos = 0

for i in range(n):
    #如果超额生产的产品即使算上存储成本也比之后的某个月生产成本要低
    if last + store < C[i]:
        #引入一个myPos变量，用来记录那些需要超额生产的月份，当前月份则是i
        X[myPos] += Y[i]
    else:
        myPos = i
        #自产自销的月份
        X[i] += Y[i]
    last = min(last + store,C[i])
    cost += last * Y[i]

print(X)
print(cost)