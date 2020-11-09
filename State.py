# Let be a state as a cell of the maze with all its information,
# its value and its neighbours.
# The unique identifier for a state is the cell position (row, col).
class State:

    def __init__(self, row, column, node, neighbors):
        self.id = (row, column)
        self.node = node
        self.neighbors = sorted(neighbors)

    # Function to get the node
    # associated with the state
    def getNode(self):
        return self.node

    # Function to get the identifier
    def getId(self):
        return self.id

    # Function to get the list of neighbours
    def getNeighbors(self):
        return self.neighbors

    # Function to get the row of the cell
    def getRow(self):
        return self.id[0]

    # Function to get the column of the cell
    def getColumn(self):
        return self.id[1]
