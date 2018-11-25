class mlQuickSort:
    def __init__(self):
        self.numOfFac = 0
        self.dataArray = []

    def getNumOfFac(self):
        temp = list(map(int, input().strip().split()))
        self.numOfFac = temp[0]

    def getData(self):
        self.dataArray = [0] * self.numOfFac
        for i in range(self.numOfFac):
            temp = list(map(int, input().strip().split()))
            self.dataArray[i] = temp[0]

    def partition(self, dataArray, num, left, right):
        pivot = self.dataArray[right]
        print("pivot", pivot)
        j = left
        lessPosi = left
        while j <= right:
            if self.dataArray[j] > pivot:
                j = j + 1
            else:
                temp = self.dataArray[lessPosi]
                self.dataArray[lessPosi] = self.dataArray[j]
                self.dataArray[j] = temp
                lessPosi = lessPosi + 1
                j = j + 1
                print("lessPosi", lessPosi)
        self.print()
        return lessPosi - 1

    def print(self):
        print(self.dataArray)

    def mlSort(self, num, left, right):
        if(left < right):
            temp = self.partition(self.dataArray, num, left, right)
            print(num, left, right)
            print("recursive partition is called")
            self.mlSort(num, left, temp -1)
            self.mlSort(num, temp + 1, right)

if __name__  == "__main__":
    ins = mlQuickSort()
    ins.getNumOfFac()
    ins.getData()
    ins.mlSort(ins.numOfFac, 0, ins.numOfFac - 1 )
    ins.print()


