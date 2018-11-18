class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None


class TreeWithRoot:
    def __init__(self):
        self.tree = [Node] * 100
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
        lnum = 0
        for nodes in range(temp[1]):
            if nodes == 0:
                self.tree[temp[0]].left = temp[nodes]
            else:
                self.tree[lnum].right = temp[nodes]
            lnum = temp[nodes]
            self.tree[nodes].parent = temp[0]


    def setDepth(self, u, p):
        pass

    def recDepth(self, u, p):
        self.D[u] = p
        if(self.tree[u].left is not None):
            self.recDepth(self, self.tree[u].r, p)
        if(self.tree[u].right is not None):
            self.recDepth(self.tree[u].right, p)



    def printNode(self, u):
        i, c = 1, 2
        print("node", u, ": ", "parent = ", self.tree[u].p, "depth = ", self.D[u] )

    def findRoot(self, x):
        for i in range(x):
            print(self.tree[i].parent, "tree i")
            if(self.tree[i].parent is None):
                print("find None")
                self.r = x

if __name__ == "__main__":
    print("tes")
    print(10)
    print(int(1000))
    n = int(input())
    t = TreeWithRoot()
    for i in range(n):
        t.maketree()
    t.findRoot(n)
    t.recDepth(t.r, 0)
    for i in range(n):
        t.printNode(i)


