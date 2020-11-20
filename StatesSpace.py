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

            """"
            if cell.getValue() == 0:
                cost = 1
            elif cell.getValue() == 1:
                cost = 2
            elif cell.getValue() == 2:
                cost = 3
            elif cell.getValue() == 3:
                cost = 4
            """


            state = State((cell.getRow(), cell.getColumn()), cell.getLinks(), self.calculateHeuristic(cell, cell.
                                                                                                      getLinks()), cell.getValue())
            cost = int(cell.getValue()) + 1

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

    def heuristic_calculation(idNode1, target_row, target_column):
        row1, col1 = idNode1.getRow(), idNode1.getColumn()
        #print("eeeeeee"+target_row+" "+target_column)
        h = abs(int(row1) - target_row) + abs(int(col1) - target_column)
        return h
