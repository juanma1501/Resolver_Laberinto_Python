class Node:
    class_counter = 0
    def __init__(self, parent, state, cost, strategy, action, depth):
        # ID
        self.id = Node.class_counter
        # Parent
        self.parentNode = parent

        # Domain information
        self.action = action
        self.state = state

        if strategy == 'GREEDY' or strategy == 'A*':
            self.heuristic = self.state.getHeuristic()
        else:
            self.heuristic = None

        self.cost = cost
        self.depth = depth

        self.f = self.strategy(strategy)
        Node.class_counter += 1

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

    def getParent(self):
        return self.parentNode

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
            if self.depth == 0:
                f = 0
            else:
                f = int(abs(1/self.depth))
        elif strategy == 'UNIFORM':
            f = self.cost
        elif strategy == 'GREEDY':
            f = self.heuristic
        elif strategy == 'A*':
            f = self.heuristic + self.cost

        return f
    def heuristic_calculation(self, origin_row, origin_column, target_row, target_column):
        h = abs(int(origin_row) - target_row) + abs(int(origin_column) - target_column)
        self.heuristic = h

    def __lt__(self, other):
        return (self.getF(), self.getState().getRow(), self.getState().getColumn(), self.getId()) < (other.getF(), self.getState().getRow(), self.getState().getColumn(), other.getId())
