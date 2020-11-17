# Let be a state as a cell of the maze with all its information,
# its value and its neighbours.
# The unique identifier for a state is the cell position (row, col).
class State:

    def __init__(self, id, node, neighbors):
        self.id = id
        self.node = node
        self.neighbors = neighbors

    def __str__(self):
        return "(" + id[0] + ", " + id[1] + ")"

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

    def successors(self, state):
        i = 0
        successors = []
        neighbors = state.getNeighbors()

        for cell in neighbors:
            if state.getRow - 1 == cell.row:
                mov = "N"
            elif state.getRow + 1 == cell.row:
                mov = "S"
            elif state.getColumn - 1 == cell.column:
                mov = "O"
            elif state.getColumn + 1 == cell.column:
                mov = "E"
            state = cell
            cost = 1

            successors.append([mov, state, cost])
            i = i + 1

        return successors
