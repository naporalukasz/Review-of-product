import numpy as np


class BinaryTree:
    def __init__(self, id, left=None, right=None):
        self.vector = np.ones(50),
        self.id = id
        self.left = left
        self.right = right

    def setLeft(self, newLeft):
        self.left = newLeft

    def setRight(self, newRight):
        self.right = newRight

    def setVecto(self, value):
        self.vector = value

    def getVector(self):
        return self.vector

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def printTree(self):
        if not self.left:
            print(self.vector)
            return
        else:
            self.left.printTree()
            print(self.vector)
            self.right.printTree()

    def compute(self):
        if not self.left and not self.right:
            return self.vector

        leftvector = self.left.compute()
        rightvector = self.right.compute()

        return self.union(leftvector, rightvector)

    def union(self, leftVector, rigrtVector):
        return np.add(leftVector, rigrtVector)
