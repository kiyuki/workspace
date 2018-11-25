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


class Node:
    def __init__(self, location, parent, left, right):
        self.location = location
        self.parent = parent
        self.left = left
        self.right = right


class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.id < other.id

    def print(self):
        print(self.id)

class MyLibKDTree:
    def __init__(self, left, right, depth):
        self.np = 0

    def getNumOfPoint(self):
        temp = list(map(int, input().strip().split()))
        self.numOfPint = temp[0]

    def getPoints(self):
        self.points = [Point() for _ in range(self.numOfPoint)]
        for i in range(self.numOfPint):
            temp = list(map(int, input().strip().split()))
            self.points[i] = Point(0, temp[0], temp[1])  #### should fix id

    def getNumOfArea(self):
        temp = list(map(int, input().strip().split()))
        self.numOfArea = temp[0]

    def getArea(self):
        self.area = []


    def lessX(self, point1, point2):
        return point1.x < point2.x

    def lexxY(self, point1, point2):
        return point1.y < point2.y

    def makeKDTree(self, left, right, depth):
        if(not (left < right)):
            return None
        self.mid = (left + right) /2
        t = self.np + 1
        if depth % 2 == 0:
            pass


