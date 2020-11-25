from State import State


class StatesSpace:
    def __init__(self, board):
        self.board = board
        pass

    def getBoard(self):
        return self.board

    def successors(self, state, problem):
        mov = None
        successors = []
        neighbors = state.getLinks()

        for cell in neighbors:
            if state.getRow() - 1 == cell.getRow():
                mov = "N"
            if state.getRow() + 1 == cell.getRow():
                mov = "S"
            if state.getColumn() - 1 == cell.getColumn():
                mov = "O"
            if state.getColumn() + 1 == cell.getColumn():
                mov = "E"

            new_state = State((cell.getRow(), cell.getColumn()), cell.getLinks())
            cost = int(cell.getValue()) + 1
            successors.append([mov, new_state, cost])

        return successors

    def calculateHeuristic(self, neighbors, problem):
        heuristics = []

        for n in neighbors:
            h = self.heuristic_calculation(n, int(problem.getRowO()), int(problem.getColO()))
            heuristics.append(h)
        if not heuristics:  # Significa que heuristic == []
            heuristics.append(0)
        return min(heuristics)

    @staticmethod
    def heuristic_calculation(idNode1, target_row, target_column):
        row1, col1 = idNode1.getRow(), idNode1.getColumn()
        h = abs(int(row1) - target_row) + abs(int(col1) - target_column)
        return h
