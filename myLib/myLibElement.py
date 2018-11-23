class DisjointSet:
    def __init__(self, size):
        self.rank = [0] * size
        self.p = [0] * size
        for i in range(size):
            self.makeSet(i)

    def getTwoNum(self):
        self.n , self.q = map(int, input().strip().split())
        print("self.n, self.q", self.n, self.q)

    def makeSet(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, elem1, elem2):
        self.link(self.findSet(elem1), self.findSet(elem2))


    def link(self, elem1, elem2):
        if(self.rank[elem1] > self.rank[elem2]):
            self.p[elem2] = elem1
        else:
            self.p[elem1] = elem2
            if self.rank[elem1] == self.rank[elem2]:
                self.rank[elem2] = self.rank[elem2] + 1

    def findSet(self, x):
        if x is not self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]

    def processQuery(self, numOfQ):
        for i in range(numOfQ):
            kindOfQ, elem1, elem2 = list(map(int, input().strip().split()))
            print("kindOfQ, elem1, elem2", kindOfQ, elem1, elem2)
            if kindOfQ == 0:
                self.unite(elem1, elem2)
            elif kindOfQ == 1:
                if self.same(elem1, elem2):
                    print(1)
                else:
                    print(0)
            self.print()

    def print(self):
        for i, j in enumerate(self.p):
            print("p", i, ": ", j)
        for i, j in enumerate(self.rank):
            print("rank", i, ": ", j)


if __name__ == "__main__":
    n, q = map(int, input().strip().split())
    disJointS = DisjointSet(n)
    disJointS.processQuery(q)

