from Node import Node
class Frontier:
    def __init__(self):
        self.listFrontier = []

    def insert(self, nodeTree):
        self.listFrontier.append(nodeTree)
        """
        self.listFrontier = sorted(self.listFrontier, key=attrgetter('f'))
        self.listFrontier = sorted(self.listFrontier, key=attrgetter('state.row'))
        self.listFrontier = sorted(self.listFrontier, key=attrgetter('state.column'))
        self.listFrontier = sorted(self.listFrontier, key=attrgetter('state.column'))
        self.listFrontier = sorted(self.listFrontier, key=attrgetter('id'))"""
        self.listFrontier = sorted(self.listFrontier)



    def insertList(self, ln):
        for node in ln:
            self.insert(node)

    def delete(self):
        return self.listFrontier.pop(0)

    def isEmpty(self):
        return self.listFrontier == []

