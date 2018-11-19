class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        print("tree is defined!")


class TreeWithRoot:
    def __init__(self):
        self.tree = [Node() for i in range(100)]
        self.D = [None] * 100
        self.r = "default__DA!!"

    def getdepth(self, u):
        d = 0
        while self.tree[u].parent != None:
            u = self.tree[u].parent
            d = d + 1
        return d

    def maketree(self):
        temp = [int(i) for i in input().strip().split()]
        print("temp, Input List", temp)
        lnum = 0
        if temp[1] == 0:
            return
        for nodes in range(2, temp[1] + 2):
            print("nodes: ", nodes)
            if nodes == 2:
                self.tree[temp[0]].left = temp[nodes]
            else:
                self.tree[lnum].right = temp[nodes]
            lnum = temp[nodes]
            self.tree[temp[nodes]].parent = temp[0]
            print("temp[0]", temp[0])
            print("Nodes", temp[nodes], " :Set parent: ", self.tree[temp[nodes]].parent)


    def setDepth(self, u, p):
        pass

    def recDepth(self, node, dep):
        self.D[node] = dep
        if(self.tree[node].left is not None):
            self.recDepth(self.tree[node].left, dep + 1)
        if(self.tree[node].right is not None):
            self.recDepth(self.tree[node].right, dep)



    def printNode(self, u):
        i, c = 1, 2
        print("node", u, ": ", "parent = ", self.tree[u].parent, "depth = ", self.D[u] )

    def findRoot(self, x):
        for i in range(x):
            print(self.tree[i].parent, "tree ", i)
            if(self.tree[i].parent is None):
                print("find None", "num:", i)
                self.r = i

    def showTree(self, x):
        for i in range(x):
            print("tree node ", i, ":" , self.tree[x].parent)
            print("tree's id", id(self.tree[i]))


if __name__ == "__main__":
    n = int(input())
    t = TreeWithRoot()
    for i in range(n):
        t.maketree()
        t.showTree(n)
    t.findRoot(n)
    print("t.r", t.r)
    t.recDepth(t.r, 0)
    for i in range(n):
        t.printNode(i)


