class JudgeTest:
    def __init__(self):
        self.numOfPeople = 0
        self.result = 0
        self.p = 0

    def getNumOfPeople(self):
        temp = list(map(int, input().strip().split()))
        self.numOfPeople = temp[0]

    def getResult(self):
        self.result = [0] * self.numOfPeople
        for i in range(self.numOfPeople):
            self.result[i] = input().strip().split()

    def print(self):
        print(self.numOfPeople)
        for i in range(self.numOfPeople):
            print(self.result[i])

    def judgeL(self, result):
        temp = result[1:6]
        temp = list(map(int, temp))
        sumResult = 0
        for i in range(5):
            sumResult = sumResult + temp[i]
        speResult = temp[3] + temp[4]
        return sumResult >= 350 and speResult >=160


    def judgeS(self, result):
        temp = result[1:6]
        temp = list(map(int, temp))
        sumResult = 0
        for i in range(5):
            sumResult = sumResult + temp[i]
        speResult = temp[1] + temp[2]
        return sumResult >= 350 and speResult >=160

    def judge(self):
        for i in range(self.numOfPeople):
            if self.result[i][0] == "s":
                if self.judgeS(self.result[i]):
                    self.p = self.p + 1
            if self.result[i][0] == "l":
                if self.judgeL(self.result[i]):
                    self.p = self.p + 1

if __name__ == "__main__":
    ins = JudgeTest()
    ins.getNumOfPeople()
    ins.getResult()
    ins.judge()
    print(ins.p)
