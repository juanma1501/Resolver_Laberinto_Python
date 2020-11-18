import Board
from State import State


class StatesSpace:
    def __init__(self, board):
        self.board = board
        pass

    def getBoard(self):
        return self.board

    def successors(self, state):
        i = 0
        successors = []
        neighbors = state.getNeighbors()

        for cell in neighbors:
            if int(state.getRow()) - 1 == cell.getRow():
                mov = "N"
            elif int(state.getRow()) + 1 == cell.getRow():
                mov = "S"
            elif int(state.getColumn()) - 1 == cell.getColumn():
                mov = "O"
            elif int(state.getColumn()) + 1 == cell.getColumn():
                mov = "E"

            if cell.getMaterial() == 0:
                cost = 1
            elif cell.getMaterial() == 1:
                cost = 2
            elif cell.getMaterial() == 2:
                cost = 3
            elif cell.getMaterial() == 3:
                cost = 4

            state = State((cell.getRow(), cell.getColumn()), cell.getLinks(), self.calculateHeuristic(cell, cell.
                                                                                                      getLinks()))

            successors.append([mov, state, cost])
            i = i + 1

        return successors

    def calculateHeuristic(self, node, neighbors):
        heuristics = []

        for n in neighbors:
            h = self.heuristic_handler(node, n)
            heuristics.append(h)
        if heuristics == []:
            heuristics.append(0)
        return min(heuristics)

    def heuristic_handler(self, idNode1, idNode2):
        row1, col1 = idNode1.getRow(), idNode1.getColumn()
        row2, col2 = idNode2.getRow(), idNode2.getColumn()
        h = abs(row1 - row2) + abs(col1 - col2)
        return h
