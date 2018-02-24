import json
from Tree import Tree


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

    return root


def main():
    tree = createTreeFromJson()
    tree.printTree()


if __name__ == "__main__":
    main()
