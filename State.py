# Let be a state as a cell of the maze with all its information,
# its value and its neighbours.
# The unique identifier for a state is the cell position (row, col).
class State:

    def __init__(self, id, neighbors, heuristic, value):
        self.row, self.column = id
        self.id = id
        self.neighbors = neighbors
        self.heuristic = heuristic
        self.value = value
        print(self.value)

    def getHeuristic(self):
        return self.heuristic

    def getValue(self):
        return self.value

    # Function to get the identifier
    def getId(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"

    # Function to get the list of neighbours
    def getNeighbors(self):
        return self.neighbors

    # Function to get the row of the cell
    def getRow(self):
        return self.row

    # Function to get the column of the cell
    def getColumn(self):
        return self.column
