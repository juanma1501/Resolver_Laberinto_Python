


class Node:
    class_counter = 0 #Variable to store the id of the nodes, it starts in 0 and will increase as new nodes are created

    def __init__(self, parent, state, cost, strategy, action, depth):
        # ID
        self.id = Node.class_counter
        # Parent
        self.parentNode = parent

        # Domain information
        self.action = action
        self.state = state

        self.heuristic = 0

        self.cost = cost
        self.depth = depth

        self.f = self.strategy(strategy)
        Node.class_counter += 1

    # Getter of variable cost
    def getCost(self):
        return self.cost

    # Getter of variable depth
    def getDepth(self):
        return self.depth

    # Getter of variable f
    def getF(self):
        return self.f

    # Getter of variable id
    def getId(self):
        return self.id

    # Getter of variable state
    def getState(self):
        return self.state

    # Getter of variable parent
    def getParent(self):
        return self.parentNode

    # Getter of id of the parent node
    def getParentId(self):
        return self.parentNode.getId()

    # Getter of variable action
    def getAction(self):
        return self.action

    # Getter of variable heuristic
    def getHeuristic(self):
        return self.heuristic

    #This function will give value to the variable f, (value),
    #according to the chosen strategy
    def strategy(self, strategy):
        if strategy == 'BREADTH':
            f = self.depth
        elif strategy == 'DEPTH':
            if self.depth == 0:
                f = 1.0
            else:
                aux = self.depth + 1
                f = float(abs(1 / aux))
        elif strategy == 'UNIFORM':
            f = self.cost
        elif strategy == 'GREEDY':
            f = self.heuristic
        elif strategy == 'A':
            f = self.heuristic + self.cost

        return f

    #Function to calculate the heuristic according to manhattan distance
    def heuristic_calculation(self, origin_row, origin_column, target_row, target_column):
        h = abs(int(origin_row) - target_row) + abs(int(origin_column) - target_column)
        self.getState().heuristic = h
        self.heuristic = h

    #Function used to sort the frontier according to the criterion said by the teacher
    def __lt__(self, other):
        return (self.getF(), self.getState().getRow(), self.getState().getColumn(), self.getId()) < (
        other.getF(), other.getState().getRow(), other.getState().getColumn(), other.getId())
