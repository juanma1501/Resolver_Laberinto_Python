import itertools
from State import State


class Node:

    def __init__(self, parent, state, cost, strategy, action):
        # ID
        self.id = itertools.count().__next__()

        # Parent
        self.parentNode = parent

        # Domain information
        self.action = action
        self.state = state

        if strategy == 'GREEDY' or strategy == 'A*':
            self.heuristic = self.state.getHeuristic()
        else:
            self.heuristic = None

        if self.parentNode == None:
            self.cost = 0
            self.depth = 0
        else:
            self.cost = parent.getCost + cost
            self.depth = parent.getDepth + 1

        self.f = self.strategy(strategy)

    def getCost(self):
        return self.cost

    def getDepth(self):
        return self.depth

    def getF(self):
        return self.f

    def getId(self):
        return self.id

    def getState(self):
        return self.state

    def getParentId(self):
        return self.parentNode.getId()

    def getAction(self):
        return self.action

    def getHeuristic(self):
        return self.heuristic

    def strategy(self, strategy):
        if strategy == 'BREADTH':
            f = self.depth
        elif strategy == 'DEPTH':
            f = int(abs(1/self.depth))
        elif strategy == 'UNIFORM':
            f = self.cost
        elif strategy == 'GREEDY':
            f = self.heuristic
        elif strategy == 'A':
            f = self.heuristic + self.cost

        return f
