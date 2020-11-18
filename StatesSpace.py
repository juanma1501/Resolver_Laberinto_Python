import Board
from State import State


class StatesSpace:
    def __init__(self, board):
        self.board = board

    def getBoard(self):
        return self.board

    def successors(self, state):
        i = 0
        successors = []
        neighbors = state.getNeighbors()

        for cell in neighbors:
            if state.getRow - 1 == cell.getRow():
                mov = "N"
            elif state.getRow + 1 == cell.getRow():
                mov = "S"
            elif state.getColumn - 1 == cell.getColumn():
                mov = "O"
            elif state.getColumn + 1 == cell.getColumn():
                mov = "E"

            if cell.material == 0:
                cost = 1
            elif cell.material == 1:
                cost = 2
            elif cell.material == 2:
                cost = 3
            elif cell.material == 3:
                cost = 4

            state = State((cell.getRow(), cell.getColumn()), cell.neighbors(), self.heuristic(cell, cell.neighbors))

            successors.append([mov, state, cost])
            print(successors[1])
            i = i + 1

        return successors

    def heuristic(self, node, neighbors):
        heuristics = []

        for n in neighbors:
            h = self.heuristic_handler(node, n)
            heuristics.append(h)
        if heuristics == []:
            heuristics.append(0)
        return min(heuristics)

    def heuristic_handler(self, idNode1, idNode2):
        row1, col1 = idNode1
        row2, col2 = idNode2
        h = abs(row1 - row2) + (col1 - col2)
        return h
