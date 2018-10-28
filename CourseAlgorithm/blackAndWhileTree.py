import numpy as np

#二叉树结点类
class Node(object):
    def __init__(self,elem = -1,lchild = None,rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

#二叉树类  
class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []
        self.allQueue = []
    
    #按照层次遍历的顺序构造二叉树使其尽量平衡
    def add(self,elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
            self.allQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
                self.allQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.allQueue.append(treeNode.rchild)
                self.myQueue.pop(0)
    
    #返回一个按层次遍历整个二叉树的数组
    def getAllQueue(self):
        return self.allQueue

#建立一颗有N个结点的树
N = 10
#生成N个数据作为树节点
elems = range(N) 
#新建一个树对象       
tree = Tree()          
for elem in elems:                  
    tree.add(elem)

queue = tree.getAllQueue() 

#自底向上找到尽量多的结点着黑色的方法，i从最下层结点开始
#f[i][0]代表以i为根结点且i为白色时的所求值；f[i][1]代表以i为根结点且i为黑色时的所求值
f = np.zeros([N,2])

i = N - 1
while i >= 0:
    if queue[i].lchild == None and queue[i].rchild == None:
        f[i][0] = 0
        f[i][1] = 1
    if queue[i].lchild != None and queue[i].rchild == None:
        f[i][0] = f[queue[i].lchild.elem][1]
        f[i][1] = f[queue[i].lchild.elem][0] + 1
    if queue[i].lchild != None and queue[i].rchild != None:
        f[i][0] = f[queue[i].lchild.elem][1] + f[queue[i].rchild.elem][1]
        f[i][1] = f[queue[i].lchild.elem][0] + f[queue[i].rchild.elem][0] + 1
    i = i - 1

print('\n最多可以染 ' + str(int(max(f[0][0],f[0][1]))) + ' 个黑色结点') 