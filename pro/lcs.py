class lcs:
    def __init__(self):
        self.setNum = None
        self.wordSet = None

    def getData(self):
        temp = input().strip().split()
        self.setNum = int(temp[0])
        self.wordSet = []
        self.wordSet = [[list(input().strip()) for _ in range(2)] for _ in\
                        range(self.setNum)]

    def showData(self):
        print(self.setNum)
        for i in self.wordSet:
            print(i)

    def findlcs(self):
        for num in range(self.setNum):
            word1, word2= self.wordSet[num]
            len1 = len(word1) + 1
            len2 = len(word2) + 1
            dpMap = [[0] * (len1) for _ in range(len2)]
            ansMap = [[""] * (len1) for _ in range(len2)]
            for w2 in range(1, len2):
                for w1 in range(1, len1):
                    w20 = w2 -1
                    w10 = w1 - 1
                    if word1[w10] == word2[w20]:
                        dpMap[w2][w1] = dpMap[w2 - 1][w1 - 1] + 1
                        ansMap[w2][w1] = ansMap[w2 - 1][w1 - 1] + word1[w10]
                    elif dpMap[w2 - 1][w1] < dpMap[w2][w1 - 1]:
                        dpMap[w2][w1] = dpMap[w2][w1 - 1]
                        ansMap[w2][w1] = ansMap[w2][w1 - 1]
                    elif dpMap[w2 - 1][w1] >= dpMap[w2][w1 - 1]:
                        dpMap[w2][w1] = dpMap[w2 - 1][w1]
                        ansMap[w2][w1] = ansMap[w2 - 1][w1]
            for i in dpMap:
                print(i)
            for i in ansMap:
                print(i)


if __name__ == "__main__":
    ins = lcs()
    ins.getData()
    ins.showData()
    ins.findlcs()


"""
5
aaaaa
aaaaaaaa
bbbbbbbbbb
asdfefcxv
kkkkasdf
lkafjowqe
ooakv
asdsfas
aaa
bbb
"""


