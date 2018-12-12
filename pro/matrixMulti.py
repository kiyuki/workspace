class matrixMalti:
    def __init__(self):
        self.num = None
        self.matrixSize = None

    def getData(self):
        temp = input().strip()
        self.num = int(temp[0])
        self.matrixSize = [0 * (self.num + 1)]
        for i in range(1, self.num):
            temp = [int(i) for i in input().strip().split()]
            self.matrixSize[i -1] = temp[0]
            self.matrixSize[i] = temp[1]
        print(self.num)
        print(self.matrixSize)


    def culcuMulti(self):
        for l in range(2, self.num):
            for i in range(1, self.num - l + 1):
                j = i + l - 1
                for k in range(i, j - 1):







"""
5
3 3
3 2
2 6
6 6
6 7

"""
