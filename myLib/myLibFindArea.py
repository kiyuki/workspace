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


