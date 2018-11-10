class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if (self.data < data):
                if self.right is None:
                    self.right = tree(data)
                else:
                    self.right.insert(data)
            elif( self.data > data):
                if self.left is None:
                    self.left = tree(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def showData(self):
        print(self.data)


if __name__ == "__main__":
    rootTree = tree(100)
    rootTree.insert(10)
    rootTree.insert(20)
    rootTree.insert(200)
    rootTree.insert(133)

    rootTree.PrintTree()


