from State import State


class StatesSpace:
    def __init__(self, board):
        self.board = board
        pass

    def getBoard(self):
        return self.board

    def successors(self, state):
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

    @staticmethod
    def heuristic_calculation(state_of_node, target_row, target_column):
        row1, col1 = state_of_node.getRow(), state_of_node.getColumn()
        h = abs(int(row1) - target_row) + abs(int(col1) - target_column)
        return h
