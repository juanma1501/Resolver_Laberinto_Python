import itertools
import random


class Node:

    def __init__(self, parent, state, cost, f, action):
        self.parentNode = parent
        self.id = itertools.count().next
        self.state = state
        self.value = value
        self.depth = parent.getDepth() + depth
        self.cost = parent.getCost() + cost
        self.action = action

    def getCost(self):
        return self.cost

    def getDepth(self):
        return self.depth

    def getValue(self):
        return self.value

    def getId(self):
        return self.id

