MAX = 500000
SENTINEL = 2000000000
cnt = 0

def mlMerge(DataArray, n, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    print("mlMerge:  dataArray, n, left, mid, right", DataArray[0:n], n, left, mid, right)
    print("n1, n2", n1, n2)
    global cnt
    for i in range(n1):
        L[i] = DataArray[left + i]
    for i in range(n2):
        R[i] = DataArray[mid + i]
    L[n1] = SENTINEL
    R[n2] = SENTINEL
    print("L: ", L[0:n] )
    print("R: ", R[0:n])
    temp1, temp2 = 0, 0
    for i in range(left, right):
        cnt = cnt + 1
        if(L[temp1] <= R[temp2]):
            DataArray[i] = L[temp1]
            temp1 = temp1 + 1
        else:
            DataArray[i] = R[temp2]
            temp2 = temp2 + 1
    print("DataArray: ", DataArray[0:n])


def mlMergeSort(DataArray, n, left, right):
    if(left + 1 < right):
        print("mlMergeSort:  n, left, right: ", n, left, right)
        mid = (left + right) / 2
        mid = round(mid)
        print("mid", mid)
        mlMergeSort(DataArray, n ,left, mid)
        mlMergeSort(DataArray, n, mid, right)
        mlMerge(DataArray, n, left, mid, right)


if __name__ == "__main__":
    L = [0] * round(MAX / 2)
    R = [0] * round(MAX / 2)
    print("type of MAX",type(MAX))
    print("type of L", type(L))
    dataArray = [0] * MAX
    i, cnt = 0, 0
    n = list(map(int, input().strip().split()))
    n = n[0]
    for i in range(n):
        temp = list(map(int, input().strip().split()))
        dataArray[i] = temp[0]
        print(temp[0])
    print("type of n ",type(n))
    print(dataArray[0:10])
    mlMergeSort(dataArray, n, 0, n)
    print(dataArray[0:10])
    for i in range(n):
        if dataArray[i]:
            print(dataArray[i])


