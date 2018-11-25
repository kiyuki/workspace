class Node:
    def __init__(self, key = 0):
        global count
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.depth = 0
        count = count + 1
        print("Node is created", count)

def rec(node):
    temp = Node()
    temp.depth = node.depth + 1
    if temp.depth > 3:
        return
    temp.parent = node
    print(temp.depth)
    node.left = temp
    rec(node.left)
    temp.parent = node
    node.right = temp
    rec(node.right)

if __name__ == "__main__":
    count = 0
    ins = Node(0)
    rec(ins)
