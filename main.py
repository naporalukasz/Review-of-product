import json
from Tree import Tree
from BinaryTree import BinaryTree
import numpy as np


def createTreeFromJson():
    with open('result.json') as jsonData:
        data = json.load(jsonData)

    dependencyParse = data["result"]["paragraphs"][0]["sentences"][0]["dependencyParse"]
    tokens = data["result"]["paragraphs"][0]["sentences"][0]["tokens"]

    nodeList = list()
    root = Tree("root", "root")

    for elem in tokens:
        id = elem["id"]
        val = elem["chosenInterpretation"]["base"]
        ctag = elem["chosenInterpretation"]["ctag"]
        nodeList.append(Tree(val, id, ctag))

    for place, elem in enumerate(dependencyParse):
        endTokenId = elem["endTokenId"]
        startTokenId = elem["startTokenId"]

        if startTokenId is None:
            child = next(x for x in nodeList if x.id == endTokenId)
            print(child)
            root.addChild(child)
        else:
            parent = next(x for x in nodeList if x.id == startTokenId)
            child = next(x for x in nodeList if x.id == endTokenId)
            parent.addChild(child)
            dependencyParse[place] = parent

    return root, nodeList


def convertToBinaryTree(treeRoot, nodelist):
    if not treeRoot.children:
        node = next(x for x in nodelist if x.id == treeRoot.id)
        newNode = BinaryTree("tmp", BinaryTree(node.getVal()))  # poprawi typ oda
        return newNode

    if len(treeRoot.children) == 1:
        newNode = convertToBinaryTree(treeRoot.children[0], nodelist)
        if newNode.right is None:
            newNode.right = BinaryTree(treeRoot.getVal())
        else:
            parent = BinaryTree("tmpParent1", newNode, BinaryTree(treeRoot.getVal()))
            return parent

    parent = None
    for child in treeRoot.children:
        newNode = convertToBinaryTree(child, nodelist)
        if parent is None:
            parent = newNode

        if parent.right is None:
            parent.right = BinaryTree(treeRoot.getVal())
        else:
            newParent = BinaryTree("tmpParent2", parent, newNode)
            parent = newParent
    return parent


def createTreeFromTxt():
    file = open("test_sentence.txt", "r")
    sentences = file.readlines()

    nodes=createNodesFromSentence(sentences[1])

    file = open("test_parents.txt", "r")
    parents = file.readlines()
    print(parents[0])


def createNodesFromSentence(sentence):
    nodeList = list()
    index = 1
    for label in sentence:
        nodeList.append(Tree(label, index))
        index + 1

    return nodeList

def buildTree(nodesList,parents):
    indexRoot = parents.find(x=0)
    root = next( x for x in nodesList if x.val == indexRoot)
    for parent in parents:
        if(parent != 0):
            r=2




def main():
    # part dedicated for trees svae in json file
    #  tree, nodeList = createTreeFromJson()
    #  #tree.printTree()
    #  binaryTree = convertToBinaryTree(tree, nodeList)
    #  finalvector = binaryTree.compute()
    #  print(finalvector)
    createTreeFromTxt()


if __name__ == "__main__":
    main()
