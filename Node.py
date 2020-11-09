import itertools


class Node:

    def __init__(self, parent, state, cost, f, action):
        self.parentNode = parent
        self.id = itertools.count().next
        self.state = state
        self.f = f
        self.depth = parent.getDepth() + 1
        self.cost = parent.getCost() + cost
        self.action = action

    def getCost(self):
        return self.cost

    def getDepth(self):
        return self.depth

    def getF(self):
        return self.f

    def getId(self):
        return self.id

