class Node:
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.dep = 0
        self.exceed = False

class Weight:
    def __init__(self, dec = 0, inc = 0):
        self.dec = dec
        self.inc = inc

class PetTree:
    def __init__(self):
        self.day = None
        self.sWeight = None
        self.tWeight = None
        self.wData = None
        self.wTree = None
        self.count = 0
        self.count2 = 0

    def getSettingInfo(self):
        temp = list(map(int, input().strip().split()))
        self.day, self.sWeight, self.tWeight = temp

    def getWeightInfo(self):
        self.wData = [Weight() for _ in range(self.day)]
        for i in range(self.day):
            temp = list(map(int, input().strip().split()))
            self.wData[i].dec = -temp[0]
            self.wData[i].inc = temp[1]

    def makeTree(self, node):
        templ = Node(node.key)
        tempr = Node(node.key)
        # # # # print("node.dep", node.dep)
        templ.dep = node.dep + 1
        tempr.dep = node.dep + 1
        if tempr.dep > self.day or templ.dep > self.day:
            # # print("return, tempr.dep, templ.dep", tempr.dep, templ.dep)
            return
        # # # # print("temp.dep", temp.dep)
        templ.parent = node
        tempr.parent = node
        templ.exceed = node.exceed
        tempr.exceed = node.exceed
        keytemp = node.key
        # # # # print("keytemp", keytemp)
        templ.key = keytemp + self.getWeight(templ.dep -1, False)
        node.left = templ
        tempr.key = keytemp + self.getWeight(tempr.dep - 1, True)
        node.right = tempr
        # # print("keytemp, temp.key, False", keytemp, node.left.key ,self.getWeight(templ.dep -1, False), templ.dep)
        # # print("keytemp, temp.key, True", keytemp, node.right.key, self.getWeight(tempr.dep -1, True), tempr.dep)
        if node.left.key > self.tWeight:
            # # # print("temp.key, self.tWeight", temp.key, self.tWeight)
            node.left.exceed = True
        if node.right.key > self.tWeight:
            node.right.exceed = True
        if templ.dep == self.day :
            if templ.exceed == False:
                self.count = self.count + 1
        if tempr.dep == self.day:
           if tempr.exceed == False:
                self.count = self.count + 1
        self.count2 = self.count2 + 2
        # # print("self.count2", self.count2)
        self.makeTree(node.left)
        self.makeTree(node.right)


    def getWeight(self, dep, onOff):
        if onOff == False:
            # # # print("False: ", self.wData[dep].dec)
            return self.wData[dep].dec
        elif onOff == True:
            # # # print("True: ", self.wData[dep].inc)
            return self.wData[dep].inc

if __name__ == "__main__":
    ins = PetTree()
    ins.getSettingInfo()
    ins.getWeightInfo()
    ins.makeTree(Node(ins.sWeight))
    print(ins.count)


