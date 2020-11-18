from Node import Node

class Frontier:
    def __init__(self):
        self.listFrontier = []

    def insert(self, nodeTree):
        self.listFrontier.append(nodeTree)
        self.listFrontier = sorted(self.listFrontier)


    def insertList(self, ln):
        for node in ln:
            self.insert(node)

    def delete(self):
        return self.listFrontier.pop()

    def isEmpty(self):
        return self.listFrontier == []

