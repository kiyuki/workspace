class mlMSort:
    def __init__(self):
        self.cnt = 0
        self.MAX = 500000
        self.SENTINEL = 2000000000

    def mlMerge(self, DataArray, n, left, mid, right):
        n1 = mid - left
        n2 = right - mid
        L = [0] * round(self.MAX / 2)
        R = [0] * round(self.MAX / 2)
        # print("mlMerge:  dataArray, n, left, mid, right", DataArray[0:n], n, left, mid, right)
        # print("n1, n2", n1, n2)
        for i in range(n1):
            L[i] = DataArray[left + i]
        for i in range(n2):
            R[i] = DataArray[mid + i]
        # print("id", id(L), id(R))
        L[n1] = self.SENTINEL
        R[n2] = self.SENTINEL
        # print("id, L, R", id(L), id(R))
        # print("L: ", L[0:n] )
        # print("R: ", R[0:n])
        temp1, temp2 = 0, 0
        for i in range(left, right):
            self.cnt = self.cnt + 1
            if(L[temp1] <= R[temp2]):
                DataArray[i] = L[temp1]
                temp1 = temp1 + 1
            else:
                DataArray[i] = R[temp2]
                temp2 = temp2 + 1
        # print("DataArray: ", DataArray[0:n])


    def mlMergeSort(self, DataArray, n, left, right):
        if(left + 1 < right):
            # print("mlMergeSort:  n, left, right: ", n, left, right)
            mid = (left + right) / 2
            mid = round(mid)
            # print("mid", mid)
            self.mlMergeSort(DataArray, n ,left, mid)
            self.mlMergeSort(DataArray, n, mid, right)
            self.mlMerge(DataArray, n, left, mid, right)

    def getDataArray(self):
        self.dataArray = [0] * self.numOfFac
        for i in range(self.numOfFac):
            temp = list(map(int, input().strip().split()))
            self.dataArray[i] = temp[0]

    def getNumOfFac(self):
        n = list(map(int, input().strip().split()))
        self.numOfFac = n[0]

    def print(self):
        print(self.dataArray[0:self.numOfFac])



if __name__ == "__main__":
    ins = mlMSort()
    ins.getNumOfFac()
    ins.getDataArray()
    ins.mlMergeSort(ins.dataArray, ins.numOfFac, 0, ins.numOfFac)
    ins.print()


