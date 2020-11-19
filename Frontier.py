from Node import Node
from operator import itemgetter
from operator import attrgetter
class Frontier:
    def __init__(self):
        self.listFrontier = []

    def insert(self, nodeTree):
        self.listFrontier.append(nodeTree)
        """sorted(self.listFrontier, key=attrgetter('f'))
        sorted(self.listFrontier, key=attrgetter('state.row'))
        sorted(self.listFrontier, key=attrgetter('state.column'))
        sorted(self.listFrontier, key=attrgetter('state.column'))
        sorted(self.listFrontier, key=attrgetter('id'))"""
        self.listFrontier = sorted(self.listFrontier)



    def insertList(self, ln):
        for node in ln:
            self.insert(node)

    def delete(self):
        return self.listFrontier.pop()

    def isEmpty(self):
        return self.listFrontier == []

