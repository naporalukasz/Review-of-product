class Tree:

    def __init__(self, val, id, ctag=None, children=None):
        self.val = val
        self.id = id
        self.ctag = ctag
        if children is None:
            self.children = list()
        else:
            self.children = children

    def getVal(self):
        return self.val

    def setVal(self, newval):
        self.val = newval

    def getLeft(self):
        return self.left

    def addChild(self, newChild):
        self.children.append(newChild)

    def printTree(self):
        if not self.children:
            print(self.val + " " + self.id)
            return
        else:
            for child in self.children:
                child.printTree()
                print(self.val + " " + self.id)