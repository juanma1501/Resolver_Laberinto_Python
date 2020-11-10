from Node import Node

class Frontier:
    def __init__(self):
        self.listFrontier = self.createFrontier()

    def createFrontier(self):
        frontier = []
        return frontier

    def insert(self, nodeTree):
        self.listFrontier.append(nodeTree)
        self.listFrontier = sorted(self.listFrontier, key=lambda node: Node.getState().getColumn())
        self.listFrontier = sorted(self.listFrontier, key=lambda node: Node.getState().getRow())
        self.listFrontier = sorted(self.listFrontier, key=lambda node: Node.getF())

    def delete(self):
        return self.listFrontier.pop(0)

    def isEmpty(self):
        return self.listFrontier == []

